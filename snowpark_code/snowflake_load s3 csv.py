import snowflake
from snowflake.snowpark.functions import col
from snowflake.snowpark.types import DataType,IntegerType,DecimalType,StructType,StructField,StringType
from snowflake.snowpark import Session
from dotenv import load_dotenv
import pandas as pd
import os

load_dotenv()


snowflake_password = os.getenv("snowflake_password")
snowflake_user = os.getenv("snowflake_user")
snowflake_account= os.getenv("snowflake_account")
snowflake_role = os.getenv("snowflake_role")
snowflake_warehouse= os.getenv("snowflake_warehouse")
snowflake_database= os.getenv("snowflake_database")
snowflake_schema= os.getenv("snowflake_schema")

connection_parameters = {
    "user": snowflake_user,
    "password": snowflake_password,
    "account":'oialxdd-xqb21073',
    "role": snowflake_role,
    "warehouse":snowflake_warehouse,
    "database":'HRMS',
    "schema":'ETL'
}

session = Session.builder.configs(connection_parameters).create()
sf = session.sql("use warehouse compute_wh").collect

employee_csv =  session.read.csv('@MY_S3_STAGE')
schema =  StructType([StructField("first name",StringType()),
StructField("last name",StringType()),
StructField("birthdate",StringType()),
StructField("address",StringType()),
StructField("city",StringType())
])


employee_csv =  session.read.schema(schema).csv('@MY_S3_STAGE')
employee_csv =  session.read.options({"ON_ERROR":"CONTINUE"}).schema(schema).csv('@MY_S3_STAGE')
employee_csv.show()
print(type(employee_csv))
employee_csv=employee_csv.cache_result()
print(employee_csv.is_cached)


employee_csv.queries