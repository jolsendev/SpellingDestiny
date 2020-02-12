import os
import random
from pathlib import Path

current_dir = os.getcwd()
base = Path(current_dir, "Words")
spelling_word_files = ["3rd_grade.txt","4th_grade.txt","5th_grade.txt","6th_grade.txt"]
word_holder = []
for file in range(len(spelling_word_files)):
	new_file_name = "weekly_word5"	
	word_file = open(Path(base,spelling_word_files[file]),"r")
	new_file = open(Path(base,new_file_name),"a") 
	if file == 0:
		word_count = 10
		new_file.write("----- Common -----\n")
	if file == 1:
		word_count = 5
		new_file.write("----- Uncommon -----\n")
	if file == 2:
		word_count = 3
		new_file.write("----- Heroic -----\n")
	if file == 3:
		word_count = 2
		new_file.write("----- Legendary -----\n")

	
	word_array = []

	for word in word_file:
		word_array.append(word)

	for i in range(word_count):
		considered_word = word_array[random.randrange(len(word_array))]
		if considered_word in word_holder:
			considered_word = word_array[random.randrange(len(word_array))]
		new_file.write(considered_word)
		word_holder.append(considered_word)
	new_file.write("\n\n")