import snowflake
from snowflake.snowpark import functions
from snowflake.snowpark.functions import col
from snowflake.snowpark import Session
import os
from snowflake.snowpark.types import DataType,StructType,IntegerType,StructField


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
    "database":'HRMS',
    "schema":'ETL'
}


session =    Session.builder.configs(connection_parameters).create();

employee_json = session.read.json('@my_s3_stage_json')
employee_json.write.mode("append").save_as_table("HRMS.ETL.JSON_WRITE")

employee_json =  employee_json.select(col("$1").as_("book"))
employee_json.columns
employee_json.show()
employee_json=employee_json.select_expr("$BOOK:address","$BOOK:birthdate","$BOOK:city")
employee_json.show()
employee_json.write.mode("overwrite").save_as_table("HRMS.ETL.JSON_WRITE_EMPLOYEE")