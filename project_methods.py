from PIL import Image
import requests
import random

#many artblocks images have differing dimensions
#use first image to define image dimension then
#map onto the remaining images
def make_image(loc,numlist,half):
  count=0
  size=[]
  image_list=[]
  for number in numlist:
    im=Image.open(requests.get(loc+str(number)+'.png', stream=True).raw)
    if(count==0):
      size=[int(half * s) for s in im.size]
      count=1
    im=im.resize( size )
    image_list.append(im)
  return image_list



def user_palette(msg,project):
  
  #set default palette to be random
  palette=random.choice(list(project))
  
  #rewrite default with user selected palette
  if(len(msg.split())>1):
    userPalette=''.join([str(elem) for elem in msg.lower().split()[1:]])
    print('User selected: %s' %userPalette)
    if(userPalette in list(project)):
      palette=userPalette
    else:
      print('Not a valid palette selection')
    
    print('Palette: %s' %palette)
  return palette

#let user decide grid dimension if 5 or less
def user_dimension(msg):
  if(len(msg.split())>1):
    dim=msg.split()[1]
    if(int(dim)<6):
      return dim
    else:
      return 3
  else:
    return 3

#binary configurations for grouping palettes
#decides which configs are possible and randomly selects one
#designed for apparations
def configuration_possibles(a,b):
    configs=[]
    
    if((a>0)&(b>8)):
      configs.append('a_middle')
    if((a>8)&(b>0)):
      configs.append('b_middle')
    if(b>8):
      configs.append('b_all')
    if(a>8):
      configs.append('a_all')
    
    return random.choice(configs)

#build 3x3 grids with the selected configuration
#designed for apparitions
def configuration_selector(proj,palette,configuration):
      number_list=[]
      a=0
      b=1
      if(configuration=='b_all'):
        number_list= random.sample(proj[palette][b], 9)
      elif(configuration=='a_all'):
        number_list= random.sample(proj[palette][a], 9)
      elif(configuration=='b_middle'):
        number_list= random.sample(proj[palette][a], 9)
        number_list[4]=random.choice(proj[palette][b])
      elif(configuration=='a_middle'):
        number_list= random.sample(proj[palette][b], 9)
        number_list[4]=random.choice(proj[palette][a])
      return number_list