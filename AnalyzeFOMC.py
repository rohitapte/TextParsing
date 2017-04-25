import nltk
from nltk.corpus import PlaintextCorpusReader

def pos_features(word):
	features={}
	for suffix in common_suffixes:
		features['endswith({})'.format(suffix)] = word.lower().endswith(suffix)
	return features


corpus_root=r"C:\Users\user\OneDrive\Documents\Python Scripts\TextParsing\FOMC"
fed=PlaintextCorpusReader(corpus_root, '.*')
#print(fed.fileids())
suffix_fdist = nltk.FreqDist()
for word in fed.words():
	word=word.lower()
	suffix_fdist[word[-1:]]+=1
	suffix_fdist[word[-2:]]+=1
	suffix_fdist[word[-3:]]+=1
common_suffixes = [suffix for (suffix, count) in suffix_fdist.most_common(100)]
print(common_suffixes)
print(pos_features('received'))