import configparser

# CREATE OBJECT
configFile = configparser.ConfigParser()

# ADD SECTION
configFile.add_section("default")
configFile.add_section("credentials")

# ADD SETTINGS TO SECTION
configFile.set("default", "localPathToWatch", r"C:\Users\sandeep.tadde\Desktop\datafile\clg\samplepath")
configFile.set("default", "localPathToOrc", r"C:\Users\sandeep.tadde\Desktop\datafile\clg\orcfiles")
configFile.set("default", "localPathToLogs", r"E:\AWSPOC\logs\task1.log")
configFile.set("default", "bucketName", "snowflakeusingsns")

configFile.set("credentials", "accessKey", "AKIARCWOZRROUSSAAB4H")
configFile.set("credentials", "secretKey", "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")

# TASK 3
configFile.set("default", "srcHost", "database-1.cdojfx1iohkq.us-east-1.rds.amazonaws.com")
configFile.set("credentials", "srcUser", "admin")
configFile.set("credentials", "srcPassword", "12345678")

configFile.set("default", "desHost", "database-3.cdojfx1iohkq.us-east-1.rds.amazonaws.com")
configFile.set("credentials", "desUser", "postgres")
configFile.set("credentials", "desPassword", "abcdefghijkl")

# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configFileObj:
    configFile.write(configFileObj)
    configFileObj.flush()
    configFileObj.close()


