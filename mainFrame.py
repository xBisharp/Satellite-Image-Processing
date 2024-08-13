import cv2 as cv
import tkinter as tk
from tkinter import ttk
from MakeImageList import *
from PIL import Image,ImageTk
from filtreFrame import *
from analizaFrame import *
from mlFrame import *
from tester import *


filterImgdump = ""
current_nr = 0


class mainFrameClass(tk.Tk):

    def __init__(self,*args, **kwargs) :

        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.pack(side='top', fill= 'both', expand=True)

        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {}
        self.shared_data ={"image_number":"pyimage1"}

        
        for F in (StartPage,Vizualizator,Filtre,Procesare,Analiza):

            frame = F(container,self)

            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")
        
        
        self.show_frame(StartPage)


    def show_frame(self, cont,**kwargs):
        frame = self.frames[cont]

        frame.tkraise()

        self.shared_data.update(kwargs)

        
        


class StartPage(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)



        test1 = ttk.Label(self, text="                                                           ")
        test1.grid(row = 0, column = 1, padx = 10, pady = 10)

        label = ttk.Label(self, text="Pagina de start")

        label.grid(row = 1, column = 3, padx = 10, pady = 10)

        test = ttk.Label(self, text="                                                         ")
        test.grid(row = 2, column = 1, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Vizualizator",command = lambda : controller.show_frame(Vizualizator))
        button1.grid(row = 2, column = 3, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Procesare ML",command = lambda : controller.show_frame(Procesare))
        button2.grid(row = 6, column = 3, padx = 10, pady = 10)


        button3 = ttk.Button(self, text ="Analiza Imagini",command = lambda : controller.show_frame(Analiza))
        button3.grid(row = 4, column = 3, padx = 10, pady = 10)



class Filtre(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)



        global current_nr

        image_dump = filterImgdump
        

        imageLabel=ttk.Label(self,image= image_dump)
        imageLabel.grid(row=3,column=0,columnspan=5)

        def refresh(imageLabel,filterImgdump):

            imageLabel.grid_forget()
            imageLabel=ttk.Label(self,image=filterImgdump)
            imageLabel.grid(row=3,column=1,columnspan=5)

            button2 = ttk.Button(self,text = "Contur",command=lambda:Selector("Contur",current_nr,imageLabel))
            button2.grid(row = 1,column = 2,padx = 10,pady =10)

            button3 = ttk.Button(self,text = "Blur",command=lambda:Selector("Blur",current_nr,imageLabel))
            button3.grid(row = 1,column = 3,padx = 10,pady =10)

            button4 = ttk.Button(self,text = "Color Space",command=lambda:Selector("Color Space",current_nr,imageLabel))
            button4.grid(row = 1,column = 4,padx = 10,pady =10)

            button5 = ttk.Button(self,text = "Load",command=lambda:refresh(imageLabel,filterImgdump))
            button5.grid(row = 1,column = 5,padx = 10,pady =10)

            button6 = ttk.Button(self,text = "Erode",command=lambda:Selector("Erode",current_nr,imageLabel))
            button6.grid(row = 2,column = 5,padx = 10,pady =10)


            button7 = ttk.Button(self,text = "LAB",command=lambda:Selector("LAB",current_nr,imageLabel))
            button7.grid(row = 2,column = 4,padx = 10,pady =10)


            button8 = ttk.Button(self,text = "BGR",command=lambda:Selector("BGR",current_nr,imageLabel))
            button8.grid(row = 2,column = 3,padx = 10,pady =10)          




        def Leave():
            
            imageLabel.grid_forget()
            
            button2 = ttk.Button(self,text = "Contur",state=DISABLED,command=lambda:Selector("Contur",current_nr,imageLabel))
            button2.grid(row = 1,column = 2,padx = 10,pady =10)

            button3 = ttk.Button(self,text = "Blur",state=DISABLED,command=lambda:Selector("Blur",current_nr,imageLabel))
            button3.grid(row = 1,column = 3,padx = 10,pady =10)

            button4 = ttk.Button(self,text = "Color Space",state=DISABLED,command=lambda:Selector("Color Space",current_nr,imageLabel))
            button4.grid(row = 1,column = 4,padx = 10,pady =10)

            button5 = ttk.Button(self,text = "Load",command=lambda:refresh(imageLabel,filterImgdump))
            button5.grid(row = 1,column = 5,padx = 10,pady =10)

            button6 = ttk.Button(self,text = "Erode",state=DISABLED,command=lambda:Selector("Erode",current_nr,imageLabel))
            button6.grid(row = 2,column = 5,padx = 10,pady =10)


            button7 = ttk.Button(self,text = "LAB",state=DISABLED,command=lambda:Selector("LAB",current_nr,imageLabel))
            button7.grid(row = 2,column = 4,padx = 10,pady =10)


            button8 = ttk.Button(self,text = "BGR",state=DISABLED,command=lambda:Selector("BGR",current_nr,imageLabel))
            button8.grid(row = 2,column = 3,padx = 10,pady =10)

            controller.show_frame(Vizualizator)
            

        def Selector(message,current_nr,imageLabel):
            if message == "Contur":
                image_dump = Canny(current_nr)
            elif message == "Blur":
                image_dump = Blur(current_nr)
            elif message =="Color Space":
                image_dump = ColorSpace(current_nr)
            elif message == "Erode":
                image_dump = Erode(current_nr)
            elif message == "LAB":
                image_dump = LAB(current_nr)
            elif message == "BGR":
                image_dump = BGRR(current_nr)


        button1 = ttk.Button(self, text ="Inapoi",command = lambda : Leave())
        button1.grid(row = 1,column = 1,padx = 10,pady =10)

        button2 = ttk.Button(self,text = "Contur",state=DISABLED,command=lambda:Selector("Contur",current_nr,imageLabel))
        button2.grid(row = 1,column = 2,padx = 10,pady =10)

        button3 = ttk.Button(self,text = "Blur",state=DISABLED,command=lambda:Selector("Blur",current_nr,imageLabel))
        button3.grid(row = 1,column = 3,padx = 10,pady =10)

        button4 = ttk.Button(self,text = "Color Space",state=DISABLED,command=lambda:Selector("Color Space",current_nr,imageLabel))
        button4.grid(row = 1,column = 4,padx = 10,pady =10)

        button5 = ttk.Button(self,text = "Load",command=lambda:refresh(imageLabel,filterImgdump))
        button5.grid(row = 1,column = 5,padx = 10,pady =10)

        button6 = ttk.Button(self,text = "Erode",state=DISABLED,command=lambda:Selector("Erode",current_nr,imageLabel))
        button6.grid(row = 2,column = 5,padx = 10,pady =10)


        button7 = ttk.Button(self,text = "LAB",state=DISABLED,command=lambda:Selector("LAB",current_nr,imageLabel))
        button7.grid(row = 2,column = 4,padx = 10,pady =10)


        button8 = ttk.Button(self,text = "BGR",state=DISABLED,command=lambda:Selector("BGR",current_nr,imageLabel))
        button8.grid(row = 2,column = 3,padx = 10,pady =10)

        


class Analiza(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)


        test = ttk.Label(self, text="                          ")
        test.grid(row = 1, column = 1, padx = 10, pady = 10)
        # Create LabelFrames for each category
        frame1 = ttk.LabelFrame(self, text="Date de start")
        frame1.grid(row=1, column=2, padx=10, pady=10, sticky="nsew")

        frame2 = ttk.LabelFrame(self, text="Date despre vegetatie")
        frame2.grid(row=2, column=2, padx=10, pady=10, sticky="nsew")

        frame3 = ttk.LabelFrame(self, text="Date despre apa si umiditate")
        frame3.grid(row=3, column=2, padx=10, pady=10, sticky="nsew")

        frame4 = ttk.LabelFrame(self, text="Date despre materiale")
        frame4.grid(row=4, column=2, padx=10, pady=10, sticky="nsew")

        # Place the buttons in the appropriate LabelFrames
        button1 = ttk.Button(self, text="Inapoi", command=lambda: controller.show_frame(StartPage))
        button1.grid(row=0, column=2, padx=10, pady=10)

        button2 = ttk.Button(frame1, text="Viz. Bands", command=lambda: visualizeBands()) #1
        button2.grid(row=0, column=0, padx=10, pady=10)

        button3 = ttk.Button(frame1, text="Composite", command=lambda: compositeRGB()) #1
        button3.grid(row=0, column=1, padx=10, pady=10)

        button4 = ttk.Button(frame1, text="Histograms", command=lambda: histogramsA()) #1
        button4.grid(row=0, column=2, padx=10, pady=10)

        button6 = ttk.Button(frame2, text="NVDI", command=lambda: NVDI()) #2
        button6.grid(row=0, column=0, padx=10, pady=10)

        button5 = ttk.Button(frame2, text="SAVI", command=lambda: SAVI()) #2
        button5.grid(row=0, column=1, padx=10, pady=10)

        button7 = ttk.Button(frame3, text="VARI", command=lambda: VARI()) #3
        button7.grid(row=0, column=0, padx=10, pady=10)

        button8 = ttk.Button(frame3, text="MNDWI", command=lambda: MNDWI()) #3
        button8.grid(row=0, column=1, padx=10, pady=10)

        button9 = ttk.Button(frame3, text="NDMI", command=lambda: NDMI()) #3
        button9.grid(row=0, column=2, padx=10, pady=10)

        button10 = ttk.Button(frame4, text="Mat.Pam.", command=lambda: Clay()) #4
        button10.grid(row=0, column=0, padx=10, pady=10)

        button11 = ttk.Button(frame4, text="Mat.Fer.", command=lambda: Fier()) #4
        button11.grid(row=0, column=1, padx=10, pady=10)





class Procesare(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)

        label = ttk.Label(self, text ="")
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        path="MLlist/1.jpg"
        
        image_list = MakeImageList3()   
        

        myLabel =ttk.Label(self,image=image_list[0])
        myLabel.grid(row=3,column=1,columnspan=5)



        def forward(image_number,myLabel):
            myLabel.grid_forget()
            myLabel = ttk.Label(self,image=image_list[image_number-1])
            
            button2 = ttk.Button(self, text=">>>",command=lambda:forward(image_number+1,myLabel))
            if image_number == 4:
                button2 =ttk.Button(self,text=">>>",state=DISABLED)
            button2.grid(row = 1,column = 5,padx=10,pady=10)

            button4 = ttk.Button(self,text="Label",command= lambda:Labeler(path))
            button4.grid(row= 1,column=4,padx=10,pady=10)

            button3 = ttk.Button(self, text="<<<",command=lambda:backward(image_number-1,myLabel))
            button3.grid(row = 1,column = 3,padx=10,pady=10)

            myLabel.grid(row=3,column=1,columnspan=5)

            path = "MLlist/" + str(image_number) +".jpg"




        def backward(image_number,myLabel):
            myLabel.grid_forget()
            myLabel = ttk.Label(self,image=image_list[image_number-1])
            
            button2 = ttk.Button(self, text=">>>",command=lambda:forward(image_number+1,myLabel))
            button2.grid(row = 1,column = 5,padx=10,pady=10)
            
            button4 = ttk.Button(self,text="Label",command= lambda:Labeler(path))
            button4.grid(row= 1,column=4,padx=10,pady=10)

            button3 = ttk.Button(self, text="<<<",command=lambda:backward(image_number-1,myLabel))
            if image_number == 1:
                button3 =ttk.Button(self,text="<<<",state=DISABLED)
            button3.grid(row = 1,column = 3,padx=10,pady=10)


            myLabel.grid(row=3,column=1,columnspan=5)
            
            path = "MLlist/" + str(image_number) +".jpg"
        

        button1 = ttk.Button(self, text ="Inapoi",command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 1,column = 1,padx = 10,pady =10)

        button3 = ttk.Button(self,text = ">>>",command = lambda :forward(2,myLabel))
        button3.grid(row = 1,column = 5,padx=10,pady=10)

        button4 = ttk.Button(self,text="Label",command= lambda:Labeler(path))
        button4.grid(row= 1,column=4,padx=10,pady=10)

        button5 = ttk.Button(self,text = "<<<",state=DISABLED)
        button5.grid(row = 1,column = 3,padx=10,pady=10)


class Vizualizator(tk.Frame):
    def __init__(self, parent,controller):
        tk.Frame.__init__(self, parent)


        image_list = MakeImageList()   
        

        test = ttk.Label(self, text="")
        test.grid(row = 2, column = 1, padx = 10, pady = 10)
        myLabel =ttk.Label(self,image=image_list[0])
        myLabel.grid(row=4,column=1,columnspan=5)



        def forward(image_number,myLabel):
            myLabel.grid_forget()
            myLabel = ttk.Label(self,image=image_list[image_number-1])
            
            button2 = ttk.Button(self, text=">>>",command=lambda:forward(image_number+1,myLabel))
            if image_number == 3:
                button2 =ttk.Button(self,text=">>>",state=DISABLED)
            button2.grid(row = 1,column = 5,padx=10,pady=10)

            button4 = ttk.Button(self,text="Filtre",command= lambda:show_filtre(image_number))
            button4.grid(row= 1,column=4,padx=10,pady=10)

            button3 = ttk.Button(self, text="<<<",command=lambda:backward(image_number-1,myLabel))
            button3.grid(row = 1,column = 3,padx=10,pady=10)

            myLabel.grid(row=3,column=1,columnspan=5)




        def backward(image_number,myLabel):
            myLabel.grid_forget()
            myLabel = ttk.Label(self,image=image_list[image_number-1])
            
            button2 = ttk.Button(self, text=">>>",command=lambda:forward(image_number+1,myLabel))
            button2.grid(row = 1,column = 5,padx=10,pady=10)
            
            button4 = ttk.Button(self,text="Filtre",command= lambda:show_filtre(image_number))
            button4.grid(row= 1,column=4,padx=10,pady=10)

            button3 = ttk.Button(self, text="<<<",command=lambda:backward(image_number-1,myLabel))
            if image_number == 1:
                button3 =ttk.Button(self,text="<<<",state=DISABLED)
            button3.grid(row = 1,column = 3,padx=10,pady=10)


            myLabel.grid(row=3,column=1,columnspan=5)


        
        def show_filtre(current_image_number):
            controller.shared_data["image_number"] = image_list[current_image_number-1]
           
            global filterImgdump
            global current_nr 

            current_nr = current_image_number
            filterImgdump = image_list[current_image_number-1]
            
            controller.show_frame(Filtre)


        button1 = ttk.Button(self, text ="Pagina de Start",command = lambda : controller.show_frame(StartPage))
        button1.grid(row = 1,column = 1,padx = 10,pady =10)

        button2 = ttk.Button(self,text = ">>>",command = lambda :forward(2,myLabel))
        button2.grid(row = 1,column = 5,padx=10,pady=10)

        button4 = ttk.Button(self,text="Filtre",command= lambda:show_filtre(1))
        button4.grid(row= 1,column=4,padx=10,pady=10)

        button3 = ttk.Button(self,text = "<<<",state=DISABLED)
        button3.grid(row = 1,column = 3,padx=10,pady=10)


app = mainFrameClass()
app.mainloop()