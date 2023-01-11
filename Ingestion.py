from multiprocessing.connection import wait
import boto3
from botocore.exceptions import NoCredentialsError
import os
import changeformat 
import helper
import logging
from datetime import date

# READ INPUT VALUES AND CREDENTIALS FROM CONFIG FILE
config = helper.read_config()
pathToWatch = config['default']['localPathToWatch']
orcFilePath = config['default']['localPathToOrc']
localPathToLogs = config['default']['localPathToLogs']
bucketName = config['default']['bucketName']

ACCESS_KEY = config['credentials']['accessKey']
SECRET_KEY = config['credentials']['secretKey']

# STORING LOGS 
today = date.today()
logging.basicConfig(filename= localPathToLogs + str(today), format='%(asctime)s | %(levelname)s: %(message)s', level=logging.NOTSET)

logging.error('Something unexpected and important happened.')
logging.critical('The code cannot run!')

# FUNCTION TO LOAD ORC FILE TO S3
def upload_to_aws(localFile, bucket, s3File):
    """Uploads the converted file to S3 to the specified Bucket"""

    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)
    try:
        s3.upload_file(localFile, bucket, s3File)
        logging.debug(file  + " uploaded to S3 sucessfully.")
        return True
    except FileNotFoundError:
        logging.error("The file was not found")
        return False
    except NoCredentialsError:
        logging.error("Credentials not available")
        return False


# CONVERT ALL THE FILES IN THE LOCAL PATH TO ORC AND LOAD TO S3
newFiles = dict ([(f, None) for f in os.listdir (pathToWatch)])
for file in newFiles:
    try:        
        # CONVERT .CSV FILE TO .ORC
        changeformat.converttoORC(pathToWatch + '\\' + file,orcFilePath + '\\'+file[:-3] + 'orc' ) 
        # print(upload_to_aws.__doc__)
        logging.debug(file  + " converted to ORC sucessfully.")
        # MOVE CONVERTED FILE TO ARCHIVE FOLDER
        os.rename(pathToWatch + '\\' + file,r'C:\Users\sandeep.tadde\Desktop\datafile\clg\archive' + '\\'+file)
        logging.debug(file  + " moved to archive.")
    except:
        logging.error('File not moved to S3.')
    
    uploaded = upload_to_aws(orcFilePath + '\\'+file[:-3] + 'orc', bucketName, file[:-3] + 'orc' )
    


