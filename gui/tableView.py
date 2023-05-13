
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *



class TableView( QTableWidget ):
    def __init__(self, data, *args):
        QTableWidget.__init__(self,*args)
        self.data = data
        self.setData()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setData(self):
        horHeaders = []
        for n, key in enumerate( sorted( self.data.keys() ) ):
            horHeaders.append( key )
            for m, item in enumerate( self.data[ key ] ):
                newItem = QTableWidgetItem( item )
                self.setItem( m, n, newItem )
        self.setHorizontalHeaderLabels( horHeaders )
        self.setVerticalHeaderLabels( horHeaders )



            
        
