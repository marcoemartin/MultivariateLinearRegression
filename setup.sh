#!/bin/bash

if [! -f faces_subset.txt ]; then
	curl http://www.teach.cs.toronto.edu/~csc411h/winter/projects/proj1/facescrub_actors.txt >> faces_subset.txt
	curl http://www.teach.cs.toronto.edu/~csc411h/winter/projects/proj1/facescrub_actresses.txt >> faces_subset.txt
fi

if [ ! -f subset_actors.txt ]; then
    touch subset_actors.txt
fi
