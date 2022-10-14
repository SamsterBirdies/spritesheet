'''
This script converts individual image files into a sprite sheet.
PIL is a required module.
prompt input = 0 arguments. argument mode = 1-6 arguments
argument usage: <filename> <iterations> <iterations_per_row> <extension> <offset> <result_appendication>
example usage: python spritesheet.py frame 2 1 .png 0 _sheet
'''

import sys, math
#dependency: Python Image Library
try:
	from PIL import Image, ImageDraw, ImageOps, ImageEnhance
except Exception:
	print("PIL not installed.\nInstall using command: python -m pip install pillow")
	exit(0)

#Default argument options
filename = "frame" #frame name format = {filename}{iteration}{extension}. example: explosion16.png
iterations = 2 #number of frames
iterations_per_row = 1 #number of frames per row. (horizontal width)
extension = ".png" #should start with the period
offset = 0 #number to start with. (animation frame numbers sometimes start with 1)
result_appendication = "_sheet" #result file name format = {filename}{result_appendication}{extension}. example: explosion_sheet.png

#arg gather
if len(sys.argv) > 1:
	filename = sys.argv[1]
else:
	filename = input("Base filename:")
	iterations = int(input("Iterations:"))
	iterations_per_row = int(input("Iterations per row:"))
	extension = input("Source extension:")
	offset = int(input("Offset:"))
if len(sys.argv) > 2:
	iterations = int(sys.argv[2])
if len(sys.argv) > 3:
	iterations_per_row = int(sys.argv[3])
if len(sys.argv) > 4:
	extension = sys.argv[4]
if len(sys.argv) > 5:
	offset = int(sys.argv[5])
if len(sys.argv) > 6:
	result_appendication = sys.argv[6]

#setup
testimage = Image.open(f"{filename}{offset}{extension}")
framesize = testimage.size
result = Image.new(mode = "RGBA", size = (framesize[0] * iterations_per_row, framesize[1] * math.ceil(iterations / iterations_per_row)), color = (0,0,0,0))

#mainloop
for i in range(iterations):
	frame = Image.open(f"{filename}{i + offset}{extension}")
	result.paste(frame, (framesize[0] * (i % iterations_per_row), framesize[1] * math.floor(i / iterations_per_row)))

#saving
result.save(f"{filename}{result_appendication}{extension}", "PNG")