# PyPI(Python Package Index) a centralized repository maintained by Packaging Working Group
# all python roads lead to PyPI
# creates projects, files managed by users
# dependency is a phenomenon that appears everytime youre going to use a piece of software that
    # relies on other software, and may include multiple levels of software development
    # a certain package needs another certain package to work
# dependency hell: the process of arduously fulfilling all the subsequent requirements
# pip takes care of all the dependencies. it can discover, identify, and resolve all dependencies

# pip help install
    # detailed info about using and parameterizing the install command
# pip list
    # what python packages have been installed
# pip show package_name
    # more details of any installed package
    # pip show pip
    # would list summary, author, location in local directory, requires(what other packages are required for this one)
    # and required-by(which other packages need this package)
# pip uses internet to search for the packages
# pip search anystring
    # anystring can either be names of the packages or their summary
# pip install pygame
    # or pip install --user pygame: you add --user to install only locally and are not the admin
# pip install has two important abilities
    # pip install -U package-name: U for Update. it updates the package and makes sure you're using the latest version of the package
    # pip install package_name==package_version: if you want to install a user-selected version
        # e.g. pip install pygame==1.9.2 (a specific version)
# pip uninstall package_name: to unistall the package
    # pip uninstall pygame
    # prompts while uninstalling (y/n)?


import pygame

run = True      # we start with run set to True
width = 400     # determines the windows size (height and width)
height = 100
pygame.init()   # initialize the environement
screen = pygame.display.set_mode((width, height))   # prepare the app window and set the size
font = pygame.font.SysFont(None, 48)    # make an object representing the default font size of 48
text = font.render("Welcome to pygame", True, (255, 255, 255))  # object representing the given text(anti-aliased = True, white color)
screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2)) # insert text in currently invisible screen buffer
pygame.display.flip()   # flips the screen buffers to make text visible
while run:
  for event in pygame.event.get():  # gets a list of all pending pygame events
   # checks if user has either closed the window, clicked somewhere inside, or pressed any key
   if event.type == pygame.QUIT\
   or event.type == pygame.MOUSEBUTTONUP\
   or event.type == pygame.KEYUP:
    run = False # when True, run is set to False

