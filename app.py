import cv2
import gradio as gr
import numpy as np
from tensorflow.keras.models import load_model


model = load_model('model.h5')


classes = {
    3 : 'bhudha temple',
    1 : 'Badrinath temple',
    16 : 'india gate',
    31 : 'charminar',
    48 : 'hindu temple',
    66 : "statue of unity"
}


def predict_image(img):
    test = cv2.imread(img)
    test = cv2.resize(test, (64, 64))
    test = np.reshape(test, [1, 64, 64, 3])
    img = img.reshape((-1, 64, 64, 3))
    predict_x = model.predict(img)

    class_ = int(np.argmax(predict_x, axis=1))
    return classes.get(class_)


gr.Interface(fn=predict_image, inputs=gr.Image(shape=(64, 64)),
             outputs=gr.Label(num_top_classes=6)).launch(debug=True, share=True)
