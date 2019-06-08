from PIL import Image
import os
im = Image.open(r'C:\Users\14813\Desktop\zhaopian\2.png')
# print(im)
# print(os.path.abspath(im))
cat_im = im.copy()
cat_im.save(r'./2.png')

# import os
# a = os.path.abspath('.')
# print(a)