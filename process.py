import psutil as pt


class Process():
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()


    def cpu_load_percent(self):
        return pt.cpu_percent(percpu=True)
    

    def ram_load_percent(self):
        return pt.virtual_memory()
    
    def cpu_total_load(self):
        return pt.cpu_percent()
    
    def get_cpu_frequency_max(self):
        return pt.cpu_freq(percpu=False)
    

# x = Process()
# for i in range(1,100):
#     print(x.cpu_frequency_total())
