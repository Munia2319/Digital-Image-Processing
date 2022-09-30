import numpy as np
import matplotlib.pyplot as plt
import skimage.io as io
import skimage.exposure as ex
img = io.imread('U:\\4-1\\Digital Image Processing LAB\\Lab_Report_4_5_6_7_8\\Dataset\\misc\\4.1.04.tiff')

plt.imshow(img)
plt.show()


r = img[:, :, 0]
g = img[:, :, 1]
b = img[:, :, 2]

plt.imshow(r)
plt.show()

plt.imshow(g)
plt.show()
plt.imshow(b)
plt.show()

r1=ex.equalize_hist(r)

plt.imshow(r1)
plt.show()

g1=ex.equalize_hist(g)

plt.imshow(g1)
plt.show()

b1=ex.equalize_hist(b)

plt.imshow(b1)
plt.show()

output = np.dstack((r1, g1, b1))

plt.imshow(output)
plt.show()
