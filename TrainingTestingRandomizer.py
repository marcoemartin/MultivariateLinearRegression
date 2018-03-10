import os
import random

#Creates directory if it does not exist
if not os.path.isdir("Training/"):
    os.makedirs("Training/")

#Creates directory if it does not exist
if not os.path.isdir("Validation/"):
    os.makedirs("Validation/")

#Creates directory if it does not exist
if not os.path.isdir("Testing/"):
    os.makedirs("Testing/")

act = list(set([a.split("\n")[0] for a in open("subset_actors.txt").readlines()]))
for actor in act:
	actorname = actor.split(" ")[1]
	if not os.path.isdir("Training/"+actor+"/"):
	    os.makedirs("Training/"+actor+"/")

	if not os.path.isdir("Validation/"+actor+"/"):
	    os.makedirs("Validation/"+actor+"/")

	if not os.path.isdir("Testing/"+actor+"/"):
	    os.makedirs("Testing/"+actor+"/")

	actor_pics = []
	for filename in os.listdir('cropped/'):
		if actorname.lower() in filename:
			actor_pics.append(filename)
	size = len(actor_pics)
	#Make training ~80% of the available data
	#validation and testing the other ~20%
	vali_size = int(size*0.10)
	testing_size = int(size*0.10)

	if size <= 70:
		print "Warning: very few data is available for Validation and Testing, consider obtaining at least 100 photos for {}".format(actor)
	if vali_size < 1:
		vali_size = 1
	if testing_size < 1:
		testing_size = 1

	#Move 10% of random files to the Testing folder
	for i in xrange(testing_size):
  		index = random.randint(0, len(actor_pics)-1)
  		print "random num: {}  filename: {}".format(index, actor_pics[index])
  		filename = actor_pics[index]
  		os.rename("cropped/"+filename, "Testing/"+actor+"/"+filename)
  		del actor_pics[index]

	# #Move 10% of random files to the Validation folder
	for i in xrange(vali_size):
  		index = random.randint(0, len(actor_pics)-1)
  		filename = actor_pics[index]
  		os.rename("cropped/"+filename, "Validation/"+actor+"/"+filename)
  		del actor_pics[index]

	# #Move remaining 80% of files to the Training folder
	for filename in actor_pics:
  		os.rename("cropped/"+filename, "Training/"+actor+"/"+filename)
