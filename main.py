import path as path
from PIL import Image, ImageEnhance, ImageColor
from PIL import ImageFilter
import os
import PIL
from PIL.ImageFilter import (BLUR, CONTOUR, DETAIL, EDGE_ENHANCE, EDGE_ENHANCE_MORE, EMBOSS, FIND_EDGES, SMOOTH,
                             SMOOTH_MORE, SHARPEN)


# import cv2
# import imageio
# import matplotlib.pyplot as plt
# import selenium
import numpy as np
# import sys

def __init__(self):
    self.input_path = 'input/'
    self.output_path = 'output/'


def main():
    try:
        Image.open(path)
    except IOError:
        pass


# size_700 = (700, 700)

# filename = input("enter the file name: ")  # path and format
with Image.open("input/fairy-transparent.png") as im:
    width, height = im.size
    im.show(path, format)  # 1.show the image

size_700 = (700, 700)
# change file extension
for f in os.listdir('.'):
    if f.endswith(".jpg"):
        im = Image.open(f)
        fn, fext = os.path.splitext(f)

        # im.save("output/png/{}.png".format(fn))
        # resize files
        im.thumbnail(size_700)
        im.save('output/700/.{}'.format(fn, fext))

img1 = ImageColor.getrgb("yellow")
print(img1)
# using getrgb for red
img2 = ImageColor.getrgb("red")
print(img2)
im = Image.open(r"input/face_back.jpg").convert("L")# opening a  image
# getting colors
# multiband images (RBG)
im1 = Image.Image.getdata(im)
print("colors of the given image: ",im1)

# filename = input("enter a file name if you want to make it transparent:")
"""if you gonna input the file name instead"""
with Image.open("input/fairy-transparent.png") as im:
    rgba = im.convert("RGBA")
    datas = rgba.getdata()

# 2. select colors and make them transparent
newData = []
for item in datas:
    if item[0] == 6 and item[1] == 6 and item[2] == 6:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
rgba.putdata(newData)
rgba.show("output/t_img1.png", "PNG")
rgba.save("output/t_img1.png", "PNG")

# 3.make background transparent
with Image.open("input/fairy-transparent.png") as im:
    rgba = im.convert("RGBA")
    datas = rgba.getdata()
# select colors and make them transparent
newData = []
for item in datas:
    if item[0] == 247 and item[1] == 247 and item[2] == 247:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
rgba.putdata(newData)
rgba.show("output/t_img2.png", "PNG")
rgba.save("output/t_img2.png", "PNG")

# 4.merge two files
filename = 'output/t_img2.png'  # Front Image
filename1 = 'input/lake.png'  # Back Image

froImage = Image.open(filename)  # Open Front Image
background = Image.open(filename1)  # Open Background Image

froImage = froImage.convert("RGBA")  # Convert image to RGBA
background = background.convert("RGBA")  # Convert image to RGBA

width = (background.width - froImage.width) // 2  # Calculate width to be at the center
height = (background.height - froImage.height) // 1  # Calculate height to be at the center

background.paste(froImage, (width, height), froImage)  # Paste the frontImage at (width, height)
background.save("output/new2.png", "png")  # Save this image
background.show("output/new2.png", "png")

# 5. merge two files

filename2 = 'output/t_img1.png'  # Front Image
filename3 = 'input/lake.png'  # Back Image
froImage = Image.open(filename2)  # Open Front Image
background = Image.open(filename3)  # Open Background Image

froImage = froImage.convert("RGBA")  # Convert image to RGBA
background = background.convert("RGBA")  # Convert image to RGBA
width = (background.width - froImage.width) // 2  # Calculate width to be at the center
height = (background.height - froImage.height) // 2  # Calculate height to be at the center

background.paste(froImage, (width, height), froImage)  # Paste the frontImage at (width, height)
background.save("output/new1.png", "png")  # Save this image
background.show("output/new1.png", "png")

# 6.black and white
with Image.open("input/face_back.jpg") as im:
    im = im.convert("L")
    im.save("output/black_White.jpg")
    im.show("output/black_White.jpg")
    # 7.rotate 90 degrees
with Image.open("input/face_back.jpg") as im:
    im = im.rotate(90)
    im.save("output/rotate90.jpg")
    im.show("output/rotate90.jpg")
    # 8.rotate 180
with Image.open("input/face_back.jpg") as im:
    im = im.rotate(180)
    im.show("output/rotate180.jpg")

