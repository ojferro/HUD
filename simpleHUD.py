from PIL import Image
import cv2
import numpy as np
import glob
import time
import math

output_size=(800,800)
base_path="layers/"
# base_path="C:/Users/t-oferro/OneDrive - University of Waterloo/PhotoshopHuD/"

background = Image.open(base_path+'0layer_Backgroung.png').resize(output_size, Image.BILINEAR)
output_image = Image.open(base_path+'0layer_Backgroung.png').resize(output_size, Image.BILINEAR)

# All layers (incl. background) must be called Xlayer_<name>.png where X=order (back to front)
layers = glob.glob("/mnt/c/Users/t-oferro/OneDrive - University of Waterloo/PhotoshopHuD/*layer*.png")
overlays = {}
for i, l in enumerate(layers[1:]):
    overlays[i+1] = Image.open(l).resize(output_size, Image.BILINEAR)
speeds={
    1: 0.1,
    2: -1,
    3: 0.8,
    4: 1.1,
    5: -0.2,
    6: 0.4
}
counter = 0
while True:
    output_image = background
    for i in overlays:
        r,g,b,a = overlays[i].split()
        bgra = Image.merge("RGBA", (b,g,r,a))
        output_image = Image.alpha_composite(output_image, bgra.rotate(i*counter*speeds[i]))

    cv2.imshow("output", np.array(output_image))
    cv2.waitKey(15)
    counter += 1
    # time.sleep(0.1)

# output_image = Image.alpha_composite(output_image, overlays[1])
print("Done {}".format(l.split('/')[-1]))

# background.save(base_path+"overlayed_imgs.png", "PNG")
output_image.resize(output_size, Image.BILINEAR).show()