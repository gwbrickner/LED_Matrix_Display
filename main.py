# Mrs. H found out how to connect to the board
# Worked on by: Ryan Stone, Aaron Spink, Dylan Stitt, Graeson Brickner

# To run:
    # cd to the file in terminal (use ls if you need a list of directories)
        # Note: You have to add single quotes around anything that has a space
    # sudo python3 WorkingLed.py
# To run again:
    # You can hit up arrow to retype run code

# Make An Import For Each File You Want Images From
    # Ex. from fileName import *
from Christmas_Images import *
from PIL import Image

from rpi_ws281x import *
import time


# Any Images That You Want Displayed Must Be Typed Here
IMAGES = [snowman2, tree, snowflake, present, star, candyCane2, candyCane1, snowman1, fire]
IMAGE_DELAY = 8


LED_COUNT = 256
LED_PIN = 18
LED_FREQ_HZ = 800000
LED_DMA = 10
LED_BRIGHTNESS = 255
LED_INVERT = False
LED_CHANNEL = 0


def boardOff(strip):
    for x in range(LED_COUNT):
        strip.setPixelColor(x, Color(0, 0, 0))
    strip.show()
    

def functionalList(listName):
        newList = []
        for x, row in enumerate(listName):
            if x % 2 == 1:
                newList.append(row)
            else:
                row.reverse()
                newList.append(row)
        return newList


def display(strip, image):
    counter = 0
    for row in image:
        for colorTuple in row:
            strip.setPixelColor(counter, Color(colorTuple[0], colorTuple[1], colorTuple[2]))
            counter += 1
    strip.show()


def main():
    strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
    strip.begin()

    image = Image.open("Sprite_heart.png")
    
    image = functionalList(image)
    
    while True:
        display(strip, image)


if __name__ == "__main__":
    main()