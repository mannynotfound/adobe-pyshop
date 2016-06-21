#!/usr/bin/env python
import argparse
import os
import json
from transform_image import map_perspective
from show import show_image

# contruct + parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-b', '--base', help = 'base image to be manipulated')
ap.add_argument('-i', '--inputs', help = 'input image to apply to base')
ap.add_argument('-c', '--coords', help = 'cords of where to place input')
ap.add_argument('-o', '--output', help = 'results output path')
ap.add_argument('-ba', '--batch', help = 'config file for batch processing')
args = vars(ap.parse_args())

batch = args['batch']

def mask_image(base, inputs, coords, output):
    map_perspective(base, inputs, coords, output)
    os.system('convert ' + output + ' -transparent black ' + output)
    os.system('convert ' + base + ' ' + output + ' -gravity center -composite ' + output)

if batch:
    with open(batch) as data:
        config = json.load(data)

        for cfg in config:
            b = cfg['base']
            i = cfg['inputs']
            c = cfg['coords']
            o = cfg['output']
            mask_image(b, i, c, o)

    # run through config file
else:
    b = args['base']
    i = args['inputs']
    c = args['coords']
    o = args['output']
    mask_image(b, i, c, o)



