from spelling_utility import *
from pathlib import Path

spelling_word_files = ["4th_grade.txt","5th_grade.txt","6th_grade.txt"]
base_file = "3rd_grade.txt"
words_dir = "Words"
for file in spelling_word_files:
	print(Path(words_dir,file))
	is_word_in_file(Path(words_dir,base_file), "NOTZOO")