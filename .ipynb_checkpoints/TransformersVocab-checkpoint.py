# fastai
from fastai.text import Collection,List,Vocab

import numpy as np

# transformers
from transformers import PreTrainedTokenizer

'''
The TransformersVoca class is wrapper around the Vocab class of fast.ai and it stores the pretrained transformers tokenizer.
Additionaly this class implements methods to converts tokens to ids and vice versa. This functionality is needed to make
transformer library work with fast.ai.
Taken from: https://www.kaggle.com/maroberti/fastai-with-transformers-bert-roberta
'''

class TransformersVocab(Vocab):
    def __init__(self, tokenizer: PreTrainedTokenizer):
        super(TransformersVocab, self).__init__(itos=[])
        self.tokenizer = tokenizer

    def numericalize(self, t: Collection[str]) -> List[int]:
        "Convert a list of tokens `t` to their ids."
        return self.tokenizer.convert_tokens_to_ids(t)
        # return self.tokenizer.encode(t)

    def textify(self, nums: Collection[int], sep=' ') -> List[str]:
        "Convert a list of `nums` to their tokens."
        nums = np.array(nums).tolist()
        return sep.join(
            self.tokenizer.convert_ids_to_tokens(nums)) if sep is not None else self.tokenizer.convert_ids_to_tokens(
            nums)