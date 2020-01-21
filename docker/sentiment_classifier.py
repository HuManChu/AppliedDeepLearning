import fastai
from fastai.text import *

class SentitmentClassfier:
    def __init__(self):
        fastai.torch_core.defaults.device = 'cpu'
        self.learner = load_learner(path="./")


    # This method predicts the sentiment of the example text:
    def get_sentiment(self,txt):
        sentiment = self.learner.predict(txt)
        if int(sentiment[0]) == 0:
            output = f'Negative sentiment with {round(sentiment[2][0].data.tolist()*100,2)}% certainty'
        elif int(sentiment[0]) == 1:
            output = f'Positive sentiment with {round(sentiment[2][1].data.tolist()*100,2)}% certainty'
        else:
            output = f'Unclear'

        return output

def main():
    seperator = "-----------------------------------------"
    print(seperator)
    print(f'''
    >>>Sentiment Classifier App<<<
''')
    print(seperator)
    clf = SentitmentClassfier()
    print(">>enter exit() to end program")
    print(">>insert sentence (english):")
    print(seperator)
    txt = "start"
    while(True):
        txt = input()
        if(txt.strip() == "exit()"):
            print(seperator)
            print(">>END<<")
            break

        print(clf.get_sentiment(txt))
        print(seperator)


if __name__ == '__main__':    main()



