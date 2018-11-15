import os
import glob
import pandas


def concatenate(indir = "C:\\Users\\DmitryDmytrenko\\Documents\\Technology\\DD\\Tickets\\AIM Uploads\\Nov\\Nov 13",
                outfile = "C:\\Users\\DmitryDmytrenko\\Documents\\Technology\\DD\\Tickets\\AIM Uploads\\Nov\\Nov 13\\Concatenated.csv"):
    os.chdir(indir)
    filelist = glob.glob("*.csv")
    dflist=[]
    colnames=["FCID", "FCID Name", "Marketing Sales Designation", "Language Designation", "Fixture Type Code",
              "Fixture Type Name", "Zone", "Subzone", "Fixture Instance Priority",
              "Within 10 Feet"]
    for filename in filelist:
        print(filename)
        df = pandas.read_csv(filename, sep=',')
        dflist.append(df)
    concatdf = pandas.concat(dflist, axis=0)
    concatdf.columns = colnames
    concatdf.to_csv(outfile, index=None)


concatenate()

