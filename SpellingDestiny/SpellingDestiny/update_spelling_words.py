from spelling_utility import *
from pathlib import Path

spelling_word_files = ["4th_grade.txt","5th_grade.txt","6th_grade.txt"]
base_file = "3rd_grade.txt"
words_dir = "Words"
for file in spelling_word_files:
	# for each file - read each word and compare against the base file(s)
	word_file = open(file,"r")
	for word in word_file:
		if is_word_in_file(Path(words_dir,base_file), word) == False:
			# Write out each word that is not in the base file(s) into a new file 
			new_file = open(word_file+"_new","w") 
			# prefixed with the current files name.