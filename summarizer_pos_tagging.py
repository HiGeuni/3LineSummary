from modules.crawler import getNewsContent
from modules.textRank import *

def summarize_contents(x):
    tr = TextRank()

    stopword = set([('있', 'VV'), ('하', 'VV'), ('되', 'VV') ])
    tr.loadSents(RawSentence(x), lambda sent: filter(lambda y:y not in stopword and y[1] in ('NNG', 'NNP', 'VV', 'VA'), tagger.pos(sent)))
    
    tr.build()
    ranks = tr.rank()
    return tr.summarize(0.2)

if __name__ == "__main__":
    print("Select Mode - 1 : News, 2 : Custom Text")
    mode = int(input())
    if mode == 1:
        print("Input Url : ", end='')
        url = input()
        try:
            content = getNewsContent(url)
            print(summarize_contents(content))
        except:
            pass
    else:
        print("Input Text all and input 'end' : ", end='')
        x = ''
        while True:
            s = input()
            if s == "end":
                break
            x += s
            
        print(summarize_contents(x))