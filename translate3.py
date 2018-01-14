import json
import argparse


if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument('-i')
	parser.add_argument('-o')
	args = parser.parse_args()
	
	print(args.o + "/output.txt"

	dict_f = open("./english_german.json", encoding='utf8')
	dict_ = json.load(dict_f)
	dict_f.close()

	with open(args.i + "/input.txt") as f:
		lines = [x[:-1] for x in f.readlines()]

	translation = []
	for l in lines:
		words = []
	        print(l)
		for w in l.split(" "):
			if w in dict_:
			    words.append(dict_[w])
			else:
			    words.append(w)
		translation.append(" ".join(words))

	with open(args.o + "/output.txt", "w", encoding='utf8') as f:
		f.write("\n".join(translation))