#pip install pymysql
#pip install psycopg2

import pymysql
import psycopg2
import helper
import pandas as pd


config = helper.read_config()
srcHost = config['default']['srcHost']
srcUser = config['credentials']['srcUser']
srcPassword = config['credentials']['srcPassword']

desHost = config['default']['desHost']
desUser = config['credentials']['desUser']
desPassword = config['credentials']['desPassword']


#Source Db connection
dbSrc = pymysql.connect(host= srcHost, user= srcUser, password = srcPassword)
cursor = dbSrc.cursor()

sourceDbCreation = '''create database if not exists RdsDataBase;'''

useSourceDb = '''use RdsDataBase;''' 

dropSrcTable = '''drop table if exists employeeData;'''

createSrcTable = '''
create table employeeData(employee_id int,
employee_name varchar(50),
employee_department varchar(50),
state varchar(50),
salary int,
age int,
bonus int);
'''
insertSrcData = '''
insert into employeeData(employee_id,employee_name,employee_department,state,salary,age,bonus)
values(1,'James','Sales','NY',90000,34,10000)
,(2,'Michael','Sales','NY',86000,56,20000)
,(3,'Robert','Sales','CA',81000,30,23000)
,(4,'Maria','Finance','CA',90000,24,23000)
,(5,'Raman','Finance','CA',99000,40,24000)
,(6,'Scott','Finance','NY',83000,36,19000)
,(7,'Jen','Finance','NY',79000,53,15000)
,(8,'Jeff','Marketing','CA',80000,25,18000)
,(9,'Kumar','Marketing','NY',91000,50,21000)'''

selectSrcData = '''select * from employeeData;'''
cursor.execute(sourceDbCreation)
cursor.execute(useSourceDb)
cursor.execute(dropSrcTable)
cursor.execute(createSrcTable)
cursor.execute(insertSrcData)
df = pd.read_sql('SELECT * FROM employeeData', con=dbSrc)

fetchSrcResult = df[df['employee_department'] == 'Finance']

#Destination Db Creation
dbDes = psycopg2.connect(host= desHost, user= desUser, password= desPassword)

dbDes.autocommit = True

cursor = dbDes.cursor()

createDestDb = '''
SELECT 'CREATE DATABASE PostgresDestDataBase' 
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'PostgresDestDataBase')'''

useDestDb = '''use PostgresDestDataBase;''' 

CreateDestTable = '''
create table if not exists employeeDestData(employee_id int,
employee_name varchar(50),
employee_department varchar(50),
state varchar(50),
salary int,
age int,
bonus int);'''

cursor.execute(createDestDb)

# cursor.execute(useDestDb)

cursor.execute(CreateDestTable)
fetchSrcResult= list(map(tuple, fetchSrcResult.to_numpy()))

for d in fetchSrcResult:    
    cursor.execute("INSERT into employeeDestData(employee_id,employee_name,employee_department,state,salary,age,bonus) VALUES (%s, %s, %s,%s, %s, %s, %s)", d)

result = '''select * from employeeDestData'''
cursor.execute(result)

varRes=cursor.fetchall()
print(varRes)
