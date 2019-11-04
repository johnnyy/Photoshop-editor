
import sys

import cv2
import tkinter
from tkinter import filedialog
from tkinter import *
from tkinter import ttk
from tkinter.colorchooser import *
from tkinter import messagebox
from tkinter import simpledialog
from  PIL import Image,ImageTk
import matplotlib.pyplot as plt
import numpy as np
import os
import button_tools as bt
from tkinter import messagebox as mbox


#media do rgb gray word
        
        
class App:
    def __init__(self,root):


       #Frames
        self.root = root
        self.init_tools()
        self.init_info()
    #    self.root.bind('d', self.function)
        self.command = 0;
        
        #teste.title("Photo")
        
        #self.frame1 = tkinter.Frame(root)

        self.root.geometry("1300x1080+300+0")
        self.root.resizable(False, False)
        self.frame = tkinter.Frame(root,borderwidth=1, relief='ridge')# width=1920,height=1080)
        self.frame_img = tkinter.Frame(self.frame,relief='ridge',width=1300,height=1080,background="white")
        #self.frame_tools2 = tkinter.Frame(self.frame,relief='ridge',width=320,height=1080,background="white")
        
        
        self.label_img = tkinter.Label(self.frame_img)
        
        self.new()
        #self.frame_tools_icon = tkinter.Frame(self.frame_tools,relief='ridge')
       # self.frame_tools_others = tkinter.Frame(self.frame_tools,relief='ridge')
       
        self.root.bind("<B1-Motion>",self.function)
        self.root.bind("<ButtonRelease-1>",self.function_release)

      #Button
      #  self.buttonpencil = tkinter.Button(self.frame_tools, width=150, height=3,command=self.new, text="aaaa").grid(column=0, row=0, sticky="nsew")
      #  self.button2 = tkinter.Button(self.frame_tools, width=150, height=3,command=self.new, text="afaaa").grid(column=1, row=0, sticky="nsew")

        #photoshop = tkinter.Tk()
        #photoshop.title("Photoshop")
        #app = App(photoshop)


        #self.button1 = tkinter.Button(self.frame11,text='Logout',command=self.logout,font=('Courier',18))
        #self.button2 = tkinter.Button(self.root)

     #Menu
        menubar = tkinter.Menu(root)
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", font=('Courier',15), command=self.new)
        filemenu.add_command(label="Open", font=('Courier',15),command=self.open)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", font=('Courier',15), command=root.quit)

        menubar.add_cascade(label="File", menu=filemenu,font=('Courier',15))
        

        filemenu = tkinter.Menu(menubar, tearoff=0) 
        filemenu.add_command(label="Histogram correction", font=('Courier',15), command=self.histogram_correction)
        filemenu.add_command(label="Fourier Transform", font=('Courier',15),command=self.fourier)




        filte = tkinter.Menu(menubar, tearoff=0)
        filte.add_command(label="Laplacian", font=('Courier',15), command=self.new)
        filte.add_command(label="Gaussian", font=('Courier',15),command=self.open)
        filemenu.add_cascade(label="Filter", font=('Courier',15), menu=filte)


        seg = tkinter.Menu(menubar, tearoff=0)
        seg.add_command(label="Threshold", font=('Courier',15), command=self.threshold)
        seg.add_command(label="Seed", font=('Courier',15),command=self.seed)
        seg.add_command(label="Watershed", font=('Courier',15),command=self.watershed)
        filemenu.add_cascade(label="Segmentation", font=('Courier',15), menu=seg)



        menubar.add_cascade(label="Tools", menu=filemenu,font=('Courier',15))

    
        filemenu = tkinter.Menu(menubar, tearoff=0)
        filemenu.add_command(label="Tools Window", font=('Courier',15), command=self.open_tools)
        filemenu.add_command(label="Info Window", font=('Courier',15),command=self.open_info)
        filemenu.add_command(label="Image Info", font=('Courier',15),command=self.image_info)
        
        menubar.add_cascade(label="View", menu=filemenu,font=('Courier',15))


    #Pack
        root.config(menu=menubar)
       # self.frame_tools.grid(column=0, row=0, sticky="nsew")  
        self.frame_img.grid(column=0, row=0, sticky="nsew") 
        #self.frame_tools2.grid(column=2, row=0, sticky="nsew")


        #self.buttonpencil.grid(column=0, row=0, sticky="nsew")
        #self.button2.grid(column=1, row=0, sticky="nsew")
        
 #      self.buttonpencil.pack()
        #self.frame.pack()
        #self.frame_tools.pack()
        #self.frame_img.pack()
        #self.frame_tools2.pack()
        #self.frame_tools_icon.pack()
        self.frame.pack()
        self.button_ant = 'None'
        self.x1 = 'None'
        self.x2 = 'None'
        self.y1 = 'None'
        self.y2 = 'None'

        self.r,self.g,self.b,self.h,self.s,self.v = 0,0,0,0,0,0
        


    def threshold(self):
        pass
    def seed(self):
        pass
    def watershed(self):
        pass

    def getColor(self):
        color = askcolor()

        if(color[0] is None):
            return None
        else:
            return np.trunc(color[0])

    def function( self, event):
            
        if(self.command == 1):
            if(self.x1 != 'None'):
                self.x2 = event.x
                self.y2 = event.y
                self.img_draw = bt.command_pencil(self.img_cv,self.x1,self.y1,self.x2, self.y2,self.color,self.thickness) 
                self.draw(self.img_draw)
                self.x1 = self.x2
                self.y1 = self.y2
            else:
                self.x1 = event.x
                self.y1 = event.y
                
    def function_release(self, event):
        self.x1 = 'None'
        self.x2 = 'None'
        self.y1 = 'None'
        self.y2 = 'None'

        
    def pencil(self):
        self.color = self.getColor()
        if(self.color is None):
            pass
        else:

            answer = simpledialog.askstring("Thickness", "Enter with value of the thickness",parent=self.root)

            if(answer is not None and answer.isdigit()):
                if(int(answer) > 0):
                    self.thickness = int(answer)
                    bt.pencil_button(self.buttonpencil, self.button_ant)

                    self.button_ant = self.buttonpencil
                    self.command = 1
                else:
                    mbox.showerror("Error", "Value must be greater than 0")
                
            else:
                mbox.showerror("Error", "Value not integer")

        

       
        
    def open_tools(self):
        if(self.tools.winfo_exists() == 0):
            self.init_tools()
            
    def open_info(self):
        if(self.info.winfo_exists() == 0):
            self.init_info()

    def image_info(self):
        
        messagebox.showinfo("Image Info", "Shape Image: {}\nChannels: {}\nImage Format: {}".format(self.img_cv.shape[0:2],self.img_cv.shape[2],self.filename.split('.')[-1]))

    def init_tools(self):

        self.tools = tkinter.Toplevel(self.root)
        self.tools.resizable(False, False)
        self.tools.config(background='white')


        self.tools.title("Tools")
        self.tools.geometry("300x1080+0+0")
        self.frame_tools = tkinter.Frame(self.tools,relief='ridge',width=300,height=900, background="white")
        self.frame_tools_label = tkinter.Frame(self.tools,relief='ridge', background="white")

        self.label_title = tkinter.Label(self.frame_tools_label, text="    Photo EC  ", font=("Courier", 30), background="white").pack(fill='x')
        self.frame_tools_label.pack()
