import os
from os import listdir
from tkinter import *
from PIL import Image,ImageTk


def MakeImageList():


    image_list = []


    for images in os.listdir("C:/Users/radul/Desktop/licenta/Images"):
        img_location = "C:/Users/radul/Desktop/licenta/Images/" + images

        dump = Image.open(img_location).resize((500,500))

        img = ImageTk.PhotoImage(dump)
        
        image_list.append(img)

   
    return image_list


def MakeSourceList():
    source_list = []
    
    for images in os.listdir("C:/Users/radul/Desktop/licenta/Images"):
        img_location = "C:/Users/radul/Desktop/licenta/Images/" + images
        source_list.append(img_location)
    return source_list




def MakeImageList2():


    image_list = []


    for images in os.listdir("C:/Users/radul/Desktop/licenta/Images"):
        img_location = "C:/Users/radul/Desktop/licenta/Images/" + images

        dump = Image.open(img_location).resize((500,500))

        img = ImageTk.PhotoImage(dump)
        
        image_list.append(img)

   
    return image_list


def MakeImageList3():
    

    image_list = []


    for images in os.listdir("C:/Users/radul/Desktop/licenta/MLList"):
        img_location = "C:/Users/radul/Desktop/licenta/MLList/" + images

        dump = Image.open(img_location).resize((500,500))

        img = ImageTk.PhotoImage(dump)
        
        image_list.append(img)

   
    return image_list

