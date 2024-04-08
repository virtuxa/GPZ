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
    The function divides the image into 512x512 segments for more accurate detection of EPCs

    Parameters: 
    image - images for segmentation 
    image_height - segment height 
    image_width - segment width

    Output: The output value is an array of images
    """
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
    

def detect_KZO(image, image_height, image_width, filepath_mod, counter):
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
    plt.imshow(np.squeeze(result), cmap = 'gray')
    plt.axis('off')
    save = 'image/test' + str(counter) + '.png'
    plt.savefig(save, dpi = 150)
   

if __name__ == "__main__":
    import sys
    filepath_model = 'location.keras'
    filename = "TestDen1.png"
    image_path = 'image/'
    segment_path = 'image/Segment/'
    if img is None:
        print("Faild to load image file:")
        sys.exit(1)
    img_wight = img_height = d = 512
    for path in [segment_path]:
        if not os.path.exists(path):
            os.mkdir(path)
            print("DIRECTORY CREATED: {}".format(path))
        else:
            print("DIRECTORY ALREADY EXISTS: {}".format(path))
    
    pic_segment(filename, image_path, segment_path, d)
    files = next(os.walk(segment_path))[2]
  
    for i in range(0, len(files)):
        img = segment_path + str(i) + ".png"
        image = skimage.io.imread(img)[:,:,:3]
        detect_KZO(image, img_height, img_wight, filepath_model, i)
 