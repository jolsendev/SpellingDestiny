from spelling_utility import *
from pathlib import Path
import os


def update_spelling_words():
	current_dir = os.getcwd()
	base = Path(current_dir, "SpellingDestiny\\SpellingDestiny\\Words")
	spelling_word_files = ["6th_grade.txt","5th_grade.txt","4th_grade.txt","3rd_grade.txt"]
	for file in range(len(spelling_word_files)):
		# for each file - read each word and compare against the base file(s)
		word_file = open(Path(base,spelling_word_files[file]),"r")
		new_file_name = "new_"+spelling_word_files[file]
		new_file = open(Path(base,new_file_name),"a") 
		for f in range(file,len(spelling_word_files)):
			if spelling_word_files[f] != spelling_word_files[file]:
				for word in word_file:			
					if is_word_in_file(Path(base,spelling_word_files[f]), word) == False:
						# Write out each word that is not in the base file(s) into a new file 
						new_file.write(word)
						# prefixed with the current file

update_spelling_words()