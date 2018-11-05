import cv2
import numpy as np 

img_size = 512
num_images = 25000




for i in range(num_images):

	img = np.zeros((img_size, img_size), np.uint8)

	center_x = np.random.randint(100,400)
	center_y = np.random.randint(100,400)

	a = np.random.randint(70, min(center_x-20, 490-center_x,490-center_y, center_y-20 ))
	b= np.random.randint(70, min(center_y-20, 490-center_y, 490-center_x, center_x-20))

	orientation = np.random.randint(0, 180)

	img = cv2.ellipse(img, (center_x, center_y), (a,b), orientation, 0 ,360, 255, -1)

	data_img_name = "Ellipse/image"+str(i)+".png"

	cv2.imwrite(data_img_name, img)


