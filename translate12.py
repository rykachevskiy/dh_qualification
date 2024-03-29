import json
import sys

if __name__ == "__main__":
	dict_f = open("./english_german.json", encoding='utf8')
	dict_ = json.load(dict_f)
	dict_f.close()

	#with open(args.i + "/input.txt") as f:
	#	lines = [x[:-1] for x in f.readlines()]
	translation = []
	for l in sys.stdin:
		l = l[:-1]
		words = []
		for w in l.split(" "):
			if w in dict_:
			    words.append(dict_[w])
			else:
			    words.append(w)
		words.append(u"\n")
		translation.append(" ".join(words))

	#for l in translation:
	#	print(l.encode('utf-8'))
	
	with open("/output/output.txt", 'wb') as f:
                for l in translation:
                        f.write(l.encode('utf-8'))
