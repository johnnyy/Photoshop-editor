
import sys

import cv2
import tkinter
from tkinter import messagebox
from  PIL import Image,ImageTk
import matplotlib.pyplot as plt
import numpy as np
import os



        
        
class App:
    def __init__(self,root):
        self.root = root
        #self.frame1 = tkinter.Frame(root)
        self.frame = tkinter.Frame(root,borderwidth=1, relief='ridge',  width=1920,height=1080)
        self.frame1 = tkinter.Frame(self.frame, borderwidth=1, relief='ridge')  
        self.frame2 = tkinter.Frame(self.frame, borderwidth=1, relief='ridge')
        self.frame14 = tkinter.Frame(self.frame2, borderwidth=1, relief='ridge')  
        self.frame15 = tkinter.Frame(self.frame2, borderwidth=1, relief='ridge')  

        self.frame3 = tkinter.Frame(root, borderwidth=1, relief='ridge')
        self.frame11 = tkinter.Frame(root, borderwidth=1, relief='ridge')
        
        self.frame4 = tkinter.Frame(self.frame3, relief='ridge')  
        self.frame5 = tkinter.Frame(self.frame3, relief='ridge')  
        self.frame6 = tkinter.Frame(self.frame3, relief='ridge')
        self.frame7 = tkinter.Frame(self.frame3, relief='ridge')
        self.frame8 = tkinter.Frame(self.frame3, relief='ridge')
        self.frame9 = tkinter.Frame(self.frame3, relief='ridge')
        self.frame10 = tkinter.Frame(self.frame3, relief='ridge')
        
        self.frame12 = tkinter.Frame(self.frame3, relief='ridge')
        self.frame13 = tkinter.Frame(self.frame3, relief='ridge')

        self.frame1.grid(column=0, row=0, sticky="nsew")  
        self.frame2.grid(column=0, row=1, sticky="nsew") 
        self.frame14.grid(column=0, row=0, sticky="nsew") 
        self.frame15.grid(column=1, row=0, sticky="nsew")  


        self.frame3.grid(column=1, row=0, sticky="nsew")
        self.frame11.grid(column=1, row=1, sticky="nsew")
        
        
        self.frame4.grid(column=0, row=0, sticky="nsew",padx=140)  
        self.frame5.grid(column=0, row=1, sticky="nsew")  
        self.frame6.grid(column=0, row=2, sticky="nsew",pady=15)
        self.frame7.grid(column=0, row=3, sticky="nsew")  
        self.frame8.grid(column=0, row=4, sticky="nsew")  
        self.frame9.grid(column=0, row=5, sticky="nsew")
        self.frame10.grid(column=0, row=6, sticky="nsew", pady = (0,15))
        self.frame12.grid(column=0, row=8, sticky="nsew")
        self.frame13.grid(column=0, row=9, sticky="nsew")
 
        #label1 = tkinter.Label(frame1, text="Simple label")  
        #button1 = tkinter.Button(frame2, text="Simple button")  
        #button2 = tkinter.Button(frame3, text="Apply and close", command=root.destroy)
 
        
    
        self.width, self.height = 800, 600
        self.label1 = tkinter.Label(self.frame1,width=self.width,height=self.height)
        self.llaa = tkinter.Label(self.frame4,text="aa",font=('Courier',15))
        self.button1 = tkinter.Button(self.frame14,text='Capture',command=self.press_button1,width=int(self.width/25),font=('Courier',18))
        self.button2 = tkinter.Button(self.frame15,text='Try again',command=self.press_button2,width=int(self.width/25),font=('Courier',18))
        self.button3 = tkinter.Button(self.frame5,text='Analyze',command=self.press_button_analise,font=('Courier',18))
        self.button4 = tkinter.Button(self.frame11,text='Logout',command=self.logout,font=('Courier',18))
        self.button5 = tkinter.Button(self.root)
        self.button6 = tkinter.Button(self.root)
        

    
        self.resum_ = tkinter.Label(self.frame6,font=('Courier',22), text='')
        self.label_sexo = tkinter.Label(self.frame7,font=('Courier',15), text='')
        self.faixa_i = tkinter.Label(self.frame8,font=('Courier',15), text='')
        self.sentimento = tkinter.Label(self.frame9,font=('Courier',15), text='')
        self.sorrindo = tkinter.Label(self.frame10,font=('Courier',15), text='')
        
        #self.lmain.pack()
        #self.button1.pack(side='left')
        #self.button2.pack(side='right')
        self.capture = cv2.VideoCapture(0)

        self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.cam_ = 1
       # self.lmain.grid(row=0,columns=1,columnspan=10,rowspan=8)
        self.label1.pack(fill='x')
        self.button1.pack(fill='x')  
        self.button2.pack(fill='x')
        self.button3.pack(fill='x')
        self.button4.pack(fill='x')
       

        self.resum_.pack(side='left')
        
        self.label_sexo.pack(side='left')
        self.faixa_i.pack(side='left')
        self.sentimento.pack(side='left')
        self.sorrindo.pack(side='left')
        
        #self.button3.pack(fill='x')#side='right')
        self.llaa.pack(fill='x',pady=10)#grid(column=1,row=0,sticky='N')#.pack(side='left')
        
    def show_frame(self):
        if(self.cam_ == 1):
            
            ret,frame = self.capture.read()
            self.frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        
            self.print_image()
        self.label1.after(10, self.show_frame)
        
    def press_button1(self):
        self.cam_ = 0
        #self.capture.release()
    def print_image(self):
        self.img = Image.fromarray(self.frame)
        self.imgtk = ImageTk.PhotoImage(image=self.img)
        self.label1.imgtk = self.imgtk
        self.label1.configure(image=self.imgtk)
    
    def press_button2(self):
        
        #self.capture = cv2.VideoCapture(0)
        #self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.width)
        #self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.height)
        self.cam_ = 1
        self.resum_.config(text='')
        self.label_sexo.config(text='')
        self.faixa_i.config(text='')
        self.sentimento.config(text='')
        self.sorrindo.config(text='')
    
 #       self.nome.delete(0, 'end')
        self.button3.config(state='normal')
        self.button5.destroy()
        self.button6.destroy()

    def press_button_analise(self):
        pass
        
    def press_button_report(self):
        
        report = tkinter.Tk()
        report.title("Photo analysis report")
        rep = Report(report,self.username,self.response)
        report.mainloop()
        
    def press_button_charts(self):
       pass
        
        
            
    def logout(self):
        self.capture.release()

        self.root.destroy()
        
                
#window = App(root)
                
                


        




photoshop = tkinter.Tk()
photoshop.title("Photoshop")
app = App(photoshop)
app.show_frame()
photoshop.mainloop()
app.capture.release()
                  


