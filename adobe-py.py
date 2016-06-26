#!/usr/bin/env python
import argparse
import os
import json
from transform_image import map_perspective
import cv2

# contruct + parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument('-c', '--config', help = 'config file for processing')
ap.add_argument('-i', '--inputs', help = 'input file for processing')
args = vars(ap.parse_args())

config_file = args['config']
inputs = args['inputs']

def perspective_map(options):
    base = options['base']
    output = options['output']
    coords = options['coords']

    map_perspective(base, inputs, coords, output)
    os.system('convert ' + output + ' -transparent black ' + output)
    os.system('convert ' + base + ' ' + output + ' -gravity center -composite ' + output)


def resize_position(options):
    base = options['base']
    output = options['output']
    width = options['width']
    os.system('convert -resize ' + str(width) + 'x ' + inputs + ' ' + output)

    position = ''
    geometry = ''
    positionX = options['positionX']
    positionY = options['positionY']

    if positionX == 'center' and positionY == 'center':
        position = '-gravity center'
        offsetX = options.get('offsetX', 0)
        offsetY = options.get('offsetY', 0)
        geometry += '-geometry +' + str(offsetX) + '+' + str(offsetY)
        position += ' ' + geometry
    else:
        position = '-geometry ' + ' +' + str(positionX) + '+' + str(positionY)

    input1 = base
    input2 = output
    extra_options = ' '

    if options.get('rotate', False):
        os.system('convert -rotate ' + str(options['rotate']) + ' ' + str(output) + ' ' + str(output))

    if options.get('overlay_base', False):
        image = cv2.imread(base)
        height = image.shape[0]
        width = image.shape[1]
        position = '-geometry +0+0'

        temp_canvas = './output/temp_canvas.png'
        os.system('convert -size ' + str(width) + 'x' + str(height) + ' xc:white ' + temp_canvas)
        os.system('convert ' + temp_canvas + ' ' + output + ' -gravity center ' + geometry + ' -composite ' + output)
        os.system('rm ' + temp_canvas)

        input1 = output
        input2 = base

    os.system('convert ' + input1 + ' ' + input2 + ' ' + position + ' -composite ' + output)


with open(config_file) as data:
    config = json.load(data)


for cfg in config:
    if cfg['type'] == 'perspective_map':
        perspective_map(cfg)
    elif cfg['type'] == 'resize_position':
        resize_position(cfg)
    else:
        print 'NO VALID ACTION FOUND'
