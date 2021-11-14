from tkinter import *
from tkinter import ttk
import sys
import requests

#Author : Vitalik Hakim aremeyaw_a@soshgic.edu.gh



root = Tk()
root.geometry('1080x400')
#root.resizable(0,0)
root.config(bg = 'ghost white')
root.title("Javascript Minifier")
Label(root, text = "Javascript Minifier", font = "arial 20 bold", bg='white smoke').pack()
Label(root,text ="@Vitalik-Hakim", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Label(root,text ="Paste Js code here", font = 'arial 13 bold', bg ='white smoke').place(x=200,y=60)
Input_text = Text(root,font = 'arial 10', height = 11, padx=5, pady=5, width = 60)
Input_text.place(x=30,y = 100)
Label(root,text ="Minified Js", font = 'arial 13 bold', bg ='white smoke').place(x=780,y=60)
Output_text = Text(root,font = 'arial 10', height = 11, wrap = WORD, padx=5, pady= 5, width =60)
Output_text.place(x = 600 , y = 100)
def Minify():
    minified = Input_text.get(1.0, END)
    url = 'https://www.toptal.com/developers/javascript-minifier/raw'
    data = {'input': minified}
    response = requests.post(url, data=data)
    Output_text.delete(1.0, END)
    Output_text.insert(END, response.text)
trans_btn = Button(root, text = 'Minify',font = 'arial 12 bold',pady = 5,command = Minify , bg = 'royal blue1', activebackground = 'sky blue', relief="flat", cursor="hand2")
trans_btn.place(x = 490, y= 180 )
root.mainloop()
