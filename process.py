import psutil as pt


class Process():
    def __init__(self):
        self.cpu_count = pt.cpu_count(logical=False)
        self.cpu_count_logical = pt.cpu_count()


    def cpu_load_percent(self):
        return pt.cpu_percent(percpu=True)
    

    def ram_load_percent(self):
        return pt.virtual_memory()
    

