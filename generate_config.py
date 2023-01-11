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

configFile.set("credentials", "accessKey", "<AccessKey>")
configFile.set("credentials", "secretKey", "<SecretKey>")

# SAVE CONFIG FILE
with open(r"configurations.ini", 'w') as configFileObj:
    configFile.write(configFileObj)
    configFileObj.flush()
    configFileObj.close()


