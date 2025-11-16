import snowflake
import snowflake.snowpark.functions
from snowflake.snowpark.functions import col
from snowflake.snowpark import Session
from snowflake.snowpark.types import DataType,StringType,StructField,StructType,DateType,IntegerType
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
    "account":'oialxdd-xqb21073',#snowflake account (change yours)
    "role": snowflake_role,
    "warehouse":snowflake_warehouse,
    "database":snowflake_database,
    "schema":snowflake_schema
}


session = Session.builder.configs(connection_parameters).create();

schema = StructType([StructField('NAME',StringType()),StructField("SALARY",IntegerType()),StructField("C",DateType())])

df =  session.create_dataframe([["MITHUN",15000.0,"2024-05-01"]],schema=schema)

df.show()





0