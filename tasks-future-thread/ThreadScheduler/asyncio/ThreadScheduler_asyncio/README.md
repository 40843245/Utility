# ThreadScheduler_asyncio.py (all version)
## NOTICE 
NOTICE that 

1. In 1th version, I just reach my goal and test it. However, haven't wrapped the code into classes.

   I will do it in the future release.

# v1
### Intro
The code is mainly about the simple application of task, thread, and coroutine parallelism and handling with combination of these Python modules:

1. threading
2. asyncio

For more details, see the comment in source code.

## Source Code 
The source code is available at GitHub. Located at ../v1/Code/ThreadScheduler.py.

Link:

https://github.com/40843245/Utility/blob/main/tasks-future-thread/ThreadScheduler/asyncio/ThreadScheduler_asyncio/v1/Code/ThreadScheduler_asyncio.py

## Learn and Apply.
This section is for myself. If you are not interested in, you can skip it.

### What I have learned.
I have learning the basic concept of parallelism of task, thread, and coroutine. And the syntax of these Python modules.

1. threading
2. asyncio

### What keywords and class and methods I Applied in this code.

keywords:

1. await
2. async

asyncio module:
1. asyncio.sleep()
2. asyncio.get_running_loop()
3. asyncio.windows_events._WindowsSelectorEventLoop class:
   3.1. loop.is_running()
   3.2. loop.create_task()
   3.3. loop.create_future()
   3.4. loop.create_task()

4. Future class:
   fut.set_result()  
5. Task class:
   task.add_done_callback()
   task.cancel()

threading module:
1. threading.Timer()
2. thread1.start()

## Ref
For reference, see the section Additional references on comments of the source code.
## Additional Ref
See above.

## Release Notes
### 2023/11/14 9:08 a.m.
Initial Notes.
### 2023/11/14 9:43 a.m.
Add infos. 

Update the references. 
