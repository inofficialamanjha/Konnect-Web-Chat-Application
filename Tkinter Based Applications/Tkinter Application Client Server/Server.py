import socket
from threading import Thread
from tkinter import messagebox
from threading import Thread
from os import path
from time import sleep
from random import uniform
from tkinter import*

SEPARATOR = "<SEPARATOR>"
BUFFER_SIZE = 4096


def connect():                                    ##connects to client
    SERVER_HOST = "192.168.1.4"
    SERVER_PORT = 33000
    ##SEPARATOR = "<SEPARATOR>"
    s = socket.socket()
    s.bind((SERVER_HOST, SERVER_PORT))
    s.listen(5)
    global client_socket
    client_socket, address = s.accept()
    messagebox.showinfo(f"{address}" + "is connected")
    msg_list.insert(END, "Welcome to the CN Project Application!")
    receive_thread = Thread(target=receive)
    receive_thread.start()

    
def receive(): ##recieve bytes
    while True:
        try:
            msg = client_socket.recv(1024).decode("utf8")##client_socket is client socket object
            msg_list.insert(END,"Client: "+ msg) #message list is tkinter lise
        except OSError:
            break
            
def send():
    display_mess = my_msg.get()
    mess = bytes(display_mess, "utf-8")
    client_socket.send(mess) 
    msg_list.insert(END, "You: "+display_mess)
    
    if display_mess == "{quit}":
        client_socket.close()
        root.quit()
    
    
def on_closing(event=None):
    my_msg.set("{quit}")
    send()

root=Tk()
root.title("Server")
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
send_button.grid(row=0,column=0,padx=5,pady=5)

mybutton=Button(root,text="Connect",command=connect)
mybutton.grid(row=0,column=1,padx=5,pady=5)

button4=Button(root,text="Exit",command=on_closing) ##the exit command
button4.pack(row=0,column=3,padx=5,pady=5)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()