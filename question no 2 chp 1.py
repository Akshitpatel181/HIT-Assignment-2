# This program changes the pixel values of an image, and finds the sum of all red
# pixel values of the altered image.

import time
from PIL import Image

image = Image.open("chapter1.jpg")
pic = image.load() # opening image for alteration


## THIS SECTION IS TAKEN FROM THE TASK SHEET
current_time = int(time.time())

generated_number = (current_time % 100) + 50

if generated_number % 2 == 0:
    generated_number += 10
#------


for i in range(0, image.size[0]): # iterate through rows
    for j in range(0, image.size[1]): # iterate through columns
        # change each pixel by adding generated number
        pic[i,j] = (pic[i,j][0] + generated_number, pic[i,j][1] + generated_number, pic[i,j][2] + generated_number)


image.save("chapter1out.png") 

image = Image.open("chapter1out.png") 
pic = image.load()

sum = 0
for i in range(0, image.size[0]): # for rows
    for j in range(0, image.size[1]): # for columns
        sum += pic[i,j][0] # adding only red pixel values to sum 

print(sum)