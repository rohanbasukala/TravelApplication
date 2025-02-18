import cv2
from PIL import ImageTk
from PIL import *
from PIL import Image
import tkinter as tk
from tkinter import *
from tkinter.filedialog import askopenfilename


video = "maroon5.mk4"
Cascade = "haarcascade_frontalface_default.xml"

def getvideofile():
	global video
	video = askopenfilename()
	print (video)
	return video

def getcascadefile():
	global Cascade
	Cascade = askopenfilename()
	print (Cascade)
	return Cascade


if __name__ == '__main__':
    try:
        root = tk.Tk()

        image_label = tk.Label(master=root)
        image_label.grid(column=0, row=0, columnspan=2, rowspan=1)
        background = ImageTk.PhotoImage(file='criminal.jfif')
        image_label['image'] = background

        button_frame = tk.Frame(root)
        button_frame.grid(column=0, row=1, columnspan=1) 

       
        
        video_choose_button = tk.Button(master=button_frame, text='Choose Video',command=lambda: getvideofile())
        video_choose_button.grid(column=0, row=0, sticky='ew')
        # video = getfile()
        #print video

        cascade_choose_button = tk.Button(master=button_frame, text='Choose Cascade',command=lambda: getcascadefile())
        cascade_choose_button.grid(column=0, row=1, sticky='ew')
        #print Cascade


        # imgfolder_choose_button = tk.Button(master=button_frame, text='Choose Folder to put images',command=lambda: getfile())
        # imgfolder_choose_button.grid(column=0, row=2, sticky='ew')
        # folder = getfile()
        # print folder

        #start button_frame
        start_button = tk.Button(master=button_frame, text='Start',command=root.destroy)
        start_button.grid(column=0, row=3, sticky='ew')
        root.mainloop()

       
        
    except Exception as e:
        print (e)

    import sys
    sys.argv = [video, Cascade]
    #execfile('webcam_cv3.py')
    exec(open('dataset_GUI.py').read())

    # from webcam_cv3 import *




    	
