import os
import sys
import win32com.client
import glob

indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos"
out = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos"

os.chdir(indir)
excel_names = glob.glob("*.xlsm")


def unprotect_xlsx(filename):
    xcl = win32com.client.Dispatch('Excel.Application')
    pw_str = 'envusa'
    wb = xcl.workbooks.open(indir + '\\' + filename)
    wb.Unprotect(pw_str)
    wb.UnprotectSharing(pw_str)
    xcl.DisplayAlerts = False
    wb.Save()
    xcl.Quit()


for filename in excel_names:
    print(filename)
    unprotect_xlsx(filename)
