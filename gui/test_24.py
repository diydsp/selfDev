#!/usr/bin/env python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# ninja stuff here!
import os
import importlib

import vehic00 as vehicSim
import plotVehic00 as plotVehic

import tableView as tv

def tableHack( table ):
    #table.setText(1,1, "City")
    table.setItem(1,1, QTableWidgetItem("City"))


def reloadVehicCode():
    importlib.reload( vehicSim )

def quit_program():
    """Quits the current program, with file objects and descriptors
    cleanup
    """
    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except:
        pass

    sys.exit()
     

# from https://stackoverflow.com/questions/11329917/restart-python-script-from-within-itself
def restart_program():
    """Restarts the current program, with file objects and descriptors
    cleanup
    """

    try:
        p = psutil.Process(os.getpid())
        for handler in p.get_open_files() + p.connections():
            os.close(handler.fd)
    except:
        pass
    #except Exception, e:
    #    logging.error(e)

    pppython = sys.executable
    os.execl(pppython, pppython, *sys.argv)

def buttonMake( win, text, pos, callback ):
    myButt = QPushButton( win )
    myButt.setText( text )
    myButt.move( pos['x'], pos['y'] )
    myButt.clicked.connect( callback )
    return myButt


def reloadMe( moduleName ):
    print( f"will now reload {moduleName}" )
    importlib.reload( moduleName )

def reload_vehicSim():
    reloadMe( vehicSim )


def addButtons( win ):
    buttonList = []
    lambload = lambda moduleName : reloadMe( moduleName )
    b1 = buttonMake( win, "reload plot", {'x':50,'y':20}, lambload )
    buttonList.append( b1 )
    b2 = buttonMake( win, "init", {'x':50,'y':70}, vehicSim.init )
    buttonList.append( b2 )
    b3 = buttonMake( win, "step", {'x':50,'y':120}, vehicSim.step )
    buttonList.append( b3 )
    b4 = buttonMake( win, "reload vehic code", {'x':50, 'y':170 }, reload_vehicSim )
    buttonList.append( b4 )
    b5 = buttonMake( win, "restart", {'x':50, 'y':220 }, restart_program )
    buttonList.append( b5 )
    b6 = buttonMake( win, "quit", {'x':50, 'y':270 }, quit_program )
    buttonList.append( b6 )
        
   

    data = {'col1':['1','2','3','4'],
            'col2':['1','2','1','3'],
            'col3':['1','1','2','1']}    
    table = tv.TableView( data, 4, 3 )
    table.show()

    tabHack = lambda tab : tableHack( table )
    b7 = buttonMake( win, "tableHack", {'x':50, 'y':320 }, tabHack )
    buttonList.append( b7 )

    return buttonList

def window():
    app = QApplication(sys.argv)
    win = QDialog()
    win.setGeometry(100,100,400,1000)

    addButtons( win )


    
    win.setWindowTitle("PyQt5")
    win.show()
    sys.exit(app.exec_())


                     
if __name__ == '__main__':
   window()


def b1_clicked():
   print ("Button 1 clicked")

def b2_clicked():
   print ("Button 2 clicked")

def meh():
   b1 = QPushButton(win)
   b1.setText("Button1")
   b1.move(50,20)
   b1.clicked.connect(b1_clicked)
   
   b2 = QPushButton(win)
   b2.setText("Button2")
   b2.move(50,50)
   b2.clicked.connect(b2_clicked)

   b3 = QPushButton(win)
   b3.setText("RunSim")
   b3.move(50,80)
   b3.clicked.connect( runSim )

