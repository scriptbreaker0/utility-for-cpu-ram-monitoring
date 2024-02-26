import tkinter as tk
from tkinter import ttk
import sys
from process import Process
from widget_update import Widget

class App(tk.Tk, Widget):

    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)
        self.overrideredirect(True)
        self.resizable(False, False)
        self.title('CPU-RAM')

        self.cpu = Process()
        self.run_set_ui()

    def run_set_ui(self):
        self.set_ui()
        self.Cpu_usage_bar()
        self.configurate_cpu_bar()

    def set_ui(self):
        exit_button = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_button.pack(fill=tk.X)

        self.frame1 = ttk.LabelFrame(self, text='Manual')
        self.frame1.pack(fill=tk.X)

        self.combobox = ttk.Combobox(self.frame1, values=['hiden', 'full', 'minimum'],width=10, state='readonly')
        self.combobox.current(1)
        self.combobox.pack(side=tk.LEFT)


        ttk.Button(self.frame1, text='move', command=self.configure_window).pack(side=tk.LEFT)
        #ttk.Button(self.frame1, text='Empty').pack(side=tk.LEFT)
        #in developing....

        self.frame2 = ttk.LabelFrame(self, text='Power')
        self.frame2.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)
        self.combobox.bind('<<ComboboxSelected>>', self.choise_combo)

    def Cpu_usage_bar(self):
        ttk.Label(self.frame2, text=f'Physical cores: {self.cpu.cpu_count}, logical cores: {self.cpu.cpu_count_logical}\
                  \nMax frequency: {self.cpu.get_cpu_frequency_max()[2]} GHz',
                    anchor=tk.CENTER).pack(fill=tk.X)
        
        self.list_label = []
        self.list_progressbar = []

        for i in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.frame2, anchor=tk.CENTER))
            self.list_progressbar.append(ttk.Progressbar(self.frame2, length=100))
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_progressbar[i].pack(fill=tk.X)


        self.ram_label = ttk.Label(self.frame2, text='', anchor=tk.CENTER)
        self.ram_label.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.frame2, length=100)
        self.ram_bar.pack(fill=tk.X)

    def create_full_window(self):
        self.after_cancel(self.wheel)
        self.clear_window()
        self.update()
        self.run_set_ui()
        self.enter_mouse('')
        self.combobox.current(1)

    def create_minimal_mod(self):

        self.frame1 = ttk.LabelFrame(self, text='CPU')
        self.frame1.pack(fill=tk.X)

        self.frame2 = ttk.LabelFrame(self, text='RAM')
        self.frame2.pack(fill=tk.X)


        self.cpu_min = ttk.Progressbar(self.frame1, length=100)
        self.cpu_min.pack(side=tk.LEFT)

        self.ram_min = ttk.Progressbar(self.frame2, length=100)
        self.ram_min.pack(side=tk.LEFT)



        ttk.Button(self, text='full',command=self.create_full_window, width=5).pack(side=tk.RIGHT)

        ttk.Button(self, text='move',command=self.configure_window, width=5).pack(side=tk.RIGHT)

        self.update()
        self.configure_minimal_window()

    def enter_mouse(self, event):
        if self.combobox.current() == 0 or 1:
            self.geometry('')


    def leave_mouse(self, event):
        if self.combobox.current() == 0:
            self.geometry(f'{self.winfo_width()}x1')


    def choise_combo(self, event):
        if self.combobox.current() == 2:
            self.enter_mouse('')
            self.unbind_class('Tk','<Enter>')
            self.unbind_class('Tk','<Leave>')
            self.combobox.unbind('<<ComboboxSelected>>')
            self.after_cancel(self.wheel)
            self.clear_window()
            self.update()
            self.create_minimal_mod()


    
    def app_exit(self):
        self.destroy()
        sys.exit()

if __name__ == '__main__':
    root = App()
    root.mainloop()