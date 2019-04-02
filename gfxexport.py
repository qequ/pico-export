import re
import PIL.Image
from tkinter import filedialog
from tkinter import *
 
root = Tk()
root.filepath =  filedialog.askopenfilename(initialdir = "/",title = "Select cartridge",filetypes = (("PICO-8 Files","*.p8"),("all files","*.*")))
cart_file = open(root.filepath, 'r')
cart_data = cart_file.read()
cart_file.close()

cart_data = re.split(r'__lua__|__gfx__|__gff__|__label__|__map__|__sfx__|__music__',cart_data)
map_data = cart_data[5]
gfx_data = cart_data[2].replace('\n','')

colors = [[0,0,0],[29,43,83],[126,37,83],[0,135,81],[171,82,54],[95,87,79],[194,195,199],[255,241,232],[255,0,77],[255,163,0],[255,236,39],[0,228,54],[41,173,255],[131,118,156],[255,119,168],[255,204,170]]
gfx_img = PIL.Image.new('RGB',(128,128),'black')
pixels = gfx_img.load()

x=0
y=0
for i in range(0,len(gfx_data)):
    if x>=127:
        x=0
        y+=1
    else:
        color_rgb = colors[int(gfx_data[i],16)]
        pixels[x,y] = (color_rgb[0], color_rgb[1], color_rgb[2])
        x+=1

gfx_img.save('gfx.png')
