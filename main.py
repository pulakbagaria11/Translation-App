from googletrans import Translator
import speech_recognition as sr
import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def fr_eng():
    try:

        # use the microphone as source for input.
        with sr.Microphone() as source2:

            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)

            # listens for the user's input
            audio2 = r.listen(source2)


            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()

            a = MyText

            translations = translator.translate([a], dest='fr')
            for translation in translations:
                print(translation.origin, '->', translation.text)
                SpeakText(translation.text)


            print("Did you say " + MyText)
    except:
        pass



def main():
    pass


win = tk.Tk()
win.geometry("720x480")
win.configure(bg='white')
r = sr.Recognizer()
translator = Translator()

logo = Image.open('schoollogo.png')
logo = logo.resize((75,75))
logo = ImageTk.PhotoImage(logo)
logol = tk.Label(win,bg='white', borderwidth=0, image=logo).place(x=0, y=0)

l1 = tk.Label(win, borderwidth=0,text='English to French translation app',bg='white', font=('Poppins', 25)).place(x=360, y=50, anchor='center')

uk = Image.open('uk.png')
uk = uk.resize((150, 100))
uk = ImageTk.PhotoImage(uk)
l3 = tk.Label(win, borderwidth=0,image=uk).place(x=150, y=150, anchor='center')

france = Image.open('france.png')
france = france.resize(((150, 100)))
france = ImageTk.PhotoImage(france)
l4 = tk.Label(win, borderwidth=0,image=france).place(x=570, y=150, anchor='center')

right = Image.open('right.png')
right = right.resize((150, 100))
right = ImageTk.PhotoImage(right)

credits = tk.Label(win, borderwidth=0, bg='white', text='Pulak Bagaria-X-MJ', font=('Poppins', 11)).place(x=710, y=460, anchor='se')
credits2 = tk.Label(win, borderwidth=0, bg='white', text='Aahil Memon-X-JA', font=('Poppins', 11)).place(x=710, y=480, anchor='se')


img1 = tk.Label(win,borderwidth=0, image=right).place(x=360, y=150, anchor='center')


img = Image.open('mic.png')
resized = img.resize((100, 100))
resized = ImageTk.PhotoImage(resized)
b1 = tk.Button(win, borderwidth=0, image=resized ,bg='white',command=fr_eng).place(x=360, y=360, anchor='center')


win.mainloop()