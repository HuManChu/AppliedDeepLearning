# fastai
from fastai.text import BaseTokenizer,List


# transformers
from transformers import  PreTrainedTokenizer

'''
A wrapper around BaseTokenizer class from fast.ai to store and call the pretrained tokenizer from 
the transformers library in the fast.ai framework.
Taken from: https://www.kaggle.com/maroberti/fastai-with-transformers-bert-roberta
'''

class TransformersBaseTokenizer(BaseTokenizer):
    def __init__(self, pretrained_tokenizer: PreTrainedTokenizer, model_type = 'bert', **kwargs):
        self._pretrained_tokenizer = pretrained_tokenizer
        self.max_seq_len = pretrained_tokenizer.max_len
        self.model_type = model_type

    def __call__(self, *args, **kwargs):
        return self
    '''
    Here the for transformers crucial CLS and SEP tokens are set at beginning and end of every sentence.
    Additionaly the input str get's tokenized and the number of tokens get's limited.
    '''
    def tokenizer(self, t:str) -> List[str]:
        CLS = self._pretrained_tokenizer.cls_token
        SEP = self._pretrained_tokenizer.sep_token
        tokens = self._pretrained_tokenizer.tokenize(t, add_prefix_space=True)[:self.max_seq_len - 2]
        return [CLS] + tokens + [SEP]