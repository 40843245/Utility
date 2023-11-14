"""
Purpose:
    The purpose of this code is: 
        1. try to get the coroutine of main() ,then 
        2. do the following task and print the task and its result (if it is not cancelled.).
            2.1. try to get task of 0th of process whose process name is 'msedge.exe'. See the following statements: 
                processName = 'msedge.exe'
                procs = OSProcessHandler.Psutil.GetProcesses(processName)
                handler1 = loop.create_task(set_after(fut, 2, get_pid(procs[0]) ) )
            Here, the task is scheduled to perform after 2 seconds. See the following statement: 
                handler1 = loop.create_task(set_after(fut, 2, get_pid(procs[0]) ) 
            While, the task is cancelled after 3 seconds (if it is not executed). See the following statements: 
                thread1 = threading.Timer(3,cancel_task,[handler1],None)
                thread1.start()
            
Additional references:
    1. For HOW to use these modules (such as psutil, asyncio, threading etc),see my notes on repo on GitHub. (NOT written yet, ready to write)
    2. For HOW to get the current running loop and create the loop in different environment (such as IDE or Python interpreter), 
        see the Jean Monet's reply on the stackoverflow (which I also place it on the following code).
        https://stackoverflow.com/questions/55409641/asyncio-run-cannot-be-called-from-a-running-event-loop-when-using-jupyter-no 

Code on GitHub:
    The code is also available at repo Utility on GitHub.        
"""
import psutil 
import asyncio
import threading

"""
A class that handles process in OS.
"""
class OSProcessHandler():
    """
    A class that achieve the goal by psutil module.
    """
    class Psutil():
        """
            Intro:
                Get all processes whose name is processName.
            Parameter:
                1. processName: name of process.
            Returned Value:
                Returns a list. Indicates all processes whose  process name is matched with processName.
        """
        @staticmethod
        def GetProcesses(processName:str) -> list :
            if processName is None:
                raise Exception("The processName must not be a NoneType object.")
            if not isinstance(processName, (str)):
                raise Exception("The processName must be a string.")
            if len(processName) <= 0:
                raise Exception("The processName must not be empty string.")
            
            procs = list()
            # iterate all processes.
            for proc in psutil.process_iter():
                # match processName and the proc.name.
                if processName in proc.name():
                    procs.append(proc)
            return procs      
        
async def get_pid(process):
    # sleep for 1 second.
    await asyncio.sleep(1)
    # return pid of process.
    return process.pid

async def set_after(fut, delay, value):
    # Sleep for *delay* seconds.
    await asyncio.sleep(delay)
    # Set *value* as a result of *fut* Future.
    fut.set_result(value)
    
def cancel_task(task,*argv,**kwargv):
    print("cancel_task:")
    # cancel the task
    task.cancel()
    
async def main():
    try:
        processName = 'msedge.exe'
        # Get all process whose process name is 'msedge.exe'
        procs = OSProcessHandler.Psutil.GetProcesses(processName)
        # Get the running loop with asyncio module.
        loop = asyncio.get_running_loop()
        # Create a Future object.
        fut = loop.create_future()
        # Create a Task object which: 
        # 1. the callback is executed (if it is not cancelled).
        # 2. when executed, delay for 2 seconds, then set the value of fut as get_task(proc[0]).
        handler1 = loop.create_task(set_after(fut, 2, get_pid(procs[0]) ) )
        # Create a threading Timer object to:
        # 1. execute the callback cancel_task with a list of arguments argv after 3 seconds of computing (if it is not cancelled).
        thread1 = threading.Timer(3,cancel_task,[handler1],None)
        # start to compute.
        thread1.start()
        # await fut and return result into variable result (if the task handler1 is not cancelled).
        result = await fut
        # return the result.
        return result
    
    except RuntimeWarning as ex:
        print(ex)

"""
Intro:
    Print infos about t.
Parameter:
    1. t: info
Returned Value:
    None
"""
def print_info(t):
    print(t)
    print(type(t))
    print(dir(t))
    
"""
Intro:
    Print task and its result (returned by result() method).
Parameter:
    1. t: task
Returned Value:
    None
"""
def print_task(t):
    print("t:")
    print_info(t)
    print("t.result():")
    print_info(t.result())
    
if __name__ == '__main__':
    
    # We have to do troublesome condition check due to different ways to handle running loop in different IDE or Python interpreter etc.
    # The code is modified from the Jean Monet's reply on the stackoverflow.
    # https://stackoverflow.com/questions/55409641/asyncio-run-cannot-be-called-from-a-running-event-loop-when-using-jupyter-no
    # For more details, see my notes at GitHub. (NOT written yet, but ready to write.)
    try:
        # Try to get current running loop with asyncio module. 
        loop = asyncio.get_running_loop()
    except RuntimeError:  # 'RuntimeError: There is no current event loop...'
        loop = None
    
    # Check loop is None (such as When there are no current running loop, thus raise RuntimeError.) , and 
    # the loop is running.
    if loop and loop.is_running():
        # It occurs such as when one of these conditions are NOT satisfied: 
        # 1. Python ≥ 3.7, and 
        # 2. IPython < 7.0
        print('Async event loop already running. Adding coroutine to the event loop.')
        try:
            # Create a Task object with coroutine object -- main().
            task = loop.create_task(main())
            # Add a callback "lambda t: print_task(t)" to task when it is completed done. (NOT including the case that it is cancelled.)
            task.add_done_callback(
                lambda t: print_task(t)
            )
        except TimeoutError as ex:
            print("TimeoutError:")
            print(ex)
            
    else:
        # Otherwise,
        # It occurs such as when all of these conditions are satisfied: 
        # 1. Python ≥ 3.7, and 
        # 2. IPython < 7.0
        print('Starting new event loop')
        # Just start a new event loop.
        result = asyncio.run(main())
