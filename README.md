# pico-export
Python script to export PICO-8 maps, spritesheets, and individual sprites!

The script has some options at the beginning to choose what you want to export:
```python
exportsprites=0
exportspritesheet=1
exportmap=1
```
By default, this script **does not** export individual sprites, only the full spritesheet and map image. To export individual sprites, change the value of exportsprites to 1.

# Dependencies
This script uses default python packages, with the exception of Pillow, a fork of the Python Imaging Library.
Pillow is used to write and export the images, and can be installed with ```pip install pillow```.
