from PIL import Image

#useful reference: https://note.nkmk.me/en/python-opencv-pillow-image-size/

import time
import os
import json
from glob import glob


FRAME_DIR = 'frames'

matrix_arr = []

#openCV might be a better alternative than pillow (PIL) for the intuition of treating
#the frames as regular, 2 dimensional lists 

#Get number of files in the directory with os dir 
fileList = glob(os.path.join(FRAME_DIR,'*.png'))


#the size of an image is 480x360

totalFiles = len(fileList)
i = 0

#These constants decide how the bad apple frames get compressed/downsized.
#If you truly want the full size images using the provided mp4 and
#the ffmpeg command provided, then delete the ".resize((WIDTH, HEIGHT))" part below 
WIDTH = 36
HEIGHT = 48

with open('input.txt', 'a+') as inp:
    for frame in glob(os.path.join(FRAME_DIR,'*.png')):
        
        progress = i / totalFiles
        print(f'\rProgress: {int(progress * 100)}% [{'#' * int(progress * 20) + ' ' * int((1-progress) * 20) + ']'}', end='', flush=True)
        i += 1


        with Image.open(frame).resize((WIDTH, HEIGHT)) as im:
            px = im.load()

        matrix = []

        #im.size returns (width, height). Rows influence height. Columns influence width 
        for r in range(im.size[1]): #for row and column instead of x y for images 
            row = []
            for c in range(im.size[0]):
                if px[c,r][0] < 125: #threshold for color or no color
                    row.append(0) #black
                    inp.write(str(0))
                else:
                    row.append(1) #white 
                    inp.write(str(1))
            matrix.append(row)
            inp.write('\n')
        matrix_arr.append(matrix)

# Save matrix
with open('BAframedata.json', 'w+') as f:
    json.dump(matrix_arr, f)

#I wish I could just smack these withs together but I was getting bugs so whatever

#This with statement is how you open the json and grab the data for use in your bad apple project
#You could also write a .txt reader and go in groups of HEIGHT rows by WIDTH columns 
with open("BAframedata.json", mode="r", encoding="utf-8") as f:#check sizes of the json to ensure everything loaded properly

    checkFile = json.load(f)
    print(f"\nCheck - Number of frames in json: {len(checkFile)}")
    print(f"Number of files in the frames folder: {totalFiles}")
    print(f"Check - length (number of rows) of first 2D array, should match HEIGHT: {len(checkFile[0])}")
    print(f"Check - length (number of rows) of first 2D array, should match WIDTH: {len(checkFile[0][0])}")
    

#https://realpython.com/python-json/ <-- reference for json opening 

