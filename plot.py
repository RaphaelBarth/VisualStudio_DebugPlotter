
from queue import Empty
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataSet import DataSet


class Plotter:

   _fig = None
   _intern_data = dict()

   def setup_plotting(self,parameters,howmany):
      self.fig, axis = plt.subplots(len(parameters), 1, figsize=(8, 6))

      for name, ax in zip(parameters, axis):
         dataset = DataSet(howmany)
         ax.set_title(name)
         #ax.set_xlabel('X-axis')
         #ax.set_ylabel('Y-axis')
         line, = ax.plot(dataset.X(),dataset.Y(),marker='o')
         self._intern_data[name]=(dataset,ax,line)


   

   def start_plotting(self,interval,data):
      ani = animation.FuncAnimation(self.fig, self._animate,fargs=(data,), interval=interval*1000, blit=True)  # Update the plot every 1 second (1000 ms)
      plt.show()



   def _animate(self,frame,extern_data):
      lines = (x[1] for x in self._intern_data.values())

      try: 
         new_data = extern_data.get_nowait()
      except Empty:
         return lines
      
      for key,value in new_data.items() :
         ele = self._intern_data.get(key)
         if not ele:
            continue
         dataset = ele[0]
         axis = ele[1]
         line = ele[2]

         x = dataset.total_elements()+1
         y = value
         dataset.append(x,y)

   
      for ele in self._intern_data.values():
         dataset = ele[0]
         axis = ele[1]
         line = ele[2]
         line.set_data(dataset.X(), dataset.Y())
         axis.relim()
         axis.autoscale_view()
      return lines

