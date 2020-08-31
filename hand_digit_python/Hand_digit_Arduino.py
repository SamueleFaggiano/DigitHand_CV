import numpy as np
import tensorflow as tf
from keras.datasets import mnist
import cv2
import matplotlib.pyplot as plt
import serial, time

def send_by_UART(label):
    if label == 'zero':
        arduino.write(b'0')
    if label == 'one':
        arduino.write(b'1')
    if label == 'two':
        arduino.write(b'2')
    if label == 'three':
        arduino.write(b'3')
    if label == 'four':
        arduino.write(b'4')
    if label == 'five':
        arduino.write(b'5')


def count_pred(x):
    x = x.tolist()
    zero = x.count(0)
    one = x.count(1)
    two = x.count(2)
    three = x.count(3)
    four = x.count(4)
    five = x.count(5)
    var = {zero: 'zero', one: 'one', two: 'two', three: 'three', four: 'four', five: 'five'}
    return var.get(max(var))


def video():
    cap = cv2.VideoCapture(0)
    predictions = np.zeros(50)

    for output in range(0,50):
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        #blur image and then find contours by canny function
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edged = cv2.Canny(blurred, 30, 150)
        contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        # sort out numbers according to their area
        contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

        if contours is not None:
            #loop over the contours and get prediction
            for c in contours:
                (x, y, w, h) = cv2.boundingRect(c)
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                # '100' is to take a little bigger image without cutting the digit otherwise the prediction doesn't work
                roi = gray[y-50:y+h+50, x-50:x+w+50]
                ret, roi = cv2.threshold(roi, 130, 255, cv2.THRESH_BINARY_INV)

                # resize in (1x28x28)
                if roi is not None:
                    roi = cv2.resize(roi, (28, 28), interpolation = cv2.INTER_AREA)
                    roi = roi/255
                    roi_3d = roi[np.newaxis, :, :]
                    res = int(classifier.predict_classes(roi_3d, 1, verbose=0))
                    prob = classifier.predict_proba(roi_3d, 1, verbose=1)
                    print('Prediction: ', res)
                    predictions[output] = res
                    #print(predictions)
                    break

            cv2.imshow('Frame', frame)
            if cv2.waitKey(1) == 27:
                break

    best_pred = count_pred(predictions)
    send_by_UART(best_pred)
    cap.release()
    cv2.destroyAllWindows()
    image()

def close_image(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.destroyAllWindows()
        # inserisci pausa con movimento iniziale della mano
        video()

def image():
    img = cv2.imread('eye.jpg', 1)
    cv2.imshow('start', img)
    cv2.setMouseCallback('start', close_image)
    if cv2.waitKey(0) & 0xFF == 27:
        cv2.destroyAllWindows()

arduino = serial.Serial('COM12', baudrate=9600, timeout=0.1)

classifier = tf.keras.models.load_model('num_reader.model')
#(x_train, y_train), (x_test, y_test) = mnist.load_data()

if __name__ == '__main__':
    image()