with Image.open("input/face_back.jpg") as im:
    # 9.filter_blur
    im = im.filter(ImageFilter.GaussianBlur(15))
    im.save("output/ blur_15.jpg")
    im.show("output/ blur_15.jpg")

    # 10.blur using PIL imageFilter
    im = Image.open("output/new2.png")
    im1 = im.filter(
        BLUR)  # Applying the BLUR filter You can change the value in filter function to see the deifferences
    im1.show("output/blur2.png")  # slight blur
    # increase contrast
    # Read image

# 11.increase the brightness of the image by 2.0
im = Image.open(r"output/new2.png")
im3 = ImageEnhance.Brightness(im)  # Creating object of Brightness class
im3.enhance(2.0).show()  # showing resultant image

# 12.increase the brightness of the image by 2.0
im = Image.open(r"output/new2.png")
im3 = ImageEnhance.Brightness(im)  # Creating object of Brightness class
im3.enhance(-1.0).show()  # showing resultant image
# increase the brightness and contrast using imread___
# 13.sharpen the image
img = Image.open('output/new2.png')
img1 = img.filter(SHARPEN)
# Applying the sharpen filter You can change the value in filter function to see the deifferences
img1.show("output/sharp.png")

# 14.print some random color as an image
image = PIL.Image.new(mode="RGB", size=(200, 200), color=(255, 153, 255))
image.show()

# 15.print the format of the image (terminal)
img = Image.open("output/new2.png")
print("format of this image is:", img.format)
# change the format and save it in the output(folder)
image = Image.open('output/new2.png')
print("Format of the image before: ", img, format)
image.save('output/new22.bmp')  # changed format
print("format of the image after: ", img, format)

# print the size of the image
img = Image.open("input/lake.png")
print("The size of this image is: ", img.size)
img = Image.open("output/t_img1.png")
print("The size of the second image is: ", img.size)

# channel drop example
img = Image.open(r'output/new2.png')
# Creating an array out of pixel values of the image
img_arr = np.array(img, np.uint8)
# Change the 2 to 1 if wanting to drop the green channel
img_arr[::, ::, 2] = 0
img = Image.fromarray(img_arr)
img.show()
#2

img_arr = np.array(img, np.uint8)
img_arr[::, ::, 0] = 0
img = Image.fromarray(img_arr)
img.show()
img.save("output/c_drop.png")
"""# 50/50 cropped image
im = Image.open(r"output/new2.png")
im = im.crop((500, 500, 500, 500))  # Show cropped Image
im.show("output/cropped.png")
"""
"""
img = cv2.imread("lake.png")
print(type(img))

# Shape of the image
print("Shape of the image", img.shape)

# [rows, columns]
crop = img[50:180, 100:300]

cv2.imshow('original', img)
cv2.imshow('cropped', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
image = Image.open(r"output/new2.png")
image.load()
r, g, b, a = image.split()
# merge funstion used
im1 = Image.merge('RGB', (r, g, b))
im1.show("output/merge.png")


# Create image object
with Image.open("output/new2.png") as img:
    img1 = img.filter(
        CONTOUR)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()
    img1.save("output/contor.png")

    img1 = img.filter(
        DETAIL)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()
    img1.save("output/detail.png")

    img1 = img.filter(
        EDGE_ENHANCE)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()
    img1.save("output/enhance.png")

    img1 = img.filter(
        EDGE_ENHANCE_MORE)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()
    img1.save("output/filter.png")

    img1 = img.filter(
        EMBOSS)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()
    img1.save("output/embos.png")

    img1 = img.filter(
        FIND_EDGES)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()

    img1 = img.filter(
        SMOOTH)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()

    img1 = img.filter(
        SMOOTH_MORE)  # Applying the sharpen filter You can change the value in filter function to see the deifferences
    img1.show()
    print("a histogram of the image shown last: ", img.histogram())


# creating a image object , if someone want to find out the band of the image
filename = input("the name of the band of the picture is:")
im = Image.open(filename, "r")
im2 = im.getbands()  # get bands of image
print(im2)  # print band names.
"""
# importing required libraries of opencv
import cv2

# importing library for plotting
from matplotlib import pyplot as plt

# reads an input image
img = cv2.imread('input/lake.png', 0)

# find frequency of pixels in range 0-255
histr = cv2.calcHist([img], [0], None, [256], [0, 256])

# show the plotting graph of an image
plt.plot(histr)
plt.show()

from matplotlib import pyplot as plt
img = cv2.imread('ex.jpg',0)
  
# alternative way to find histogram of an image
plt.hist(img.ravel(),256,[0,256])
plt.show()
"""