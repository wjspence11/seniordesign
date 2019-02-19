import PIL
import math
from PIL import Image

im = Image.open("picture.jpg","r").convert("RGBA");
px = im.load();

width, height =  im.size;

for x in range(width):
	for y in range(height):
		tuples = px[x,y];
		mean = math.sqrt(0.241* (tuples[0] ** 2) + 0.691* (tuples[1] ** 2) + 0.068* (tuples[2] ** 2));
		if (mean >= 204) :
			px[x,y] = (255,0,0);
		elif(mean > 76.5 and mean < 204):
			px[x,y] = (0,255,0);
		elif(mean <= 76.5):
			px[x,y] = (0,0,255);

im.show();
im.save("transformed.png");