#!/usr/bin/env bash

#base = $1
#input = $2
#output = $3
#coords = $4

python transform_image.py --base "$1" --image "$2" --output "$3" --coords "$4";

convert "$3" -transparent black "$3";

convert "$1" "$3" -gravity center -composite "$3";

python show.py --image "$3"




