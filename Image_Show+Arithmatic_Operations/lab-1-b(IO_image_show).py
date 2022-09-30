import skimage.io as io
import matplotlib.pyplot as plt

img_01 = io.imread('G:\\need to organise\\All_DIP\\Dataset\\4.1.01.tiff')
img_02 = io.imread('G:\\need to organise\\All_DIP\\Dataset\\5.1.12.tiff')


plt.subplot(1,2,1)
plt.axis('off')
#plt.title('Color image ... .')
plt.imshow(img_01)

plt.subplot(1,2,2)
plt.axis('off')
#plt.title('Grayscale image.')
plt.imshow(img_02,cmap='gray')

plt.show()

