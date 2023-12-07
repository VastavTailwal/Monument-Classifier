import gradio as gr
import numpy as np
from keras.models import load_model


model = load_model("model.h5")

classes = {
    15: 'india gate',
    23: 'india gate',
    37: 'Agha Khan Palace',
    44: 'hindu temple',
    48: 'hindu temple',
    3: 'bhudha temple',
    1: 'Badrinath temple',
    31: 'charminar',
    66: "statue of unity"
}


def predict_image(img):
    img = img.reshape((-1, 64, 64, 3))
    predict_x = model.predict(img)
    class_ = int(np.argmax(predict_x, axis=1))
    return classes.get(class_)


gr.Interface(fn=predict_image, inputs="image", outputs=gr.Label(num_top_classes=49)).launch(debug=True, share=True)
