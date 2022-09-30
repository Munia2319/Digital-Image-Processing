import skimage.io as io
import matplotlib.pyplot as plt
img = io.imread('G:\\need to organise\\All_DIP\\Dataset\\4.2.05.tiff')
print(img)
plt.subplot(2,3,1)
plt.axis('off')
plt.title('original image')
io.imshow(img)

plt.subplot(2,3,2)
plt.axis('off')
plt.title('value added to image')
img_add=img+100
print("this is the added image")
print(img_add)
io.imshow(img_add)
io.show()
