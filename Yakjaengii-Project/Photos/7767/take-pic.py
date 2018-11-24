from picamera import PiCamera
from time import sleep
from PIL import Image

camera = PiCamera()
mydir  = '/home/pi/Yakjaengii-Project/Photos/7767/7767-NUM'

camera.start_preview()
for i in range(20):
	filename = 'ato' + str(i) + '.jpg'
	print(filename)
	fullpath = mydir + filename
	camera.capture(fullpath)
	imageObj = Image.open(fullpath)
	cropped  = imageObj.crop((190,80,590,380))
	cropped.save("cropped_" + filename)
camera.stop_preview()
