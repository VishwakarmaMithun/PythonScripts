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
    "database":snowflake_database,
    "schema":snowflake_schema
}

session  = Session.builder.configs(connection_parameters).create()

df  = session.create_dataframe([[1],[2],[3],[4]],schema=["A"])
df.show()

df = session.create_dataframe([[1,2,3,4],[4,5,6,7]],schema=["A","B","C","D"])
df.show()

df = session.create_dataframe([[1,2],[None,3]],schema=["A","B"])
df.show()