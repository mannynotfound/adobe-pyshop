# adobe-pyshop

adobe-pyshop is a batch image processor similiar to Adobe Photoshop's "batch automate" function. Templates
are created inside a config file and then a single image or group of images is run through all the templates.

## dependencies

* [ImageMagick](http://stackoverflow.com/questions/7053996/how-do-i-install-imagemagick-with-homebrew/27862954#27862954)
* [cv2 for python](http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/)

## usage

Set up a `.json` file like so:

```js
[
  {
    "base": "./images/billboard.png",
    "output": "./output/billboard_final.png",
    "type": "perspective_map",
    "coords": "[(135, 140), (462, 30), (488, 256), (97, 328)]",
    "fit": "stretch"
  },
  {
    "base": "./templates/10x10CM_Oak.png",
    "output": "./output/framed_oak_final.png",
    "type": "resize_position",
    "width": 485,
    "positionX": "center",
    "positionY": "center"
  },
]
```

## templates

#### perspective_map

applies a perspective warp to the input and then maps it to the coordinates provided

#### resize_position

resizes the input image and then positions it at the values provided

```bash
python adobe-py.py -c ./batch.json -i images/subway.jpg
```

