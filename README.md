# adobe-pyshop

## dependencies

* [ImageMagick](http://stackoverflow.com/questions/7053996/how-do-i-install-imagemagick-with-homebrew/27862954#27862954)
* [cv2 for python](http://www.pyimagesearch.com/2015/06/15/install-opencv-3-0-and-python-2-7-on-osx/)

## usage

Single masker:

```bash
python adobe-py.py -b "images/billboard.png" -i "images/subway.jpg" -c "[(135, 140), (462, 30), (488, 256), (97, 328)]" -o "images/lolpy.png"
```

Batch masker:

Set up a `.json` file like so:

```js
[
  {
    "base": "./images/billboard.png",
    "inputs": "./images/subway.jpg",
    "output": "./output/billboard_final.png",
    "coords": "[(135, 140), (462, 30), (488, 256), (97, 328)]"
  }
]
```

and then just run with `-ba` or `--batch`:

```bash
python adobe-py.py --batch ./batch.json
```

