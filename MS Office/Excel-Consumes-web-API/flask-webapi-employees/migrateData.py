import pandas as pd
from sqlalchemy import create_engine
import sqlalchemy
import os

engine = create_engine('mysql+pymysql://root:w123456@localhost/stonetest?charset=utf8')
target_engine = create_engine(os.environ.get('MSSQL_URI'))

df = pd.read_sql('emp_master', engine)
df.to_sql('emp_master', target_engine, index=False, if_exists='append')