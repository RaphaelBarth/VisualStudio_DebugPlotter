from threading import Thread, Event
import time
import re


class DataCollector():
    _thread =Thread()
    _thread_stop = Event()

    PATH = ""

    def set_logfilepath(self,filepath):
        '''
        Set the path of the logfile 
        '''
        self.PATH = filepath
    

    def collect(self,queue,wait):
        ''''''
        self._thread_stop.clear()
        self._thread = Thread(target=self._run_DataCollector, args=(queue,0.001))
        self._thread.start()


    def stop(self):
        ''''''
        self._thread_stop.set()
        self._thread.join()


    def _run_DataCollector(self,queue,wait):
        '''
        '''
        #print('_run_DataCollector')
        if not self.PATH:
            raise Exception("not path to logfilepath is set")
        file_pos = 0
        while not self._thread_stop.is_set():  
            with open(self.PATH, 'r',encoding="utf-16") as log_file:
                log_file.seek(file_pos)
                for line in log_file:
                    data = self._transform_line(line)
                    if data:
                        queue.put(data)
                
                file_pos=log_file.tell()
                time.sleep(wait)


    def _transform_line(self,line):
        '''
        Extracting funktion name and key-value pairs using regular expressions.
        Store the in a dictonary
        '''
        try:
            #print(f"{line=}\n")
            #function_name = re.match(r"([a-zA-Z0-9_]+):", line).group(1)
            parameter_value_pairs = re.findall(r"(\b\w+)\s*=\s*(\d+)", line)
            result = {}
            for pair in parameter_value_pairs:
                parameter,value = pair
                #parameter = function_name+"-"+parameter
                result[parameter] = int(value)
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


        



