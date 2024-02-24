

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