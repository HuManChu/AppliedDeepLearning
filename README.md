## **Bert-based movie-genre classifier**

### **1.Literature**:

[BERT: Pre-training of Deep Bidirectional Transformers forLanguage Understanding](https://arxiv.org/pdf/1810.04805.pdf%E3%80%91)

[How to Fine-Tune BERT for Text Classification?](https://arxiv.org/pdf/1905.05583.pdf)

[Transformer Architecture](https://arxiv.org/pdf/1706.03762.pdf)

### **2.Topic**: 
The topic of my project is text classification.


### **3.Project Type**:
The project type is beat the classics.


### **4.Summary**:
I'll try to beat the classical aproaches like svm, random forest,.. on a text classification task. The neural network architecture I'm gonna use is a pretrained BERT model [pytorch-bert-pretrained](https://pypi.org/project/pytorch-pretrained-bert/), which I'll fine tune for a specific classification task. 
BERT stands for Bidirectional Encoder Representations from Transformers, the backbone of this architecture is the Transformer [Transformer Architecture](https://arxiv.org/pdf/1706.03762.pdf).

The dataset is the Wikipedia Movie Plots [kaggle.com/jrobischon/wikipedia-movie-plots](https://www.kaggle.com/jrobischon/wikipedia-movie-plots) data and the task is predicting the genre. This is quite complicated since there are more than 2.000 disctinct genres listed from 34,886 movie descriptions. We will need some data preprocessing and probably also a method to handle genres where only 1 example exists.


**Work breakdown**:

| hours | description |
| --- | ----------- |
| 15h | data preprocessing and literature |
| 15h | model building |
| 20h | build application and documentation |