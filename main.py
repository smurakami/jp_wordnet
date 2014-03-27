# coding: utf-8
import word_sim

if __name__ == "__main__":
    wn = word_sim.WordSim()
    wn.printSimilarity(u"飛行機", u"りんご")
    wn.printSimilarity(u"メロン", u"りんご")
    wn.printSimilarity(u"警察", u"りんご")
    wn.printSimilarity(u"自動車", u"りんご")
    wn.printSimilarity(u"自動車", u"警察")


