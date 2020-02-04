def is_word_in_file(file, word):
		f = open(file,"r")		
		for x in f:
			if x == word:
				return True;
		return False