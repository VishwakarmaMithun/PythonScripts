from snowflake.snowpark.functions import col
import time
import snowflake
from snowflake.snowpark import Session
from snowflake.snowpark.types import StructType,DataType,StringType,IntegerType,StructField
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

session = Session.builder.configs(connection_parameters).create()
df = session.table('SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.CUSTOMER')
df = df.filter(col("C_NATIONKEY")=='23').select("C_NAME")
dtwrite = df.write.mode("overwrite").saveAsTable("HRMS.ETL.CUSTOMER")
df.write.mode("append").save_as_table('HRMS.ETL.CUSTOMER')


