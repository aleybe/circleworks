import imageio, os
import math
from circlecalc import * 
from PIL import Image, ImageFont, ImageDraw, ImageEnhance

#first test draw based off circle data.

# newImage = Image.new('RGBA', (400, 400), "white")


#PIL.ImageDraw.ImageDraw.line(xy, fill=None, width=0)
#xy – Sequence of either 2-tuples like [(x, y), (x, y), ...] or numeric values like [x, y, x, y, ...].
#xy will have to contain details from circlecalc.circleObjects.AnglePoints()

#First - 
#Get potential x,y locations from the AnglePoints

firstCircleDetails = circleObjects(200, 200, 100)
drawPointsAvailable = firstCircleDetails.AnglePoints(2)

filenumber = 0 
imagelist = []

for eachPoint in drawPointsAvailable:
    filenumber+=1
    newImage = Image.new('RGBA', (400, 400), "black")
    drawCircle = ImageDraw.Draw(newImage)
    drawCircle.ellipse([(eachPoint[0]-20, eachPoint[1]-20), eachPoint], f"rgb({int(math.ceil(eachPoint[0]))},{int(math.ceil(eachPoint[1]))},125)", f"rgb({int(math.ceil(eachPoint[0]))},{int(math.ceil(eachPoint[1]))},125)")
    newImage.save(f"./saves/png/{filenumber}.png", "PNG")
    imagelist.append(f"./saves/png/{filenumber}.png")

png_dir = './saves/png/'
images = []

# for file_name in os.listdir(png_dir):
#     if file_name.endswith('.png'):
#         file_path = os.path.join(png_dir, file_name)

for frame in imagelist:
    images.append(imageio.imread(frame))

# print(imagelist)
imageio.mimsave('./saves/gif/movie.gif', images)



