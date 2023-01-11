 drop database if exists s3_to_snowflake_using_sns; 

--database creattion

create database s3_to_snowflake_using_sns


use s3_to_snowflake_using_sns

use role accountadmin


--s3 integration 

create or replace storage integration s3_int
TYPE = EXTERNAL_STAGE
STORAGE_PROVIDER = S3
ENABLED = TRUE
STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::074521873501:role/Snowflake_SNS_Role'
STORAGE_ALLOWED_LOCATIONS = ('s3://snowflakeusingsns')
COMMENT = 'Snowflake external table refresh'

DESC INTEGRATION s3_int;

--creating stage

create stage SnowFlakeUsingSnsExternalStage
url = 's3://snowflakeusingsns'
storage_integration = s3_int;


list @SnowFlakeUsingSnsExternalStage

-- creating orc format

create or replace file format my_orc_format
type = orc 
null_if = ('NULL', 'null');

-- Returns an AWS IAM policy statement that must be added to the Amazon SNS topic policy in order to grant the Amazon SQS 

select system$get_aws_sns_iam_policy('arn:aws:sns:us-east-1:074521873501:TopicSNS');



--external table

create or replace external table s3_to_snowflake_using_sns.public.test_dataset
with location = @SnowFlakeUsingSnsExternalStage file_format = 'my_orc_format'

select * from s3_to_snowflake_using_sns.public.test_dataset



-- select t.$1:"id",t.$1:"col2",t.$1:"col3",t.$1:"col4",t.$1:"col5" 
-- ,t.$1:"col6"
-- ,t.$1:"col7"
-- ,t.$1:"col8"
-- ,t.$1:"col9"
-- ,t.$1:"col10"
-- ,t.$1:"col11"
-- ,t.$1:"col12"
-- ,t.$1:"col13"
-- ,t.$1:"col14"
-- ,t.$1:"col15"
-- ,t.$1:"col16"
-- ,t.$1:"col17"
--   from @SnowFlakeUsingSnsExternalStage (file_format => my_orc_format) t;

