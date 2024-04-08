import numpy as np
import skimage as ski
import matplotlib.pyplot as plt
import skimage.io
import skimage.metrics as metrics

def Pirson(imageA,imageB):
    # print(imageA)
    n_inter = 255
    inter = [x*(255/n_inter) for x in range(0,n_inter+1)]
    size = imageA.shape[0]*imageA.shape[1]
    nA = np.zeros(n_inter)
    for x in imageA:
        for i in range(0, n_inter):
            nA[i] += sum(inter[i] <= z <= inter[i+1] for z in x)
    wA = nA
    # print(wA)
    # print(imageB)
    nB = np.zeros(n_inter)
    for x in imageA:
        for i in range(0, n_inter):
            nB[i] += sum(inter[i] <= z <= inter[i+1] for z in x)
    wB = nB
    # print(wB)

    pir = np.sum((wA-wB)**2/wA)
    print(pir)
    # nA = float(imageA.shape[0] * imageA.shape[1])
    # nB = float(imageB.shape[0] * imageB.shape[1])
    # Pa = imageA.astype("float")/nA+0.000000001
    # Pb = imageB.astype("float")/nB+0.000000001
    # dif = np.sum((imageA.astype("float")-imageB.astype("float"))**2/Pa)

    return "HUI"


def mse(imageA, imageB):

    err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)/float(imageA.shape[0] * imageA.shape[1])

    return err


def compare_images(imageA, imageB, title):
    # compute the mean squared error and structural similarity
    # index for the images
    m = mse(imageA, imageB)
    s = metrics.structural_similarity(imageA, imageB,win_size=3,channel_axis=0, multichanel=True,data_range=1.5)
    print(m)
    print(s)
    # setup the figure
    fig = plt.figure(title)
    plt.suptitle("MSE: %.3f, SSIM: %.3f" % (m, s))
    # show first image
    ax = fig.add_subplot(1, 2, 1)
    plt.imshow(imageA)
    plt.axis("off")
    # show the second image
    ax = fig.add_subplot(1, 2, 2)
    plt.imshow(imageB)
    plt.axis("off")
    # show the images
    plt.show()


imageA = ski.io.imread('image/test0.png')[104:616,224:736,1]
imageB = ski.io.imread('image/test1.png')[104:616,224:736,1]
imageC = ski.io.imread('image/test2.png')[104:616,224:736,1]
imageD = ski.io.imread('image/test3.png')[104:616,224:736,1]

print("MSE")
print(metrics.mean_squared_error(imageA, imageA))

print(metrics.mean_squared_error(imageA, imageC))
print(metrics.mean_squared_error(imageB, imageD))

print(metrics.mean_squared_error(imageA, imageB))
print(metrics.mean_squared_error(imageC, imageD))
print()

print('NRMSE')
print(metrics. normalized_root_mse(imageA, imageA))

print(metrics. normalized_root_mse(imageA, imageC))
print(metrics. normalized_root_mse(imageB, imageD))

print(metrics. normalized_root_mse(imageA, imageB))
print(metrics. normalized_root_mse(imageC, imageD))
print()

print("SSIM")
print(metrics.structural_similarity(imageA, imageA,win_size=3,channel_axis=0,data_range=1))

print(metrics.structural_similarity(imageA, imageC,win_size=3,channel_axis=0,data_range=1))
print(metrics.structural_similarity(imageB, imageD,win_size=3,channel_axis=0,data_range=1))

print(metrics.structural_similarity(imageA, imageB,win_size=3,channel_axis=0,data_range=1))
print(metrics.structural_similarity(imageC, imageD,win_size=3,channel_axis=0,data_range=1))
print()

print("ARE")
print(metrics.adapted_rand_error(imageA.astype("int"),imageA.astype("int")))

print(metrics.adapted_rand_error(imageA.astype("int"),imageC.astype("int")))
print(metrics.adapted_rand_error(imageB.astype("int"),imageD.astype("int")))

print(metrics.adapted_rand_error(imageA.astype("int"),imageB.astype("int")))
print(metrics.adapted_rand_error(imageC.astype("int"),imageD.astype("int")))
print()

print("HD standard")
print(metrics.hausdorff_distance(imageA, imageA, method='standard'))

print(metrics.hausdorff_distance(imageA, imageC, method='standard'))
print(metrics.hausdorff_distance(imageB, imageD, method='standard'))

print(metrics.hausdorff_distance(imageA, imageB, method='standard'))
print(metrics.hausdorff_distance(imageC, imageD, method='standard'))
print()

print("HD modified")
print(metrics.hausdorff_distance(imageA, imageA, method='modified'))

print(metrics.hausdorff_distance(imageA, imageC, method='modified'))
print(metrics.hausdorff_distance(imageB, imageD, method='modified'))

print(metrics.hausdorff_distance(imageA, imageB, method='modified'))
print(metrics.hausdorff_distance(imageC, imageD, method='modified'))
print()

print("NMI")
print(metrics.normalized_mutual_information(imageA, imageA, bins=200))


print(metrics.normalized_mutual_information(imageA, imageC, bins=200))
print(metrics.normalized_mutual_information(imageB, imageD, bins=200))

print(metrics.normalized_mutual_information(imageA, imageB, bins=200))
print(metrics.normalized_mutual_information(imageC, imageD, bins=200))
print()


fig = plt.figure("Image")

ax = fig.add_subplot(2, 2, 1)
plt.title("ImageA")
plt.imshow(imageA, cmap='gray')
plt.axis("off")

ax = fig.add_subplot(2, 2, 2)
plt.title("ImageB")
plt.imshow(imageB, cmap='gray')
plt.axis("off")

ax = fig.add_subplot(2, 2, 3)
plt.title("ImageC")
plt.imshow(imageC, cmap='gray')
plt.axis("off")

ax = fig.add_subplot(2, 2, 4)
plt.title("ImageD")
plt.imshow(imageD, cmap='gray')
plt.axis("off")

plt.show()