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
df_orders_info =  session.table('SNOWFLAKE_SAMPLE_DATA.TPCH_SF1000.ORDERS')
 
record_count = df_orders_info.count()

print(record_count)

df_orders_select =  df_orders_info.select(col("O_ORDERKEY"),col("O_ORDERSTATUS"),col("O_TOTALPRICE"))

df_orders_select.show(15)


# Try to get high level stat information about dataframe, df_orders_select
df_orders_select.describe().sort("SUMMARY").show()