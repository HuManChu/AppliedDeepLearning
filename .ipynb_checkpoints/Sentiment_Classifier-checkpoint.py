# fastai
from fastai.text import nn

# transformers
from transformers import PreTrainedModel

'''
Just a wrapper around nn.Module to make the transformer work with the fast.ai library
Taken from: https://www.kaggle.com/maroberti/fastai-with-transformers-bert-roberta
'''


class Sentiment_Classifier(nn.Module):
    def __init__(self, transformer_model: PreTrainedModel):
        super(Sentiment_Classifier, self).__init__()
        self.transformer = transformer_model

    def forward(self, input_ids, attention_mask=None):
        logits = self.transformer(input_ids,attention_mask=attention_mask)[0]
        return logits