#  Making simple terminal app to add attendance
from pyrogram import Client,filters
from pyrogram.methods import messages
import os

app = Client("Marco",api_id=1684890,api_hash="4b24d4045a3dca817ca317df9c9dedb2",bot_token="1763143853:AAEv7KcY9GeltYkEQG3gDqgsAhogd62sVrw")

admin = ['917099183']


# Start Command
@app.on_message(filters.command(["start"]))
def msg(client, message):
    print(message)
    msgm = "Hey User i'm Online"
    app.send_message(chat_id=message['from_user']['id'],text=msgm)

# Get all apps running but need to put app name
@app.on_message(filters.command(["tasklist"]))
def taskmngr(client, message):
    if str(message['from_user']['id']) in  admin:
        msgstring = ""
        for msgs in message['command']:
            msgstring = msgstring + msgs + " "
        print(msgstring)
        msgm = msgstring.replace(message['command'][0],"")
        execution = os.popen('tasklist /v /fi "IMAGENAME eq '+msgm+'"').read()
        print(execution)
        app.send_message(chat_id=message['from_user']['id'],text=execution)
    else:
        app.send_message(chat_id=message['from_user']['id'],text="You are not only of my admin")

# Close or stop a task in Windows 10 as I have tested
@app.on_message(filters.command(["taskkill"]))
def taskkiller(client, message):
    if str(message['from_user']['id']) in  admin:
        msgstring = ""
        for msgs in message['command']:
            msgstring = msgstring + msgs + " "
        print(msgstring)
        msgm = msgstring.replace(message['command'][0],"")
        execution = os.popen('taskkill /f /im '+msgm+'').read()
        print(execution)
        app.send_message(chat_id=message['from_user']['id'],text="<code>"+execution+"</code>")
    else:
        app.send_message(chat_id=message['from_user']['id'],text="You are not only of my admin")

# Make sure it's in environment variable, works with /newtask code to open VS Code (If You have one)
@app.on_message(filters.command(["newtask"]))
def newtaskhere(client, message):
    if str(message['from_user']['id']) in  admin:
        msgstring = ""
        for msgs in message['command']:
            msgstring = msgstring + msgs + " "
        msgm = msgstring.replace(message['command'][0],"")
        print(msgm)
        execution = os.popen(msgm).read()
        print(execution)
        if execution == "":
            execution = "Code Running Successfully"
        else:
            pass
        app.send_message(chat_id=message['from_user']['id'],text="<code>"+execution+"</code>")
    else:
        app.send_message(chat_id=message['from_user']['id'],text="You are not only of my admin")

#  To get a list of admins
@app.on_message(filters.command(["admins"]))
def terminalapp(client, message):
    if str(message['from_user']['id']) in  admin:
        list_admins = ""
        for ad in admin:
            list_admins = list_admins + str(ad) + "\n"
        app.send_message(chat_id=message['from_user']['id'],text="<code>"+list_admins+"</code>")
    else:
        app.send_message(chat_id=message['from_user']['id'],text="You are not only of my admin")


app.run()