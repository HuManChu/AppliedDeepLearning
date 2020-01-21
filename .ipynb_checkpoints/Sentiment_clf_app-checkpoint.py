#!/usr/bin/python

# tkinter for GUI:
import tkinter
from tkinter import messagebox

# fastai for AI:
import fastai
from fastai import *
# fastai:
from fastai import *
from fastai.text import *
from fastai.callbacks import *


class SentitmentClassfierApp:
    def __init__(self):
        # create root window
        self.root = tkinter.Tk()
        self.root.title("Sentiment Classifier")
        self.root.geometry('1000x50')
        # Create two frames
        # One frame for the top of the window
        # Another frame for bottom of the window
        self.top_frame = tkinter.Frame(self.root)
        self.bottom_frame = tkinter.Frame(self.root)
        # Create two labels
        self.prompt_label = tkinter.Label(self.top_frame, text='Enter to classify sentence (english only):')
        self.entry = tkinter.Entry(self.top_frame, width=500)
        # Pack top frame widgets
        self.prompt_label.pack(side='left')
        self.entry.pack(side='left')
        # Create the button widgets
        self.calc_button = tkinter.Button(self.bottom_frame, text='Sentiment', command=self.get_sentiment)
        # root.destroy exits/destroys the main window
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', command=self.root.destroy)
        # Pack the buttons
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Now pack the frames also
        self.top_frame.pack()
        self.bottom_frame.pack()

        # Load trained Roberta Model:
        fastai.torch_core.defaults.device = 'cpu'
        self.learner = load_learner(path="./")

        tkinter.mainloop()

    # This method predicts the sentiment of the example text:
    def get_sentiment(self):
        sentiment = self.learner.predict(self.entry.get())
        if int(sentiment[0]) == 0:
            messagebox.showinfo('Result:', 'Negative sentiment')
        elif int(sentiment[0]) == 1:
            messagebox.showinfo('Result:', 'Positive sentiment')
        else:
            messagebox.showinfo('Result:', 'Unclear')


gui = SentitmentClassfierApp()