import pandas as pd
import psycopg2
import os
from pandas import ExcelWriter


cwd = os.getcwd()
connection = psycopg2.connect("dbname='visionkit_staging' user='visionkit' password='dsflk3497*#bgDS42390g' host='visionkit-staging.clidgkcrhpmh.us-west-2.rds.amazonaws.com' port='5432'")
query = open('fixture_instances.sql', 'r')

DF = pd.read_sql_query(query.read(), connection)

DF.to_csv(cwd+'\\FI.csv', index=False)
