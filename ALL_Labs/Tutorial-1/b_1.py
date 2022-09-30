import skimage.data as data
import matplotlib.pyplot as plt
import skimage.exposure as ex
import skimage.io as io


img0 = data.camera()
plt.imshow(img0,cmap='gray')
plt.show()


f = plt.figure()

f.show(plt.hist(img0.flatten(), bins=256))
plt.show()

img1=ex.equalize_hist(img0)

plt.imshow(img1)
plt.show()

f.show(plt.hist(img1.flatten(), bins=256))



