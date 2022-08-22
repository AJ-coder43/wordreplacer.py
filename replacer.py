# define the replacer function here


# text = "This is one, one@ two !onem"
# punc = [This, is, one, one, two, onem]
# this = "one"
# that = "three"
# whole_word = false
# punc =[This, is, three, three, two ,onem]
def word_replacer(this, that, text, whole_word=True):
	import string
	punc = string.punctuation + ' '
 #punc = !@$^&*(())

	if not whole_word:						# not replacing whole words, let Python do it
		return text.replace(this, that)
		
	# TO DO: Only replace whole words. Be sure to check for punctuation on either end
	if whole_word == True:
		for i in range(len(punc)):
			if this == punc[i]:
				punc[i] = that
		result = ' '.join(punc)
		return result

