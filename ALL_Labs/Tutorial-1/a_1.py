import skimage.data as data
import matplotlib.pyplot as plt
import skimage.io as io
img0 = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\5.1.12.tiff')
img1 = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\4.2.07.tiff')
img2 = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\indexed_color.png')

plt.subplot(3,1,1)
plt.title('Grayscale image')
plt.axis('off')
plt.imshow(img0,cmap='gray')

plt.subplot(3,1,2)
plt.title('RGB image')
plt.axis('off')
plt.imshow(img1)

plt.subplot(3,1,3)
plt.title('Indexed color image')
plt.axis('off')
plt.imshow(img2)

plt.show()





