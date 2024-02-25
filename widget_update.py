

class Widget:
    def configurate_cpu_bar(self):

        r = self.cpu.cpu_load_percent()
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].configure(text=f'core {i+1} usage: {r[i]}%')
            self.list_progressbar[i].configure(value=r[i])


        r2 = self.cpu.ram_load_percent()
        self.ram_label.configure(text=f'RAM used: {r2[2]}%, {round(r2[3]/1048576)} Mb,\
                                 \n available: {round(r2[1]/1048576)} Mb')
        self.ram_bar.configure(value=r2[2])

        self.wheel = self.after(1000, self.configurate_cpu_bar)


    def configure_window(self):
        if self.wm_overrideredirect():
            self.overrideredirect(False)
        else:
            self.overrideredirect(True)
        self.update()


    def clear_window(self):
        for i in self.winfo_children():
            i.destroy()


    def configure_minimal_window(self):
        self.cpu_min.configure(value=self.cpu.cpu_total_load())
        self.ram_min.configure(value=self.cpu.ram_load_percent()[2])
        self.frame1.configure(text=f'CPU {self.cpu.cpu_total_load()} %')
        self.frame2.configure(text=f'RAM available:{round(self.cpu.ram_load_percent()[1]/1048576)} Mb\
                              \nUsed: {self.cpu.ram_load_percent()[2]} %')
        self.wheel = self.after(1000, self.configure_minimal_window)