import asyncio

"""
A class that handles the class asyncio.windows_events._WindowsSelectorEventLoop.
"""
class LoopHandler():
    """
    Intro:
        Get the current running loop.
        If either it does not exist or it is not running anymore, create a new loop.
        For more techinical details, see the following comments.
    Parameter:
        1. done_callback: The callback that executed once after the speficied task is completely done. (NOT including the case that it is cancelled.)
    Returned Value:
        None
    """
    @staticmethod
    def GetRunningLoop(done_callback,main):
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
                    done_callback
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
            
if __name__ == '__main__':
    async def main():
        print("main")
        
    def doneCallback():
        print("x")
    done_callback = doneCallback
    LoopHandler.GetRunningLoop(lambda t: done_callback(), main)
