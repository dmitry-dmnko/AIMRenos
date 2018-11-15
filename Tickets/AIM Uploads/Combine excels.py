import os
import glob
import pandas as pd


indir="C:\\Users\\DmitryDmytrenko\\Documents\\Technology\\DD\\Tickets\\AIM Uploads\\Nov\\10.23.18"
os.chdir(indir)
filelist = glob.glob("*QA_completed.xlsx")
print(filelist)

# read them in
excels = [pd.ExcelFile(name) for name in filelist]
print(excels)
# turn them into dataframes
frames = [x.parse(x.sheet_names[0], header=None, index_col=None) for x in excels]

# delete the first row for all frames except the first
# i.e. remove the header row -- assumes it's the first
frames[1:] = [df[1:] for df in frames[1:]]

# concatenate them..
combined = pd.concat(frames)

# write it out
combined.to_excel("c.xlsx", header=False, index=False)