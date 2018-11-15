import win32com.client
import datetime
import os


outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
inbox = outlook.GetDefaultFolder(6)
root_folder = outlook.Folders.Item(1)
subfolder = root_folder.Folders['Inbox'].Folders['AIM Renos']
messages = subfolder.Items
message = messages.GetFirst()
subject = message.Subject

indir = "C:\\Users\\DmitryDmytrenko\\Documents\\AIM Renos\\All Attachments"

def getaimrenos():
    for m in messages:
        try:
            attachments = message.Attachments
            attachment1 = attachments.Item(1)
            attachment1.SaveASFile(indir + '\\' + str(attachment1))
            attachment2 = attachments.Item(2)
            attachment2.SaveASFile(indir + '\\' + str(attachment2))
            attachment3 = attachments.Item(3)
            attachment3.SaveASFile(indir + '\\' + str(attachment3))
            attachment4 = attachments.Item(4)
            attachment4.SaveASFile(indir + '\\' + str(attachment4))
            message = messages.GetNext()

        except:
            message = messages.GetNext()

getaimrenos()

