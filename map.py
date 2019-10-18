from PIL import Image, ImageDraw
import math

im = Image.new('RGBA',(601,600), color=(0,0,0,255))
draw = ImageDraw.Draw(im)
im.save('image.png')

class Map:
    def __init__(self, file):
        self.file = file

    def read_file(self, file):
        with open(file) as text_file:
            text_contents = text_file.read() 

        elevations = [[int(each) for each in line.split()]
                      for line in text_contents.split("\n")]

        min = elevations[0][0]
        max = elevations[0][0]
        print("hi")

        for each in elevations:
            for integer in each:
                if integer < min:
                    min = integer
                if integer > max:
                    max = integer

        colors_big_list = []
        little_rows_of_colors = []

        for rows in elevations:
            for number in rows:
                color_int = round(((number - min) / (max-min)) * 255)
                little_rows_of_colors.append(color_int)
        colors_big_list.append(little_rows_of_colors)
        little_rows_of_colors = []

if __name__ == "__main__":
    map = Map("elevation_small.txt")       


    

 

for each

