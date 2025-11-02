import os
import snowflake.snowpark.functions
from snowflake.snowpark import Session
from snowflake.snowpark.functions import col

# Build connection parameters
snowflake_password = os.getenv("snowflake_password")
snowflake_user = os.getenv("snowflake_user")
snowflake_account= os.getenv("snowflake_account")
snowflake_role = os.getenv("snowflake_role")
snowflake_warehouse= os.getenv("snowflake_warehouse")
snowflake_database= os.getenv("snowflake_database")
snowflake_schema= os.getenv("snowflake_schema")

# Build connection parameters
connection_parameters = {
    "user": snowflake_user,
    "password": snowflake_password,
    "account":snowflake_account,
    "role": snowflake_role,
    "warehouse":snowflake_warehouse,
    "database":snowflake_database,
    "schema":snowflake_schema
}

session = Session.builder.configs(connection_parameters).create();
session.sql("USE WAREHOUSE COMPUTE_WH").collect();

df_customer_info = session.table("SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.CUSTOMER")
df_customer_filter = df_customer_info.filter(col("C_MKTSEGMENT")=='HOUSEHOLD')
df_customer_select = df_customer_info.select(col("C_NAME"),col("C_ADDRESS"))
df_customer_select.show()
print(df_customer_select.count())
df_customer_select.describe().sort("SUMMARY").show()
