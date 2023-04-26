!apt-get -y install fonts-ipafont-gothic

import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

fonts = fm.findSystemFonts()

def str2img(input_str, yoko_mojisuu, tate_mojisuu, moji_size):
  img  = Image.new('RGBA', (moji_size * yoko_mojisuu , moji_size * tate_mojisuu), 'white')
  draw = ImageDraw.Draw(img)
  myfont = ImageFont.truetype("fonts-japanese-gothic.ttf    /usr/share/fonts/truetype/fonts-japanese-gothic.ttf", moji_size)
  yoko_count = 0
  tate_count = 0
  for char in input_str:
    if tate_count >= tate_mojisuu:
      break
    draw.text( ( yoko_count * moji_size, tate_count * moji_size ), char, fill=(0, 0, 0), font = myfont)
    yoko_count +=1
    if yoko_count >= yoko_mojisuu:
      yoko_count =  0
      tate_count += 1

  return img

img = str2img("小森教授", 2, 3, 50)

def img2graylist(input_img):
  img_width, img_height = input_img.size

  result_graylist = []
  for y in range(0, img_height, 1):
    tmp_graylist=[]
    for x in range(0, img_width, 1):
      r,g,b, = input_img.getpixel((x,y))[0:3]
      g = (r + g + b)/3
      tmp_graylist.append(g)
    result_graylist.append(tmp_graylist)
  return result_graylist

def graylist2wblist(input_graylist):
  gray_sum_list = []
  for tmp_graylist in input_graylist:
    gray_sum_list.append( sum(tmp_graylist)/len(tmp_graylist) )
  gray_ave = sum(gray_sum_list)/len(gray_sum_list) 

  result_wblist = []
  for tmp_graylist in input_graylist:
    tmp_wblist = []
    for tmp_gray_val in tmp_graylist:
      if tmp_gray_val >= gray_ave:
        tmp_wblist.append(1)
      else:
        tmp_wblist.append(0)
    result_wblist.append(tmp_wblist)

  return result_wblist

def print2Dcharlist(charlist):
  for tmp_charlist in charlist:
    for char in tmp_charlist:
      print(char, end="")
    print()

# 0/1表記は漢字が潰れる
img = str2img("小森教授", 6, 1, 10)
graylist = img2graylist(img)
wblist = graylist2wblist(graylist)

def infinity_gen_str(str):
  for a in range(1000000000):
    for s in str:
        yield s
def wblist2wbcharlist(input_wblist, nakami_str, soto_str):
  gen_nakami_str =  infinity_gen_str(nakami_str)
  gen_soto_str =  infinity_gen_str(soto_str)
  result_wbcharlist = []
  for tmp_wblist in input_wblist:
    tmp_wbcharlist = []
    for tmp_wb_val in tmp_wblist:
      if tmp_wb_val == 1:
        tmp_wbcharlist.append( next(gen_soto_str))
      else:
        tmp_wbcharlist.append( next(gen_nakami_str) )

    result_wbcharlist.append(tmp_wbcharlist)

  return result_wbcharlist

# 表示する文字
img = str2img("我男好", 15, 1, 30)
graylist = img2graylist(img)
wblist = graylist2wblist(graylist)
# 上記の文字を表示する文字
wbcharlist = wblist2wbcharlist(wblist, "松田隼斗","　")
print2Dcharlist(wbcharlist)
