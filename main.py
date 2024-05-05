"""
pip install gtts sounddevice soundfile
"""

# Import necessary libraries
from tkinter import *
from gtts import gTTS
import tkinter as tk
import sounddevice as sd
import soundfile as sf
import tempfile
import os

# Create Class for Text-to-Speech app
class Text_to_Speech(tk.Tk):
    def __init__(self):
        super().__init__()
        # Window attributes
        self.geometry("350x350")
        self.configure(bg='ghost white')
        self.title("TEXT TO SPEECH")

        # Label and Entry Field
        Label(self, text="TEXT_TO_SPEECH", font="arial 20 bold", bg='white smoke').pack()
        Label(text="Pythonify", font='arial 15 bold', bg='white smoke', width='20').pack(side='bottom')
        self.msg = StringVar()
        Label(self, text="Enter Text", font='arial 15 bold', bg='white smoke').place(x=20, y=60)
        self.entry_field = Entry(self, textvariable=self.msg, width='50')
        self.entry_field.place(x=20, y=100)


    # Function to convert text to speech
    def Text_to_speech(self):
        # Get text from entry field
        Message = self.entry_field.get()
        # Convert text to speech using gTTS
        speech = gTTS(text=Message)

        # Create a temporary file to save the speech
        with tempfile.NamedTemporaryFile(delete=False) as file:
            filename = file.name + ".wav"
            speech.save(filename)

        data, fs = sf.read(filename)
        sd.play(data, fs)
        # Wait until the sound is finished playing
        sd.wait()
        # Delete the temporary file
        os.remove(filename)

    def Reset(self):
        self.msg.set("")

    def Exit(self):
        self.destroy()


def main():
    # Instance of the class
    window = Text_to_Speech()

    # Buttons to play, reset and exit
    Button(window, text="PLAY", font='arial 15 bold', command=window.Text_to_speech, width='4').place(x=25, y=140)
    Button(window, font='arial 15 bold', text='EXIT', width='4', command=window.Exit, bg='OrangeRed1').place(x=100,
                                                                                                             y=140)
    Button(window, font='arial 15 bold', text='RESET', width='6', command=window.Reset).place(x=175, y=140)

    window.mainloop()


if __name__ == "__main__":
    main()
