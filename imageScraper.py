from pylab import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import random
import time
from scipy.misc import imread
from scipy.misc import imresize
import matplotlib.image as mpimg
import os
from scipy.ndimage import filters
import urllib
from os import listdir
from PIL import Image

"""
This is an image scraper used to download images from a new line separated list of actors that should be added
under a file named 'subset_actors.txt'

The database that this is getting it from is FaceScrub.

The script will download all available pictures on the given subset for each actor.
"""

act = list(set([a.split("\n")[0] for a in open("subset_actors.txt").readlines()]))


def rgb2gray(rgb):
    ''' Return the grayscale version of the RGB image rgb as a 2D numpy array
    whose range is 0..1
    Arguments:
    rgb -- an RGB image, represented as a numpy array of size n x m x 3. The
    range of the values is 0..255
    '''
    r, g, b = rgb[:,:,0], rgb[:,:,1], rgb[:,:,2]
    gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
    return gray/255.


def timeout(func, args=(), kwargs={}, timeout_duration=1, default=None):
    '''From:
    http://code.activestate.com/recipes/473878-timeout-function-using-threading/'''
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None

        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = default

    it = InterruptableThread()
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return False
    else:
        return it.result

testfile = urllib.URLopener()


#Creates directory if it does not exist
if not os.path.isdir("uncropped/"):
    os.makedirs("uncropped/")

for a in act:
    name = a.split()[1].lower()
    i = 0
    for line in open("faces_subset.txt"):
        if a in line:
            filename = name+str(i)+'.'+line.split()[4].split('.')[-1]
            #A version without timeout (uncomment in case you need to
            #unsupress exceptions, which timeout() does)
            #testfile.retrieve(line.split()[4], "uncropped/"+filename)
            #timeout is used to stop downloading images which take too long to download
            timeout(testfile.retrieve, (line.split()[4], "uncropped/"+filename), {}, 30)
            if not os.path.isfile("uncropped/"+filename):
                continue

            print filename
            try:
				img = Image.open('uncropped/'+filename) # open the image file
				img.verify() # verify that it is, in fact an image
            except (IOError, SyntaxError) as e:
				print('Bad file removed:', filename) # print out the names of corrupt files
				os.remove('uncropped/'+filename)
            i += 1


#Creates directory if it does not exist
if not os.path.isdir("cropped/"):
    os.makedirs("cropped/")

for filename in os.listdir('uncropped/'):
	try:
		im = imread(filename)
		img = rgb2gray(im)
		crop_face = img[int(croparea[1]):int(croparea[3]), int(croparea[0]): int(croparea[2])]
		res = imresize(crop_face,(32, 32))
		imsave("cropped/"+filename, res)
	except:
		print("Couldn't read the file " + filename)
