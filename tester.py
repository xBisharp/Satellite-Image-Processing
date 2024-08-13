import numpy as np
import tkinter as tk
import PIL
from tkinter import ttk, filedialog
from PIL import Image, ImageTk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tensorflow as tf
from keras._tf_keras.keras import layers, models

model = tf.keras.models.load_model("out_model.keras")

def parse_predict(image):
    global model
    image = image.resize((64, 64), PIL.Image.LANCZOS)
    pixels = list(image.getdata())
    data = np.array([np.array([np.array([np.array(pixels[x * 64 + y]) for x in range(64)]) for y in range(64)])])
    data = data / 255.0
    data = data[..., tf.newaxis]
    prediction = model.predict(data)[0]
    print(np.argmax(prediction))
    print(prediction)
    return prediction


def Labeler(path):
    image_path = path
    original_image = Image.open(image_path).convert("RGB")


    categories = ["cloudy", "desert", "green", "water"]
    values = parse_predict(original_image)

    plt.barh(categories, values)

    plt.xlabel('Values')
    plt.ylabel('Categories')
    plt.title('Imaginea este')



    plt.show()
