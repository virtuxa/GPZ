
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



def pic_resize(image, image_height, image_width):
    """
    The function divides the image into 512x512 segments for more accurate detection of EPCs

    Parameters: 
    image - images for segmentation 
    image_height - segment height 
    image_width - segment width

    Output: The output value is an array of images
    """
    

def detect_KZO(image, image_height, image_width, filepath_mod):
    """
    EPC detection function

    Parameters: 
    img_detect - image array for EPC detection 
    filepath_model - location of trained model files
    """
    img = np.zeros((1, image_width, image_height, 3), dtype = np.uint8)
    model = keras.models.load_model(filepath_model)
    res_image = skimage.transform.resize(image, (image_width, image_height), mode = 'constant', preserve_range = True)
    img[0] = res_image
    res = model.predict(img, verbose = 1)
    result = (res > 0.2).astype(np.uint8)
    skimage.io.imshow(np.squeeze(result))
    plt.savefig('image/test3.png')
    plt.show()
    
    
    
   
def pic_outrut(pred_t,segment_img):
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
    filepath_model = 'location.keras'
    image = skimage.io.imread('image/1.png')[:,:,:3]
    w = image.shape[0]
    h = image.shape[1]
    image_width = image_height = 512
    
    detect_KZO(image, image_height, image_width, filepath_model)