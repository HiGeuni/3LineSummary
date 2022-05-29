from modules.crawler import getNewsContent
from modules.textRank_TFIDF import *

def summarize_contents(x):
    tr = TextRank() 
    token = tokenize(x)
    tr.loadSentence(token)

    tr.build()
    ranks = tr.get_rank()
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
