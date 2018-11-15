import pandas as pd
import glob
import os
import time


indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos"
os.chdir(indir)
excelm_files = glob.glob("*.xlsm")

print(excelm_files)


def create_csv():
    for filename in excelm_files:
        pd.read_excel(indir+'\\'+filename, sheet_name='AIM Upload').to_csv(os.path.splitext(filename)[0]+'.csv', index=False)
        print(filename)


while True:
    try:
        create_csv()
        time.sleep(60)
    except KeyboardInterrupt:
        print('Manual break by user')