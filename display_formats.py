from PIL import Image

#prints 3 images in horizontal orientation
#used for Void triptych
def three_images_in_row(image_list):
    im1=image_list[0]
    im2=image_list[1]
    im3=image_list[2]

    dst = Image.new('RGB', (100+im1.width + 100+ im2.width +100+ im3.width+100, im1.height+200))
    dst.paste(im1, (100, 100))
    dst.paste(im2, (100+im1.width+100, 100))
    dst.paste(im3, (100+im1.width+100+im2.width+100, 100))
    return dst

#prints 4 images in horizontal orientation
#used for Fragments
def four_images_in_row(image_list):
    im1=image_list[0]
    im2=image_list[1]
    im3=image_list[2]
    im4=image_list[3]

    dst = Image.new('RGB', (100+im1.width + 100+ im2.width +100+ im3.width+100+ im4.width+100, im1.height+200))
    dst.paste(im1, (100, 100))
    dst.paste(im2, (100+im1.width+100, 100))
    dst.paste(im3, (100+im1.width+100+im2.width+100, 100))
    dst.paste(im4, (100+im1.width+100+im2.width+100+im3.width+100, 100))
    return dst

#prints images in adjustable square grid
def adjustable_squares(im_list,dim):
  h=im_list[0].height
  w=im_list[0].width

  dimension=int(dim)
  
  dst = Image.new('RGB', (((dimension+1)*100+w*dimension, (dimension+1)*100+h*dimension)))
  position=0
  for i in range(0,dimension): #width
    for j in range(0,dimension): #height
      dst.paste(im_list[position], ((i+1)*100+w*i, (j+1)*100+h*j))
      position+=1

  return dst

#prints images in adjustable square grid
def adjustable_squares_noInnerBorder(im_list,dim):
  h=im_list[0].height
  w=im_list[0].width

  dimension=int(dim)
  
  dst = Image.new('RGB', ((200+w*dimension, 200+h*dimension)))
  position=0
  for i in range(0,dimension): #width
    for j in range(0,dimension): #height
      dst.paste(im_list[position], (100+w*i, 100+h*j))
      position+=1

  return dst
