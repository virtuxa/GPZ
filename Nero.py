import matplotlib.pyplot as plt
import matplotlib.image as img
import os
import numpy as np
import skimage
import cv2
import keras
from keras.src.saving import serialization_lib
from PIL import Image
from itertools import product
serialization_lib.enable_unsafe_deserialization()

def pic_segment(filename, dir_in, dir_out, d):
    """
#     The function divides the image into 512x512 segments for more accurate detection of KZO

#     Parameters: 
#     image - images for segmentation 
#     image_height - segment height 
#     image_width - segment width

#     Output: 
#     Saves image segments as files
#     """
    name, ext = os.path.splitext(filename)
    img = Image.open(os.path.join(dir_in, filename))
    w, h = img.size
    counter = 0

    grid = product(range(0, h-h%d, d), range(0, w-w%d, d))
    for i, j in grid:
        box = (j, i, j+d, i+d)
        out = os.path.join(dir_out, f'{counter}{ext}')
        img.crop(box).save(out)
        counter += 1
    print("Total segments {}\n".format(counter))

def detect_KZO(segmet_path, filepath_model):
    """
    KZO detection function

    Parameters:
    img_detect - folder with image segments for EPC detection
    filepath_model - location of trained model files

    Output:
    Saves processed segments with selected EPC objects
    """
    files = next(os.walk(segment_path))[2]
    model = keras.models.load_model(filepath_model)
    for i in range(0, len(files)):
        segment_image_path = segment_path + str(i) + ".png"
        segment_image = cv2.imread(segment_image_path)[:,:,:3]
        print(segment_image.shape[0])
        pred = model.predict(segment_image, verbose = 1)
        pred_t = (pred > 0.33).astype(np.uint8)
        img = Image.fromarray(pred_t)
        img.imsave('F:/Codes/Model AI/Segment_nero/{}.png'.format(i))
   
def pic_output(pred_t,segment_img):
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
    import sys
    filepath_model = 'F:/Codes/Model AI/Testmodel/location.keras'
    filename = "TESST.png"
    image_path = 'F:/Codes/Model AI/'
    segment_path = 'F:/Codes/Model AI/Segment/'
    # image = cv2.imread('F:/Codes/Model AI/TESTIM.png')[:,:,:3]
    if img is None:
        print("Faild to load image file:")
        sys.exit(1)
    segment_path = 'F:/Codes/Model AI/Segment/'
    img_wight = img_height = d = 512
    for path in [segment_path]:
        if not os.path.exists(path):
            os.mkdir(path)
            print("DIRECTORY CREATED: {}".format(path))
        else:
            print("DIRECTORY ALREADY EXISTS: {}".format(path))
    
    pic_segment(filename, image_path, segment_path, d)
    detect_KZO(segment_path, filepath_model)
    # pic_output(pred_t, segment_img)