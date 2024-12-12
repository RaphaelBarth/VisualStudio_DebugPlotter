# VS_DebugPlotter
Python script for graphical plotting of VS debug messages

### 0. create Debug Messages:
Insert breakpoints where you want to analyze your code. Adjust your breakpoints via settings, then Select the options *Actions* and *Continue code execution*. 
This type of breakpoint is also known as the feature tracepoint.
In the message, use the following style to indicate the key and value pair of your parameter

```
parameter={parameter}
```
Be aware that printing debugs in this manner can significantly reduce the performance of the executed program, so use breakpoints/tracepoints carefully.

### 1. redirect Visual Studio Output Window to file:

1. Change Settings:

    Tools -> Options -> Debugging -> General -> Redirect all Output Window text to the Immediate Window

2. Open Immediate Window:

    Ctrl + Alt + I or Debug -> Windows -> Immediate Window

3. Change Destination:

    ```
    >Tools.LogCommandWindowOutput /on C:\temp\temp.log
    ```

4. Stop file Logging:

    ```
    >Tools.LogCommandWindowOutput /off
    ```

### 2. plotting via Python Script

1. Update the file path in the main.py file.
2. Configure the number of values displayed in a plot and the update frequency.
3. Set the parameter names that you wish to plot, ensuring that they are named the same as in your key-value pairs.
4. Launch the script by running main.py.


Note that there is no temporal connection between the different plots. To solve this, you need to place your debugs correctly and smartly in the code.
