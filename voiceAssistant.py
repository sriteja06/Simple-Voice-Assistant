import google.generativeai as genai
import pyttsx3
import speech_recognition as sr
import tkinter as tk
from tkinter.ttk import *
import customtkinter as Ctk
from PIL import Image,ImageTk
import time


global LbUpdate
apiKey="<YOUR API KEY>"

recog=sr.Recognizer()
txt_to_speech=pyttsx3.init()
txt_to_speech.setProperty("rate",150)
genai.configure(api_key=apiKey)
model=genai.GenerativeModel("gemini-pro")
recog=sr.Recognizer()

def toSpeech(text):
    txt_to_speech.say(text)
    txt_to_speech.runAndWait()
    LbUpdate.configure(text="Result Spoken")
    time.sleep(1)
    

def search(text):
    responce=model.generate_content(text)
    print(responce.text)
    toSpeech(responce.text)

def recognize():
    with sr.Microphone() as source:
        print("listening.......")
        recog.adjust_for_ambient_noise(source)
        aud=recog.listen(source)
        
    try:
        text=recog.recognize_google(aud)
        search(text)    
    except sr.UnknownValueError:
        toSpeech("Couldnt understand what you said")
    except sr.RequestError as err:
        toSpeech("Error fetching results; {0}".format(err))
    LbUpdate.configure(text="")
    
    

root=Ctk.CTk()
root.geometry("500x500")
root.config(background="#084C4E")

LbTitle=Ctk.CTkLabel(root,text='Simple Voice Assistant',text_color="#7F9CE5",bg_color="#084C4E",font=("arial ",22))
LbTitle.place(relx=0.5,rely=0.03,anchor=tk.CENTER)

LbUpdate=Ctk.CTkLabel(root,text="",text_color="#7F9CE5",bg_color="#084C4E")
LbUpdate.place(relx=0.5,rely=0.7,anchor=tk.CENTER)

BtMic=Ctk.CTkButton(root,text='Speak',font=("arial",22),border_color="#5075D1",bg_color="#084C4E",fg_color="#5075D1",corner_radius=100,border_width=1,command=recognize)
BtMic.place(relx=0.5,rely=0.5,anchor=tk.CENTER)

BtEx=Ctk.CTkButton(root,text="Exit",bg_color="#084C4E",fg_color="#C42006",font=("arial",22),command=root.destroy)
BtEx.place(relx=0.85,rely=0.95,anchor=tk.CENTER)

root.mainloop()

