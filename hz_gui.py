from tkinter import *
from bs4 import BeautifulSoup
import urllib.request



'''
select towns and get train scheudle

use lists

and then GO button
'''


class MainFrame(Frame):
    def __init__(self,parent):
        Frame.__init__(self, parent)
        self.parent=parent
        self.countrynames = ('Argentina', 'Australia', 'Belgium', 'Brazil', 'Canada', 'China', 'Denmark', \
        'Finland', 'France', 'Greece', 'India', 'Italy', 'Japan', 'Mexico', 'Netherlands', 'Norway', 'Spain', \
        'Sweden', 'Switzerland')
        self.cnames = StringVar(value=self.countrynames)
        
        
        #scroll1
        
        #listbox2
        #scroll2
        
        #button
        
        #text
        
        self.GUI()
    

    def GUI(self):
        self.departureBox=Listbox(self,height=25,selectmode=SINGLE,listvariable=self.cnames)
        self.departureBox.grid(row=0,column=0)
    
    
    def GetData(self,departure,destination):
        pass
    

def main(): 
    root=Tk()
    mf=MainFrame(root)
    root.geometry('800x600')
    mf.grid(row=0,column=0)
    mf.mainloop()

main()

        