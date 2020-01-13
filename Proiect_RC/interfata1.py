#!/usr/bin/python2
import Tkinter as tk
from client import *
import tkFileDialog
import os

class CC(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(bg='bisque')

        tk.Label(root,bg='bisque').grid(row=0,column=0)
        self.ip_addr = tk.Label(root, text="IP ADDRESS", bg='bisque')
        self. ip_addr.grid(row=1, column=0)
        self.ip_field = tk.Entry(root)
        self.ip_field.grid(row=1, column=1, ipadx="100")

        self.port = tk.Label(root, text="PORT", bg='bisque')
        self.port_field = tk.Entry(root)
        self.port.grid(row=2, column=0)
        self.port_field.grid(row=2, column=1, ipadx="100")

        self.file_to_send = tk.Label(root, text="FILE TO GET", bg='bisque')
        self.file_to_send.grid(row=3, column=0)
        self.name_field = tk.Entry(root)
        self.name_field.grid(row=3, column=1, ipadx="100")

        self.receive = tk.Button(root, text="REQUEST", fg="Black",
                      bg="salmon2", command=receive_data)
        self.receive.grid(row=4, column=1)
        self.choose = tk.Button(root, text="Choose File", fg="Black",
                                bg="salmon2", command=self.choose_func)
        self.choose.grid(row=5, column=1)
        self.show = tk.Button(root, text="Show status", fg="Black",
                              bg="salmon2", command=self.show_status)
        self.show.grid(row=6, column=1)

    # def apel(self):
    #     a=self.ip_field.get()
    #     a=a[:2] +'.'+a[2:4]+'.'+a[4:5]+'.'+a[5:]
    #     receive_data()
    def show_status(self):
        root1 = tk.Tk()
        sbar = tk.Scrollbar(root1)
        sbar.pack(side='right', fill='y')
        T = tk.Text(root1,yscrollcommand = sbar.set, height=40, width=60)
        T.pack(expand=True, fill='both')
        sbar.config(command=T.yview)

        fisier = open('log_client.txt', 'r')
        if fisier.mode == 'r':
            content = fisier.read()
            T.insert(tk.END, content)


    def choose_func(self):
        self.filename = tkFileDialog.askopenfilename(initialdir="C:\Users\\roxan\PycharmProjects\LELA-RCP",
                                                     title="Select A File",
                                                     filetype=(("txt files", "*.txt"), ("image files", ".png")))
        self.name_field.configure(text=self.filename)



if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.configure(bg='bisque')

    #Example(root).pack(fill="both", expand=True)
    app=CC(root)
    app.mainloop()