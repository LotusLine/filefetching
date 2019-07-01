from PIL import ImageGrab

image = ImageGrab.grab(bbox=(0,0,700,800))
image.save('screenshot3.png')
print("I just took a screenshot with pillow module")