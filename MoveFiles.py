import os, fnmatch, csv, re

dog_match_string = 'dog*'
cat_match_string = 'cat*'

count = 0

for file in os.listdir('.'):
  if count < 400:
    if fnmatch.fnmatch(file, dog_match_string):
      destination = './dogs/dogs/' + file
      os.rename(file, destination)
      print file
      print destination

    if fnmatch.fnmatch(file, cat_match_string):
      destination = './cats/cats/' + file
      # os.rename(file, destination)
      print file
      print destination

  else:
    if fnmatch.fnmatch(file, dog_match_string):
      destination = './dogs/' + file
      os.rename(file, destination)
      print file
      print destination

    if fnmatch.fnmatch(file, cat_match_string):
      destination = './cats/' + file
      os.rename(file, destination)
      print file
      print destination
  count += 1