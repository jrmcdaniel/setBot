from PIL import Image
import random

from display_formats import three_images_in_row,adjustable_squares,adjustable_squares_noInnerBorder,four_images_in_row
from project_methods import make_image

#address to pull 
loc='https://media.artblocks.io/'

#define discord channels
channel={
  889676076190683209:'Alexis-Andre',
  912755231866114099:'Dmitri-Cherniak',
  912820078871978024:'Kjetil-Golid',
  912831891390992464:'Monica-Rizzolli',
  913647091035832340:'Aaron-Penne',
  913648473839128656:'Snowfro'
}

#project_sorter listens to channel and sorts set requests
def project_sorter(channelid, msg):
  channel_choice=channel[channelid]
  print('Channel selection in sorter function: %s' %channel_choice)

  if(channel_choice=='Alexis-Andre'):
    from project_maps import triptych,triptych_crossref
    from project_methods import user_palette
    
    #define image scaling factor
    scale = 0.5

    #select palette based on user feedback
    palette=user_palette(msg,triptych)

    #select void
    if(len(triptych[palette][0])>0):
      void_select=random.choice(triptych[palette][0])
    else:
      print('Void palette reselect')
      void_list=[]
      for i in range(0,len(triptych_crossref[palette])):
        void_list.extend(triptych[triptych_crossref[palette][i]][0])
      void_select=random.choice(void_list)
    
    #select messenger
    if(len(triptych[palette][1])>0):
      mess_select=random.choice(triptych[palette][1])
    else:
      print('Mess palette reselect')
      mess_list=[]
      for i in range(0,len(triptych_crossref[palette])):
        mess_list.extend(triptych[triptych_crossref[palette][i]][1])
      mess_select=random.choice(mess_list)
    
    #select obicera
    if(len(triptych[palette][2])>0):
      obi_select=random.choice(triptych[palette][2])
    else:
      print('Obi palette reselect')
      obi_list=[]
      for i in range(0,len(triptych_crossref[palette])):
        obi_list.extend(triptych[triptych_crossref[palette][i]][2])
      obi_select=random.choice(obi_list)

    #add project numbers
    void_select=void_select+42000000
    mess_select=mess_select+68000000
    obi_select=obi_select+130000000

    image_list=[void_select,mess_select, obi_select]

    triptych=three_images_in_row(make_image(loc,image_list,scale))
    return triptych


  elif(channel_choice=='Dmitri-Cherniak'):
    from project_methods import user_dimension

    #define default image scaling
    scale = 0.5

    #allow user to select grid size
    dim=user_dimension(msg)

    #select random and unique ringers to populate grid
    numImages=int(dim)**2
    print('Selected images: %s' %numImages)
    number_list= random.sample(range(13000000, 13001000), numImages)
        
    grid=adjustable_squares(make_image(loc,number_list,scale), dim)
    
    return grid



  elif(channel_choice=='Kjetil-Golid'):
    from project_maps import armada
    from project_methods import user_palette

    project_num=37000000
    
    #define image and grid size
    dim=3
    scale = 0.5
    
    #pull images
    numImages=int(dim)**2
    
    #user select palette and random orientation
    orientation=random.choice([0,1])
    palette=user_palette(msg,armada)
    
    print('Aramada palette: %s' %(palette))
    print('Aramada orientation: %s' %(orientation))
    
    #Create list of ships to avoid duplication
    number_list= random.sample(armada[palette][orientation][1], 9)

    #Determine if there is a mothership or swarm available
    if(len(armada[palette][orientation][0])>0):
      number_list[4]= random.choice(armada[palette][orientation][0])

    number_list = [x+project_num for x in number_list]

    #Pull images and build grid
    grid=adjustable_squares(make_image(loc,number_list,scale), dim)
    
    return grid




  elif(channel_choice=='Monica-Rizzolli'):
    from project_maps import fragments
    from project_methods import user_palette
    
    project_num=+159000000
    
    #image and grid size
    dim=2
    scale = 0.25
    
    #select a random image from each season
    number_list= [
      random.choice(fragments['spring']),
      random.choice(fragments['summer']),
      random.choice(fragments['autumn']),
      random.choice(fragments['winter'])
    ]

    #let user choose storm, blues, pinks
    palette=user_palette(msg,fragments)
    if(palette=='storm'):
      number_list[1]=random.choice(fragments['storm'])
    elif(palette=='pinks'):
      number_list[1]=random.choice(fragments['pinks'])
    elif(palette=='blues'):
      number_list[2]=random.choice(fragments['blues'])
    else:
      pass

    print('Selection list Sp:%s, Su:%s, Au:%s, Wn:%s' %(number_list[0],number_list[1],number_list[2],number_list[3]))
    
    number_list = [x+project_num for x in number_list]

    #Pull images and assemble grid
    grid=four_images_in_row(make_image(loc,number_list,scale))
    
    return grid




  elif(channel_choice=='Aaron-Penne'):
    from project_maps import apparitions
    from project_methods import user_palette,configuration_possibles,configuration_selector
    
    project_num=28000000
    
    #define grid size and scaling factor
    dim=3
    scale = 0.25
    
    #user select palette or use random default
    palette=user_palette(msg,apparitions)
    
    print('Apparitions palette: %s' %(palette))
  
    #Create list of apps to avoid duplication
    #select grid composition to reflect palette
    num_dark=len(apparitions[palette][0])
    num_light=len(apparitions[palette][1])

    configuration=configuration_possibles(num_dark,num_light)
    number_list=configuration_selector(apparitions,palette,configuration)
    print('Apparitions configuration: %s' %configuration)

    number_list = [x+project_num for x in number_list]

    #Pull images and build grid
    grid=adjustable_squares(make_image(loc,number_list,scale), dim)
    
    return grid


  elif(channel_choice=='Snowfro'):
    from project_methods import user_dimension
    
    #define default image scaling
    scale = 0.5

    #allow user to select grid size
    dim=user_dimension(msg)

    #select random and unique squiggles to populate grid
    numImages=int(dim)**2
    print(numImages)
    number_list= random.sample(range(0, 9232), numImages)
    image_list=[]

    #pull images  
    grid=adjustable_squares_noInnerBorder(make_image(loc,number_list,scale), dim)
    
    return grid


  else:
    print('Not a mapped channel')