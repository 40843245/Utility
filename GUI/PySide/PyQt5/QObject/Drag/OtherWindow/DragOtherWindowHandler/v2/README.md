# DragOtherWindowHandler.py (2th version)
## Fixed
1. Many QObjects can be on different y axis. Since I don't use QLayout, I just simply implement by method QObject.setParent.
## Known issues
Sorry that I did not test it carefully before updating. After a several try, I found a known issue.

For a QObject that is attached to window by method QObject.setParent, attaching it to other window (i.e. use method QObject.setParent to other window) will not take any effect. I don't know why it is, even if I google it for one and half hour.

Thus, I highly recommend you that use the old version. 

Available at GitHub :

  ../v1/DragOtherWindowHandler.py


## Release Notes
### 2023/10/16 14:58
Initial Notes.
