import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import pyautogui
import skimage
import cv2
import keras
import PIL
from keras.src.saving import serialization_lib
serialization_lib.enable_unsafe_deserialization()



def pic_segment(image, image_height, image_width):
    """
    Функция делит изображение на сегменты размером 512x512 для более точного определения КЗО
    
    Параметры:
    image - изображения для сегментации
    image_height - высота сегмента
    image_width - ширина сегмента
    
    Выход:
    В качестве выходного значения выводится массив изображений
    """
    segment_img = np.zeros((1, image_width, image_height, 3), dtype = np.uint8)
    counter = 0
    for i in range(0, image.shape[0], image_height):
        for j in range(0, image.shape[1], image_width):
            segment_img += np.array(image[i:i+image_height, j:j+image_width,:3])
            counter += 1
    return segment_img

def detect_KZO(img_detect, filepath_model):
    """
    Функция определения КЗО
    
    Параметры:
    img_detect - массив изображений для определения КЗО
    filepath_model - место расположения файлов обученной модели
    """
    model = keras.models.load_model(filepath_model)
    for i in range(0, len(img_detect)):
        pred = model.predict(img_detect[i], verbose = 1)
        pred_t = (pred > 0.33).astype(np.uint8)
    return pred_t

# def pic_concat(pred_t, image, image_height, image_width):
#     x, y = image.size
   
def pic_outprut(pred_t,segment_img):
    plt.figure(figsize=(100, 200))
    for i in range(0, len(segment_img)):
        plt.subplot(5,5,i+1)
        skimage.io.imshow(segment_img[i])
        plt.show
    for j in range(0, len(pred_t)):
        plt.subplot(5,5,j+2)
        skimage.io.imshow(np.squeeze(pred_t[j]))
    plt.tight_layout()
    

if __name__ == "__main__":
    filepath_model = 'F:/Codes/Model AI/Testmodel/location.keras'
    image = cv2.imread('F:/Codes/Model AI/TESTIM.png')[:,:,:3]
    img_wight = img_height = 512
    
    segment_img = pic_segment(image, img_height, img_wight)
    pred_t = detect_KZO(segment_img, filepath_model)
    pic_outprut(pred_t, segment_img)