from tkinter import *
from tkinter import ttk
from tkinter import filedialog

import socket                   # Import socket module

port = 50000                    # Reserve a port for your service every new transfer wants a new port or you must wait.
s = socket.socket()             # Create a socket object
host = ""   # local machine name
s.bind((host, port))            # Bind to the port
s.listen(5)                     # Now wait for client connection.

print ('Server listening....')

class Root(Tk):
    def __init__(self):
        super(Root, self).__init__()
        self.title("TCP File Transfer")
        self.minsize(400, 200)
        self.labelFrame = ttk.LabelFrame(self, text="Open File")
        self.labelFrame.grid(column=0, row=1, padx=20, pady=20)
        self.button()


    def button(self):
        self.button = ttk.Button(self.labelFrame, text="Browse A File", command=self.fileDialog)
        self.button.grid(column=1, row=1)

        button2 = ttk.Button( text="Send!",command=self.Trimitere)
        button2.grid(column=2, row=3)


    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype=(("txt files", "*.txt"), ("all files", "*.*")))
        self.label = ttk.Label(self.labelFrame, text="")
        self.label.grid(column=1, row=2)
        self.label.configure(text=self.filename)
    def Trimitere(self):
        print(self.filename)
        while True:
            conn, addr = s.accept()  # Establish connection with client.
            print('Got connection from', addr)
            data = conn.recv(1024)
            print('Server received', repr(data))

            file = self.filename
            f = open(file, 'rb')
            l = f.read(1024)
            while (l):
                conn.send(l)
                print('Sent ', repr(l))
                l = f.read(1024)
            f.close()

            print('Done sending')
            #conn.send('\nCe faci, Condrea? Multam de conectare! :*')
            conn.close()
root = Root()
root.mainloop()