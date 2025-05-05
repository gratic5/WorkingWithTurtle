import colorgram
from PIL import Image
from turtle import Turtle, Screen

def image_colour_scheme(abs_path_image):
    img = Image.open(abs_path_image)
    #absolute path of image
    #make the path a raw string with r"string"

    color_list = colorgram.extract(img, 2**32)
    colors = [(i.rgb.r,i.rgb.g,i.rgb.b) for i in color_list]
    return colors


def image_generator(number_of_dots,image):
    
    colors = image_colour_scheme(image)
    i = 0
    j = 0
    while i < number_of_dots:

        a1.dot(20,colors[j])
        a1.forward(50)

        i += 1
        if i % 10 == 0 and i != 0:
            a1.setpos((-300, (i // 10)*50-250))

        j += 1
        if j == len(colors):
            j = 0



input1 = input("type number of spots and image location: ")

a1 = Turtle()
a1.penup()
Screen().colormode(255)
a1.speed("fastest")
a1.setpos((-300,-250))


image_generator(int(input1.split(",")[0]),input1.split(",")[1])

a1.hideturtle()
screen = Screen()
screen.exitonclick()



