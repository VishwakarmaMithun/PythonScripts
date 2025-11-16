import snowflake
import snowflake.snowpark.functions 
import os
from snowflake.snowpark.functions import col
from snowflake.snowpark import Session
from snowflake.snowpark.types import StructType, StructField, IntegerType


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

session = Session.builder.configs(connection_parameters).create()
session.sql("use warehouse compute_wh").collect()

# Define schema with correct data type
schema = StructType([
    StructField('One', IntegerType(), nullable=True)
])

# Create DataFrame
test = session.create_dataframe([[1], [3]], schema=schema)

# Show results
test.show()

type(test)

testsql =session.sql("SELECT * FROM SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.CUSTOMER WHERE C_NATIONKEY='23'").select(col("C_NAME"))
testsql.show(2);

