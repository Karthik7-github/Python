import PIL.Image as im 
 
# Open an image file 
img = im.open("E:\\Python Numpy and Pandas\\images\\ Pythonlogo.png") 
print(img.format)   # JPEG, PNG, etc. 
print(img.size)       # (width, height) 
print(img.mode)    # RGB, RGBA,L (grayscale), etc. 