import tkinter as tk
from tkinter import ttk
import sys

class App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 0.5)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title('CPU-RAM')

        self.set_ui()

    def set_ui(self):
        exit_button = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_button.pack(fill=tk.X)

        self.frame2 = ttk.LabelFrame(self, text='Manual')
        self.frame2.pack(fill=tk.X)

        self.combobox = ttk.Combobox(self.frame2, values=['hiden', 'full', 'minimum'],width=10, state='readonly')
        self.combobox.current(1)
        self.combobox.pack(side=tk.LEFT)


        ttk.Button(self.frame2, text='move').pack(side=tk.LEFT)
        ttk.Button(self.frame2, text='>>>').pack(side=tk.LEFT)

        self.frame2 = ttk.LabelFrame(self, text='Power')
        self.frame2.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)


    def enter_mouse(self, event):
        if self.combobox.current() == 0 or 1:
            self.geometry('')


    def leave_mouse(self, event):
        if self.combobox.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')
    def app_exit(self):
        self.destroy()
        sys.exit()
root = App()
root.mainloop()