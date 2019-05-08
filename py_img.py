
#import matplotlib.image as mlimg;
import matplotlib.pyplot as plt;
import math;
from PIL import Image, ImageDraw;
import py_util;

#
#
def load_img(file_path):
    try:
        img = Image.open(file_path);#mlimg.imread(str(file_path));
    except IOError as err:
        print("load_img failed: ", err);
    else:
        return img;

    return None;

def resize_img(img, width, height):
    return img.resize((width, height));

def rotate_img(img, angle):
    return img.rotate(angle, expand = True);

def thumbnailize_img(img, width, height):
    img.thumbnail((width, height), Image.ANTIALIAS);

def mask_regioin(img, polygon, outline_color, fill_color_RGBA):
    draw = ImageDraw.Draw(img, "RGBA");
    draw.polygon(polygon, outline = outline_color, fill = fill_color_RGBA);
    return img;

def show_images(img_list, row_num, col_num, title_list = [], show_axe = True):
    fig, axes = plt.subplots(row_num, col_num, squeeze = False)#, figsize = (5, 5))
    index = 0
    img_num = len(img_list)
    title_num = len(title_list)
    for row in axes:
        for axe in row:
            img = img_list[index]
            axe.imshow(img)
            axe.axis(show_axe and 'on' or 'off')

            if not index >= title_num:
                axe.set_title(title_list[index])
            index += 1
            if index >= img_num:
                return

def calc_row_col(total_num):
    sqrt_root = math.sqrt(total_num)
    row = math.floor(sqrt_root)
    col = math.floor(sqrt_root)
    
    while row * col < total_num:
        if row > col:
            col = col + 1;
        else:
            row = row + 1;

    return row, col;

##
# Parse image materials
# Given that all images with the same type are stored in the same folder with the type name.
##

def parse_img_folder(path, max_width, max_height):
    file_list = traverse_folder(path);
