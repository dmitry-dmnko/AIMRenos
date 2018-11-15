import glob
import os
import psycopg2
import xlrd
from AIM_update import aim_update


indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos\\All Attachments\\2018-11-09_all_emails"
os.chdir(indir)
excelm_files = glob.glob("*.xlsm")
print(excelm_files)


def insert():
    conn = psycopg2.connect("dbname='EnvUsa' user='postgres' password='DmEe990046' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("INSERT INTO tracker VALUES(%s,%s,%s, %s, %s)", (fcid
                                                                 ,initial_date
                                                                 ,final_date
                                                                 ,delivery_date
                                                                 ,instalation_date))
    conn.commit()
    conn.close()


for item in excelm_files:
    def initial():
        if item.split(' ')[1] == 'INITIAL':
            return item.split(' ')[2]

    def final():
        if item.split(' ')[1] == 'FINAL':
            return item.split(' ')[2]

    print(item)
    wb = xlrd.open_workbook(item)
    ws = wb.sheet_by_name('Order')
    fcid = int(item.split(' ')[0])
    initial_date = initial()
    final_date = final()
    delivery_date = xlrd.xldate.xldate_as_datetime(ws.cell(3, 3).value, wb.datemode).date()
    instalation_date = xlrd.xldate.xldate_as_datetime(ws.cell(4, 3).value, wb.datemode).date()
    insert()


# aim_update()