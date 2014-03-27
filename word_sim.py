# coding: utf-8
import jp_wordnet as JPWN

"""
類似度計算モジュール
"""

class WordSim(JPWN.JapaneseWordNetCorpusReader):
    def __init__(self):
        JPWN.JapaneseWordNetCorpusReader.__init__(self)
        self.cache = {} #計算を早くするために一度計算した結果を保存しておく

    def similarity(self, a, b):
        "類似度の計算"
        if not isinstance(a, unicode):
            a = unicode(a)
        if not isinstance(b, unicode):
            b = unicode(b)
        # キャッシュに保存するために順番を統一
        if a > b:
            a, b = b, a
        # キャッシュに結果がのこっていないか調べる
        if self.cache.has_key((a, b)):
            return self.cache[(a, b)]
        # 類似度の計算
        jsyn_a = self.synset(a)
        jsyn_b = self.synset(b)
        if jsyn_a and jsyn_b:
            sim = jsyn_a.path_similarity(jsyn_b)
        else:
            sim = None
        self.cache[(a, b)] = sim # キャッシュに結果の保存
        return sim

    def printSimilarity(self, a, b):
        "類似度の表示"
        sim = self.similarity(a, b)
        if sim != None:
            print "「"+a+"」と「"+b+"」の類似度:", sim
        else:
            print "「"+a+"」と「"+b+"」:辞書に無い単語を含みます"

if __name__ == "__main__":
    wn = WordSim()
    wn.printSimilarity(u"うどん", u"そば")
    wn.printSimilarity(u"うどん", u"りんご")
    wn.printSimilarity(u"うどん", u"くじら")
    wn.printSimilarity(u"みかん", u"りんご")
    wn.printSimilarity(u"メロン", u"りんご")
    wn.printSimilarity(u"自動車", u"りんご")
    wn.printSimilarity(u"ほあ", u"りんご")

