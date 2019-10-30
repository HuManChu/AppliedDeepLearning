## Bert-based-text classifier

### 1.References:

[BERT: Pre-training of Deep Bidirectional Transformers forLanguage Understanding](https://arxiv.org/pdf/1810.04805.pdf%E3%80%91)

[How to Fine-Tune BERT for Text Classification?](https://arxiv.org/pdf/1905.05583.pdf)

### 2.Topic: Text Classification


### 3.Project Type: Beat the classics


### 4.Summary:
I'll try to beat the classical aproaches like svm, random forest,.. on a text classification task. The neural network architecture I'm gonna use is a pretrained BERT model [pytorch-bert-pretrained](https://pypi.org/project/pytorch-pretrained-bert/), which I'll fine tune for a specific classification task.

The dataset is the Wikipedia Movie Plots [kaggle.com/jrobischon/wikipedia-movie-plots](https://www.kaggle.com/jrobischon/wikipedia-movie-plots) data and the task is predicting the genre. This is quite complicated since there are more than 2.000 disctinct genres listed from 34,886 movie descriptions. We will need some data preprocessing and probably also a method to handle genres where only 1 example exists.

**Work breakdown**:

| hours | description |
| --- | ----------- |
| 10h | data preprocessing |
| 15h | model building |
|25h|build application and documentation|