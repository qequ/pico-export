from tkinter import filedialog
from tkinter import *
from PIL import Image
import re
import math
import os

##options
exportsprites=0
exportspritesheet=1
exportmap=1

##load cart file
root = Tk()
root.withdraw()
cart_path = filedialog.askopenfilename(initialdir = "/",title = "Select cart",filetypes = (("PICO-8 files (.p8)","*.p8"),))

cart_file = open(cart_path, 'r')
cart_data = cart_file.read()
cart_file.close()

##split cart data into sections based on content
cart_data = re.split(r'__lua__|__gfx__|__label__|__gff__|__map__|__sfx__|__music__', cart_data)
map_data = cart_data[5].replace('\n','')
gfx_data = cart_data[2].replace('\n','')

##convert map data to integer format, place in 2d array
map_array = [[0 for x in range(128)] for y in range(64)]

x=0
y=0
for i in range(0,len(map_data),2):
    tile_hex = map_data[i] + map_data[i+1]
    tile_int = int(tile_hex, 16)
    map_array[y][x] = tile_int

    if x >= 127:
        y += 1
        x = 0
    else:
        x += 1
x=0
y=32
for i in range(math.floor(len(gfx_data)/2),len(gfx_data),2):
    tile_hex = gfx_data[i+1] + gfx_data[i]
    tile_int = int(tile_hex, 16)
    map_array[y][x] = tile_int

    if x >= 127:
        y += 1
        x = 0
    else:
        x += 1

##define colors
colors = [[0,0,0],[29,43,83],[126,37,83],[0,135,81],[171,82,54],[95,87,79],[194,195,199],[255,241,232],[255,0,77],[255,163,0],[255,236,39],[0,228,54],[41,173,255],[131,118,156],[255,119,168],[255,204,170]]

##reading spritesheet
gfx_img = Image.new('RGB',(128,128),'black')
pixels = gfx_img.load()
y=0
x=0

for char in gfx_data:
    color_int = int(char,16)

    if (x >= 127):
        y += 1
        x = 0
    else:
        color_rgb = colors[color_int]
        pixels[x,y] = (color_rgb[0], color_rgb[1], color_rgb[2])
        x+=1
if exportspritesheet:
    gfx_img.save('gfx.png')

##seperate into sprites
x=0
y=0

sprites = []
if not os.path.exists('sprites/') and exportsprites:
    os.makedirs('sprites/')

for i in range(0,2048,8):
    x = i%128
    y = math.floor(i/128)*8
    spr_image = gfx_img.crop((x,y,x+8,y+8))
    sprites.append(spr_image)
if exportsprites:
    for index, spr in enumerate(sprites):
        spr.save('sprites/{}.png'.format(index),'PNG')

##combine sprites to create map image
map_image = Image.new('RGB',(1024,512),'black')
for yindex, lines in enumerate(map_array):
    for xindex, tile in enumerate(lines):
        map_image.paste(sprites[tile],(xindex*8,yindex*8))
if exportmap:
    map_image.save('map.png','PNG')
