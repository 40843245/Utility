Why the objects are not displayed in main window with layout (QHBoxLayout) in PyQt5?

I expected that there is a QPushButton object in the layout. 

However, in the following code. 

    from PyQt5.QtWidgets import QHBoxLayout , QVBoxLayout
    from PyQt5.QtWidgets import QApplication , QMainWindow
    from PyQt5.QtWidgets import QPushButton
    from PyQt5.QtCore import QRect
    
    import sys
    
    if __name__ == '__main__':
        app = QApplication(sys.argv)
        mainWindow = QMainWindow()
        mainLayout = QVBoxLayout()
        
        pushButton = QPushButton()
        
        
        mainWindow.setGeometry(QRect(0,0,1000,1000))
        
        pushButton.setText("Button")
        pushButton.setGeometry(QRect(20,20,100,35))
        
        mainLayout.addWidget(pushButton)
        mainWindow.setLayout(mainLayout)
        
        
        mainWindow.show()
        sys.exit(app.exec_())

I get a window without any objects that belongs to QWidget. 

Thank you for any reply.
