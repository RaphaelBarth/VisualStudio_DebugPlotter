from queue import Queue
from dataCollector import DataCollector
from plot import Plotter


FILE_PATH ="path to logfile"
PARAMETERS =[
   "my_parameter",
   "u8_example",
   "..."]

PLOT_HOWMANY = 100
INTERVAL = 0.01

    
def main():
    try:
        queue = Queue()
        dataCollector = DataCollector()
        dataCollector.set_logfilepath(filepath=FILE_PATH)
        dataCollector.collect(queue=queue, wait=INTERVAL)
        plotter = Plotter()
        plotter.setup_plotting(parameters=PARAMETERS,howmany=PLOT_HOWMANY)
        plotter.start_plotting(interval=INTERVAL,data=queue)
        #test = lambda q: [print(q.get()) for _ in iter(int, 1)]
        #test(queue)
    finally:
        dataCollector.stop()

    

if __name__ == "__main__":
    main()


