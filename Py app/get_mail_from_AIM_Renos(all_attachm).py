import win32com.client
import datetime
import os
from datetime import timedelta

outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
root_folder = outlook.Folders.Item(1)
subfolder = root_folder.Folders['Inbox'].Folders['AIM Renos']
messages = subfolder.Items

indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos\\All Attachments"
yestr = datetime.date.today()-timedelta(1)
friday = datetime.date.today()-timedelta(3)
today = datetime.date.today()



def get_yestr_mail():
    print(yestr)
    try:
        os.mkdir(indir + "\\" + str(yestr))
    except OSError:
        print("Creation of the directory %s failed" % str(yestr))
    else:
        print("Successfully created the directory %s " % str(yestr))
    for m in messages:
        if m.SentOn.date() == yestr:
            print(m)
            print(m.SentOn.date())
            attachments = m.Attachments
            num_attach = len([x for x in attachments])
            for x in range(1, num_attach + 1):
                attachment = attachments.Item(x)
                if str(attachment)[-4:] == 'xlsm':
                    attachment.SaveASFile(indir + '\\' + str(yestr) + '\\' + str(attachments.Item(x)))
                else:
                    attachment.SaveASFile(indir + '\\other files\\' + str(attachments.Item(x)))
            message = messages.GetNext()


def get_fr_mail():
    print(friday)
    try:
        os.mkdir(indir + "\\" + str(friday))
    except OSError:
        print("Creation of the directory %s failed" % str(friday))
    else:
        print("Successfully created the directory %s " % str(friday))
    for m in messages:
        if m.SentOn.date() == friday:
            print(m)
            print(m.SentOn.date())
            attachments = m.Attachments
            num_attach = len([x for x in attachments])
            for x in range(1, num_attach + 1):
                attachment = attachments.Item(x)
                if str(attachment)[-4:] == 'xlsm':
                    attachment.SaveASFile(indir + '\\' + str(friday) + '\\' + str(attachments.Item(x)))
                else:
                    attachment.SaveASFile(indir + '\\other files\\' + str(attachments.Item(x)))
            message = messages.GetNext()


def get_tod_mail():
    print(today)
    try:
        os.mkdir(indir + "\\" + str(today))
    except OSError:
        print("Creation of the directory %s failed" % str(today))
    else:
        print("Successfully created the directory %s " % str(today))
    for m in messages:
        if m.SentOn.date() == today:
            print(m)
            print(m.SentOn.date())
            attachments = m.Attachments
            num_attach = len([x for x in attachments])
            for x in range(1, num_attach + 1):
                attachment = attachments.Item(x)
                if str(attachment)[-4:] == 'xlsm':
                    attachment.SaveASFile(indir + '\\' + str(today) + '\\' + str(attachments.Item(x)))
                else:
                    attachment.SaveASFile(indir + '\\other files\\' + str(attachments.Item(x)))
            message = messages.GetNext()

def get_all_mail():
    print(today)
    try:
        os.mkdir(indir + "\\" + str(today) + "_all_emails")
    except OSError:
        print("Creation of the directory %s failed" % str(today))
    else:
        print("Successfully created the directory %s " % str(today))
    for m in messages:
        print(m)
        print(m.SentOn.date())
        attachments = m.Attachments
        num_attach = len([x for x in attachments])
        for x in range(1, num_attach + 1):
            attachment = attachments.Item(x)
            if str(attachment)[-4:] == 'xlsm':
                attachment.SaveASFile(indir + '\\' + str(today) + '_all_emails\\' + str(attachments.Item(x)))
            else:
                attachment.SaveASFile(indir + '\\other files\\' + str(attachments.Item(x)))
        message = messages.GetNext()

get_all_mail()

get_yestr_mail()
