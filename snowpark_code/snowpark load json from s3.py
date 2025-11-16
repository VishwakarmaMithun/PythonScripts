import snowflake
import snowflake.snowpark.functions
from snowflake.snowpark.functions import col
from snowflake.snowpark import Session
from snowflake.snowpark.types import DataType,StringType,StructField,StructType,DateType
import os

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

session  = Session.builder.configs(connection_parameters).create()
session.sql("use warehouse compute_wh").collect

employee_json  = session.read.json('@my_s3_stage_json')
employee_json.show();
employee_json.select_expr("$1:address").show();
