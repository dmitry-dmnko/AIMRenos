import pandas as pd
import glob
import os
import time
import shutil

indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos\\All Attachments\\2018-11-07"
os.mkdir(indir + "\\CSV_uploads")
csv_indir = indir + '\\CSV_uploads'
outfile = csv_indir + "\\concatenated.csv"
os.chdir(indir)
excelm_files = glob.glob("*.xlsm")
fullpath = os.path.join
print(excelm_files)


def create_csv():
    os.chdir(indir)
    for filename in excelm_files:
        pd.read_excel(indir+'\\'+filename, sheet_name='AIM Upload').to_csv(os.path.splitext(filename)[0]+'.csv',
                      index=False)
        print('CSV Extracted from ' + filename)


def move_csv():
    os.chdir(indir)
    csv_files = glob.glob("*.csv")
    for filename in csv_files:
        shutil.move(filename, csv_indir)


def concatenate():
    os.chdir(csv_indir)
    filelist = glob.glob("*.csv")
    dflist=[]
    colnames=['FCID', 'FCID Name', 'Marketing Sales Designation', 'Language Designation', 'Fixture Type Code',
              'Fixture Type Name', 'Zone', 'Subzone', 'Fixture Instance Priority', 'Within 10 Feet']
    for filename in filelist:
        print(filename)
        df = pd.read_csv(filename, sep=',')
        dflist.append(df)
    concatdf = pd.concat(dflist, axis=0)
    concatdf.columns = colnames
    concatdf.to_csv(outfile, index=None)


create_csv()
move_csv()
concatenate()
