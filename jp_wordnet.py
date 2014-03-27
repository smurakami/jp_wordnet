# coding: utf-8
from nltk.corpus.reader.wordnet import WordNetCorpusReader
import nltk
import os

class JapaneseWordNetCorpusReader(WordNetCorpusReader):
    def __init__(self):
        "データのロード"
        root = nltk.data.find('corpora/wordnet')
        cd = os.path.dirname(__file__)
        if cd == "":
            cd = "."
        filename = cd+'/wnjpn-ok.tab'
        WordNetCorpusReader.__init__(self, root)
        import codecs
        with codecs.open(filename, encoding="utf-8") as f:
            self._jword2offset = {}
            counter = 0
            for line in f:
                try:
                    _cells = line.strip().split('\t')
                    _offset_pos = _cells[0]
                    _word = _cells[1]
                    if len(_cells)>2: _tag = _cells[2]
                    _offset, _pos = _offset_pos.split('-')
                    self._jword2offset[_word] = {'offset': int(_offset), 'pos': _pos}
                    counter += 1
                except:
                    print "failed to lead line %d" % counter

    def synset(self, word):
        "synsetの取得"
        if word in self._jword2offset:
            return WordNetCorpusReader._synset_from_pos_and_offset(
                self, self._jword2offset[word]['pos'], self._jword2offset[word]['offset']
            )
        else:
            return None


if __name__ == '__main__':
    pass











