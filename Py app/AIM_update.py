import os
import psycopg2

indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos\\All Attachments\\2018-11-07"


def aim_update():
    os.chdir(indir)
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    with open(indir+'\\CSV_uploads\\concatenated.csv', 'r') as f:
        next(f)  # Skip the header row.
        cur.copy_from(f, 'aim_update', sep=',')
    conn.commit()

