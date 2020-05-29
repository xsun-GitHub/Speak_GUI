import pyttsx3
import tkinter as tk
from PIL import ImageTk, Image
import requests

engine = pyttsx3.init();
voices = engine.getProperty('voices')
#for voice in voices:
#    print("Voice: %s" % voice.name)
#    print(" - ID: %s" % voice.id)
#    print(" - Languages: %s" % voice.languages)
#    print(" - Gender: %s" % voice.gender)
#    print(" - Age: %s" % voice.age)
#    print("\n")

root = tk.Tk()                   # Create the root (base) window
#root.geometry("300x300")
canvas = tk.Canvas(root, height=600, width=600).pack()

def speak(entry,x):
    #engine = pyttsx3.init();
    engine.setProperty("voice", voices[x].id)
    engine.say(entry);
    engine.runAndWait();

def translate(entry):
    key = "trnsl.1.1.20200516T221023Z.3af20d14a00c909c.11418a8100b8b771fe82a5077a0516b06de394aa"
    url = "https://translate.yandex.net/api/v1.5/tr.json/translate"
    params = {"AppID": key, "from":"en","to":"es","text":"hello world"}
    response = requests.get(url, params=params)
    print(response.text)
    
#class Action():
#    def __init__(self, entry):
#        self.speak = 
    

#background_image = tk.PhotoImage(file="coast.png")
background_image = ImageTk.PhotoImage(Image.open("landscape.jpg").resize(size=(600,600)))
background_lable = tk.Label(root, image=background_image)
#background_lable.pack(expand=1, side='left')
background_lable.place(relwidth=1, relheight=1)
#background_lable.pack()                   # Put the label into the window

frame = tk.Frame(root, bg='yellow',bd=5)
frame.place(relx=0.1, rely= 0.05, relwidth=0.6, relheight=0.8)
Entry = tk.Entry(frame, bg='white')
Entry.place(relwidth=1, relheight=0.495)
Translation = tk.Entry(frame, bg='white')
Translation.place(rely= 0.505, relwidth=1, relheight=0.5)

frame2 = tk.Frame(root, bg='yellow',bd=5)
frame2.place(relx=0.75, rely= 0.05, relwidth=0.2, relheight=0.8)

button1 = tk.Button(frame2, text="Press to \n speak English \n 按下讲英语", command=lambda:translate(Entry.get()))
button1.place(rely= 0, relwidth=1, relheight=0.33)

button2 = tk.Button(frame2, text="Press to \n speak German \n 按下讲德语", command=lambda:speak(Entry.get(),2))
button2.place(rely= 0.335, relwidth=1, relheight=0.33)

button3 = tk.Button(frame2, text="Press to \n speak Chinese \n 按下讲中文", command=lambda:speak(Entry.get(),3))
button3.place(rely= 0.67, relwidth=1, relheight=0.33)



root.mainloop()                             # Start the event loop