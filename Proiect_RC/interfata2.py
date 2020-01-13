#!/usr/bin/python2
import Tkinter as tk
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

from server import *

plt.rcParams['figure.figsize']=(12,6)
fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.tick_params(axis='x', which='major', labelsize=5)

class SS(tk.Frame):
    def __init__(self, root):
        tk.Frame.__init__(self, root)
        self.configure(bg='bisque')
        tk.Label(root,bg='bisque').grid(row=0,column=0)

        self.ip_addr = tk.Label(root, text="IP ADDRESS", bg='bisque')
        self.ip_addr.grid(row=1, column=0)
        self.ip_field = tk.Entry(root)
        self.ip_field.grid(row=1, column=1, ipadx="100")

        self.port = tk.Label(root, text="PORT", bg='bisque')
        self.port.grid(row=2, column=0)
        self.port_field = tk.Entry(root)
        self.port_field.grid(row=2, column=1, ipadx="100")

        self.send = tk.Button(root, text="SEND", fg="Black",
                              bg="salmon2", command=send_data)
        self.send.grid(row=3, column=1)
        self.show = tk.Button(root, text="Show status", fg="Black",
                                bg="salmon2", command=self.show_status)
        self.show.grid(row=4, column=1)
        self.showg = tk.Button(root, text="Show Congestion Graphic", fg="Black",
                              bg="salmon2", command=self.grafic)
        self.showg.grid(row=5, column=1)


    def grafic(self):
        style.use('fivethirtyeight')

        #fig = plt.figure()
        #self.ax1 = fig.add_subplot(111)

        self.ani = animation.FuncAnimation(fig, self.animate, interval=1000)

        plt.show()
    def animate(self,i):
        graph_data = open('text.txt', 'r').read()
        lines = graph_data.split('\n')
        xs = []
        ys = []

        for line in lines:
            if len(line) > 1:
                x, y = line.split(',')
                xs.append(x)
                ys.append(float(y))


        ax1.clear()
        ax1.plot(xs, ys,linewidth=2)

    def show_status(self):
        root1 = tk.Tk()
        sbar = tk.Scrollbar(root1)
        sbar.pack(side='right', fill='y')
        T = tk.Text(root1, yscrollcommand=sbar.set, height=40, width=60)
        T.pack(expand=True, fill='both')
        sbar.config(command=T.yview)

        fisier = open('log_server.txt', 'r')
        if fisier.mode == 'r':
            content = fisier.read()
            T.insert(tk.END, content)

    # def apel(self):
    #     a = self.ip_field.get()
    #     a = a[:2] + '.' + a[2:4] + '.' + a[4:5] + '.' + a[5:]
    #     send_data()


if __name__ == "__main__":
    root = tk.Tk()
    root.geometry('500x300')
    root.configure(bg='bisque')
    #Example(root).pack(fill="both", expand=True)
    app=SS(root)
    app.mainloop()