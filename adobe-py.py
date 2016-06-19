#!/usr/bin/env python
import argparse
import os
from transform_image import map_perspective
from show import show_image

# contruct + parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-b', '--base', help = 'base image to be manipulated')
ap.add_argument('-i', '--inputs', help = 'input image to apply to base')
ap.add_argument('-c', '--coords', help = 'cords of where to place input')
ap.add_argument('-o', '--output', help = 'results output path')
args = vars(ap.parse_args())

base = args['base']
inputs = args['inputs']
coords = args['coords']
output = args['output']

map_perspective(base, inputs, coords, output)

os.system('convert ' + output + ' -transparent black ' + output)
os.system('convert ' + base + ' ' + output + ' -gravity center -composite ' + output)

show_image(output)


