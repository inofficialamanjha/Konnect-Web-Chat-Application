import socket
from _compression import BUFFER_SIZE
from tkinter import messagebox
from threading import Thread
from os import path
from time import sleep
from random import uniform
from tkinter import*
from time import sleep

##SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096

def connect():              ##connects to server
    ##SEPARATOR = "<SEPARATOR>"
    host = "192.168.1.4"
    port = 33000
    global s
    s = socket.socket()
    s.connect((host, port))
    messagebox.showinfo("connected", "")
    msg_list.insert(END, "Welcome to CN project Application")
    receive_thread = Thread(target=receive)
    receive_thread.start()
    
def receive(): ##recive bytes
    while True:
        try:
            msg = s.recv(1024).decode("utf8")
            msg_list.insert(END,"Server: "+ msg) ##msg list is tkinter list
        except OSError:
            break
          
def send():
    display_mess = my_msg.get()
    mess = bytes(display_mess, "utf-8")
    s.send(mess)
    msg_list.insert(END, "You: " + display_mess)
          
    if display_mess == "{quit}":
        s.close()
        root.quit()
          
def on_closing(event=None):
    my_msg.set("{quit}")
    send()
          
root=Tk()
root.title("Client")
root.geometry('400x360')
messages_frame = Frame(root,padx=10,pady=10)
my_msg = StringVar() # For the messages to be sent.
my_msg.set("Type your messages here.")

scrollbar = Scrollbar(messages_frame)

msg_list = Listbox(messages_frame, height=15, width=70,yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
msg_list.pack(side=LEFT, fill=BOTH)
msg_list.pack()
messages_frame.pack()

entry_field = Entry(root, textvariable=my_msg)
entry_field.bind("<Return>", send)
entry_field.pack()

send_button = Button(root, text="Send", command=send) ##uses the send function
send_button.pack()

mybutton=Button(root,text="Connect",command=connect)
mybutton.pack(side='bottom')

button4=Button(root,text="Exit",command=on_closing) ##the exit coomand
button4.pack(side='bottom')

root.protocol("WM_DELETE_WINDOW", on_closing) ##send {quit}
root.mainloop()