#
        img = Image.open("icons/pencil.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_pencil = ImageTk.PhotoImage(img)


        self.buttonpencil = tkinter.Button(self.frame_tools, width=50, height=50,command=self.pencil,image=photo_pencil)
        self.buttonpencil.image = photo_pencil
        self.buttonpencil.grid(column=0, row=0,padx = (1,1), sticky="nsew")
       
        
        img = Image.open("icons/r.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_r = ImageTk.PhotoImage(img)

        
        self.buttonr = tkinter.Button(self.frame_tools, width=50, height=50,command=self.channel_r,image=photo_r)
        self.buttonr.image = photo_r
        self.buttonr.grid(column=1, row=0, sticky="nsew")# self.buttonpencil.pack()

 
 
        img = Image.open("icons/g.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_g = ImageTk.PhotoImage(img)
        self.buttong = tkinter.Button(self.frame_tools, width=50, height=50,command=self.channel_g,image=photo_g)
        self.buttong.image = photo_g
        self.buttong.grid(column=2, row=0, sticky="nsew")
       
 
 
        img = Image.open("icons/b.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_b = ImageTk.PhotoImage(img)
        
        self.buttonb = tkinter.Button(self.frame_tools, width=50, height=50,command=self.channel_b,image=photo_b)
        self.buttonb.image = photo_b
        self.buttonb.grid(column=3, row=0, sticky="nsew")# self.buttonpencil.pack()
       

 
        img = Image.open("icons/im.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_im = ImageTk.PhotoImage(img)

        self.buttonim = tkinter.Button(self.frame_tools, width=50, height=50,command=self.no_channel,image=photo_im)
        self.buttonim.image = photo_im
        self.buttonim.grid(column=4, row=0, sticky="nsew")# self.buttonpencil.pack()
      
        img = Image.open("icons/retan.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_reta = ImageTk.PhotoImage(img)

        self.buttonre = tkinter.Button(self.frame_tools, width=50, height=50,command=self.select_reta,image=photo_reta)
        self.buttonre.image = photo_reta
        self.buttonre.grid(column=0, row=1, sticky="nsew")# self.buttonpencil.pack()


        img = Image.open("icons/h.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_h = ImageTk.PhotoImage(img)

        self.buttonh = tkinter.Button(self.frame_tools, width=50, height=50,command=self.channel_h,image=photo_h)
        self.buttonh.image = photo_h
        self.buttonh.grid(column=1, row=1, sticky="nsew")# self.buttonpencil.pack()
 
        img = Image.open("icons/s.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_s = ImageTk.PhotoImage(img)

        self.buttons = tkinter.Button(self.frame_tools, width=50, height=50,command=self.channel_s,image=photo_s)
        self.buttons.image = photo_s
        self.buttons.grid(column=2, row=1, sticky="nsew")# self.buttonpencil.pack()

        img = Image.open("icons/v.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_v = ImageTk.PhotoImage(img)

        self.buttonv = tkinter.Button(self.frame_tools, width=50, height=50,command=self.channel_v,image=photo_v)
        self.buttonv.image = photo_v
        self.buttonv.grid(column=3, row=1, sticky="nsew")# self.buttonpencil.pack()

        
 
        img = Image.open("icons/erase.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_coun = ImageTk.PhotoImage(img)

        self.buttoncount = tkinter.Button(self.frame_tools, width=50, height=50,command=self.select_countorn,image=photo_coun)
        self.buttoncount.image = photo_coun
        self.buttoncount.grid(column=4, row=1, sticky="nsew")# self.buttonpencil.pack()



        img = Image.open("icons/rectang.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_retang = ImageTk.PhotoImage(img)

        self.buttonretang = tkinter.Button(self.frame_tools, width=50, height=50,command=self.draw_retang,image=photo_retang)
        self.buttonretang.image = photo_retang
        self.buttonretang.grid(column=0, row=2, sticky="nsew")# self.buttonpencil.pack()


        img = Image.open("icons/elipse.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_elipse = ImageTk.PhotoImage(img)

        self.buttonelipse = tkinter.Button(self.frame_tools, width=50, height=50,command=self.draw_elipse,image=photo_elipse)
        self.buttonelipse.image = photo_elipse
        self.buttonelipse.grid(column=1, row=2, sticky="nsew")# self.buttonpencil.pack()


        img = Image.open("icons/circle.png")
        img = img.resize((30,30), Image.ANTIALIAS)
        photo_circle = ImageTk.PhotoImage(img)

        self.buttoncircle = tkinter.Button(self.frame_tools, width=50, height=50,command=self.draw_elipse,image=photo_circle)
        self.buttoncircle.image = photo_circle
        self.buttoncircle.grid(column=2, row=2, sticky="nsew")# self.buttonpencil.pack()




 
        self.frame_tools.pack()#.grid(rowspan=10,columnspan=10)



    def init_info(self):

        self.info = tkinter.Toplevel(self.root)
        self.info.resizable(False, False)
        self.info.config(background='white')

        self.info.title("Tools")
        self.info.geometry("320x1080+1600+0")
        self.frame_info = tkinter.Frame(self.info,relief='ridge',width=300,height=900, background="white")

    
 

 
        self.frame_info.pack()#.grid(rowspan=10,columnspan=10)


        
     



   
    def new(self):
      self.img_cv_b = cv2.imread("icons/white.png")
      self.filename = 'icons/white.png'
      self.img_cv_b = cv2.cvtColor(self.img_cv_b,cv2.COLOR_BGR2RGB)
      self.img_cv = cv2.resize(self.img_cv_b,(1300,1080),interpolation = cv2.INTER_AREA)
      self.img_cv_copy = self.img_cv.copy()
      self.draw(self.img_cv)




    def open(self):
      self.filename =  filedialog.askopenfilename(initialdir = "/home/johnny/Documentos",title = "Select file", filetypes = (("jpeg files","*.jpg"),("png files","*.png"),("bmp files","*.bmp"),("all files","*.*")))
      self.img_cv = cv2.imread(self.filename)
      self.img_cv = cv2.cvtColor(self.img_cv,cv2.COLOR_BGR2RGB)
      if(self.img_cv.shape[0] > 1300 or self.img_cv.shape[1] >1080):
          self.img_cv = cv2.resize(self.img_cv,(1300,1080),interpolation = cv2.INTER_AREA)
      self.img_cv_copy = self.img_cv.copy()
      self.draw(self.img_cv)
      
      
    def histogram_correction(self):
        img_to_yuv = cv2.cvtColor(self.img_cv,cv2.COLOR_BGR2YUV)
        img_to_yuv[:,:,0] = cv2.equalizeHist(img_to_yuv[:,:,0])
        hist_equalization_result = cv2.cvtColor(img_to_yuv, cv2.COLOR_YUV2BGR)
        self.draw(hist_equalization_result)
    def fourier(self):
        img_gray = cv2.cvtColor(self.img_cv, cv2.COLOR_RGB2GRAY)
        fft_img = np.fft.fft2(img_gray)
        fft_shift = np.fft.fftshift(fft_img) 
        mag_spectrum = np.log(np.abs(fft_shift)+1)
        mag_spectrum = mag_spectrum/np.max(mag_spectrum)*255
        self.draw(mag_spectrum)
        
      
    def draw(self,img_cv):
      self.img = Image.fromarray(img_cv)
      self.imgtk = ImageTk.PhotoImage(image=self.img)
      self.label_img.imgtk = self.imgtk
      self.label_img.configure(image=self.imgtk)
      self.label_img.pack(fill='x')



    def select_reta(self):
        pass
    def select_countorn(self):
        pass
                
    def draw_retang(self):
        pass
    def draw_circle(self):
        pass
    def draw_elipse(self):
        pass      


    def channel_r(self):
        
        if(self.r == 0):
            bt.button(self.buttonr,self.button_ant)
            self.button_ant = self.buttonr
            self.command = 2
            self.backup_img = self.img_cv.copy()
            self.red = self.img_cv[:,:,0]
            self.r,self.g,self.b,self.h,self.s,self.v = 1,0,0,0,0,0

            self.draw(self.red)

    def channel_g(self):
        
        if(self.g == 0):
            bt.button(self.buttong,self.button_ant)
            self.button_ant = self.buttong
            self.command = 2
            self.backup_img = self.img_cv.copy()
            self.green = self.img_cv[:,:,1]
            self.r,self.g,self.b,self.h,self.s,self.v = 0,1,0,0,0,0
            self.draw(self.green)

    def channel_b(self):
        
        if(self.b == 0):
            bt.button(self.buttonb,self.button_ant)
            self.button_ant = self.buttonb
            self.command = 2
            self.backup_img = self.img_cv.copy()
            self.blue = self.img_cv[:,:,2]
            self.r,self.g,self.b,self.h,self.s,self.v = 0,0,1,0,0,0
            self.draw(self.blue)

    def channel_h(self):
        
        if(self.h == 0):
            bt.button(self.buttonh,self.button_ant)
            self.button_ant = self.buttonh
            self.command = 2
            self.backup_img = self.img_cv.copy()
            self.hue = cv2.cvtColor(self.img_cv,cv2.COLOR_RGB2HSV)[:,:,0]
            self.r,self.g,self.b,self.h,self.s,self.v = 0,0,0,1,0,0
            self.draw(self.hue)


    def channel_s(self):
        
        if(self.s == 0):
            bt.button(self.buttons,self.button_ant)
            self.button_ant = self.buttons
            self.command = 2
            self.backup_img = self.img_cv.copy()
            self.satu = cv2.cvtColor(self.img_cv,cv2.COLOR_RGB2HSV)[:,:,1]
            self.r,self.g,self.b,self.h,self.s,self.v = 0,0,0,0,1,0
            self.draw(self.satu)

    def channel_v(self):
        
        if(self.v == 0):
            bt.button(self.buttonv,self.button_ant)
            self.button_ant = self.buttonv
            self.command = 2
            self.backup_img = self.img_cv.copy()
            self.valu = cv2.cvtColor(self.img_cv,cv2.COLOR_RGB2HSV)[:,:,2]
            self.r,self.g,self.b,self.h,self.s,self.v = 0,0,0,0,0,1
            self.draw(self.valu)


    def no_channel(self):
        
        bt.button('None',self.button_ant)
        self.button_ant = 'None'

        self.r,self.g,self.b,self.h,self.s,self.v = 0,0,0,0,0,0
        self.draw(self.img_cv)
            




photoshop = tkinter.Tk()

photoshop.title("Photoshop")
app = App(photoshop)
#app.show_frame()
photoshop.mainloop()

                  


