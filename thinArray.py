from skimage import img_as_float
from skimage import io, color, morphology
import numpy as np
from PIL import Image
import os


srcImage = Image.open("C:\\Users\\pc\\Desktop\\SDGP\\signature-523237_960_720r.jpg")  # enter the image filename here
size = 256, 256
resizedImg = srcImage.resize(size)
resizedImg.save("C:\\Users\\pc\\Desktop\\SDGP\\resizedimg.jpg")
image = img_as_float(color.rgb2gray(io.imread("C:\\Users\\pc\\Desktop\\SDGP\\resizedimg.jpg")))
os.remove("C:\\Users\\pc\\Desktop\\SDGP\\resizedimg.jpg")
image_binary = image < 0.5
out_skeletonize = morphology.skeletonize(image_binary)
out_thin = morphology.thin(image_binary)
np.savetxt("C:\\Users\\pc\\Desktop\\SDGP\\binary3.txt", out_thin, fmt="%d")  # enter output filename here


# f, (ax0, ax1, ax2) = plt.subplots(1, 3, figsize=(10, 3))
#
# ax0.imshow(image, cmap='gray')
# ax0.set_title('Input')
#
# ax1.imshow(out_skeletonize, cmap='gray')
# ax1.set_title('Skeletonize')
#
# ax2.imshow(out_thin, cmap='gray')
# ax2.set_title('Thin')
#
# plt.savefig("C:\\Users\\pc\\Desktop\\signature-523237_960_7201S.jpg")
# plt.show()
