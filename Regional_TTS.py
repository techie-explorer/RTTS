import tkinter as tk
from tkinter import ttk
from gtts import gTTS
from langdetect import detect
import os
import os.path
from playsound import playsound
import threading
from PIL import ImageTk, Image

class RTTS(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Regional Text to Speech")
        self.iconbitmap('rtts_icon.ico')
        

        container = tk.Frame(self, bg='white')
        container.pack(side=tk.TOP, fill='both', expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # The following variable stores all the frame pages of the app
        self.frames = {}

        # main_frame_window is the page which contains widgets to run the application
        frame = main_frame_window(container, self)
        self.frames[main_frame_window] = frame
        frame.grid(row=0, column=0, sticky = 'nsew')

        # the following call puts the main_frame_window page as the visible frame of RTTS APP
        self.show_frame(main_frame_window)
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class main_frame_window(tk.Frame):
    # below 3 lines are common
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.controller = controller
        self.can = tk.Canvas(self, bg='lightblue', height = 800, width = 2000, relief = tk.RAISED)

        self.text_input= tk.StringVar()
        
      
        self.input_text = tk.Entry(self.can, textvariable = self.text_input,  background="white", font=("Helvetica",10), foreground = "#000000", insertbackground = "black")
        self.input_text.pack(side=tk.RIGHT)
        self.input_text.place(relx=0.243, rely=0.303, height=44, relwidth=0.49)

        #self.perform = threading.Thread(target = self.ok)
        #self.perform.isDaemon = True
        #try:
        self.button = tk.Button(self.can, text="Speech",font=("Helvetica",15), fg = "white",command = self.ok, bg= "blue")
        #except Exception as e:
            #my_app = RTTS()
            #my_app.mainloop()   

        self.button.pack()
        self.button.place(relx=0.385, rely=0.520, height=44, relwidth=0.25)
        self.can.pack(side=tk.TOP)

        ##self.language = tk.StringVar()
        #self.lang_label = tk.Label(self.can, textvariable = self.language)
        #self.lang_label.pack()
        #self.lang_label.place(relx=0.485, rely=0.420, height=50, relwidth=0.05)

        self.can.create_text(600, 365, text = 'Detected Language', font=("Verdana", 12), fill="Black") 

        """
        self.lang_label_head = tk.Label(self.can, textvariable = "Detected Language")
        self.lang_label_head.pack()
        self.lang_label_head.place(relx=0.185, rely=0.420, height=50, relwidth=0.05)
        """
        self.img = ImageTk.PhotoImage(Image.open("logo.png"))
        self.logo_label = tk.Label(self.can, image = self.img)
        self.logo_label.pack()
        self.logo_label.place(x=735,y=35)
        """
        self.status = tk.StringVar()
        self.status_label = tk.Label(self.can, textvariable = self.status)
        self.status_label.pack()
        self.status_label.place(relx=0.4, rely=0.85, height=55, relwidth=0.09)
"""
    
    #can.create_text(600, 665, text='Converting', font=("Verdana", 12), fill="Black", tags = "text")
    def ok(self):
        #stat="Converting"
        #self.status.set(stat)
        #self.status_label.config(text="Converting")
        #self.can.create_text(600, 565, text = 'Converting', font=("Verdana", 12), fill="Black", tags = "text") 
        if(os.path.isfile('speech.txt')):
            os.remove('speech.mp3')
        else:
            self.can.create_text(600, 665, text = 'Converting....', font=("Verdana", 12), fill="Black", tags = "text1")
            #self.can.create_text(600, 665, text='Converting', font=("Verdana", 12), fill="Black", tags = "text")
            self.can.delete("text")
            text = self.input_text.get()
            print ("Text is:" + text)
            lang = detect(text)
            #self.language.set(lang)
            self.can.create_text(1000, 365, text = lang, font=("Verdana", 12), fill="Black", tags = "text3")
            print("Text Language: ", lang)
            tts = gTTS(text=text, lang=lang)
            tts.save('speech.mp3')
            self.can.delete("text1")
            self.can.create_text(600, 665, text = 'Speaking....', font=("Verdana", 12), fill="Black", tags = "text") 
            #self.status.set("Speaking")
            playsound('speech.mp3', True)
            os.system("rm %s" %('speech.mp3'))
            self.can.delete("text")
            #self.status.set(" ")
            #print("deleted file")
            
my_app = RTTS()
my_app.mainloop()
