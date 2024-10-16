import pathlib
import platform

plt = platform.system()

if plt != 'Windows':
    pathlib.WindowsPath = pathlib.PosixPath


import gradio as gr
from fastai.vision.all import *
from fastai.vision.widgets import *
from fastai.learner import load_learner
from pathlib import Path

learn = load_learner('model.pkl')

countries = 'china','france', 'india', 'japan', 'usa'

def classify_image(img):
    country,idx,probs = learn.predict(img)
    return dict(zip(countries,map(float,probs)))


image = gr.Image(height=300,width=300)
label = gr.Label()

examples = [
    'testing_images/china.png',
    'testing_images/france.png',
    'testing_images/india1.png',
    'testing_images/india2.png',
    'testing_images/japan.png',
    'testing_images/usa.png'
]


intf = gr.Interface(fn=classify_image, inputs=image, outputs=label, examples=examples)

intf.launch(inline=False)