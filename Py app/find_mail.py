import win32com.client
import datetime
import os
from datetime import timedelta


outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
root_folder = outlook.Folders.Item(1)
subfolder = root_folder.Folders['Inbox'].Folders['AIM Renos']
messages = subfolder.Items
message = messages.GetFirst()
subject = message.Subject

indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos\\All Attachments"
yestr = datetime.date.today()-timedelta(5)
print(yestr)
for m in messages:

    if message.SentOn.date() > yestr:
        print(message)
        print(message.SentOn.date())
        attachments = message.Attachments
        num_attach = len([x for x in attachments])
        for x in range(1, num_attach+1):
            attachment = attachments.Item(x)
            if str(attachment)[-4:] == 'xlsm':
                attachment.SaveASFile(indir + '\\order_sheets\\' + str(attachments.Item(x)))
            else:
                attachment.SaveASFile(indir + '\\other files\\' + str(attachments.Item(x)))
        message = messages.GetNext()

