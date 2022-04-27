#!/bin/bash

python encrypted_names.py
python random_generator.py

cat vote_list.txt | python mapper.py | sort -k1,1 | python reducer.py