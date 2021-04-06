from PIL import Image
import os
import time

new_image=Image.new(mode = "RGB", size = (600, 500), color = (255,255,255))
counter=1

for x in range(0,60):
    for y in range(0,50):
        filename = str(counter) + '.jpg'

        img=Image.open("60x50/"+filename)
        new_image.paste(img,(x*10,y*10))
        print("[+] Processing... ", str(x) , " " , str(y))
        counter += 1

new_image.show()
