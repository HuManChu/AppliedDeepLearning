# **Bert based sentiment classifier**

## **Exc.1) Initiate**:

### **1.Literature**:

[BERT: Pre-training of Deep Bidirectional Transformers forLanguage Understanding](https://arxiv.org/pdf/1810.04805.pdf%E3%80%91)

[How to Fine-Tune BERT for Text Classification?](https://arxiv.org/pdf/1905.05583.pdf)

[Transformer Architecture](https://arxiv.org/pdf/1706.03762.pdf)

[RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://arxiv.org/pdf/1907.11692.pdf)

### **2.Topic**: 
The topic of my project is text classification.


### **3.Project Type**:
The project type is beat the classics.


### **4.Summary**:
I'll try to beat the classical aproaches like TF-IDF and Word2Vec on a text classification task. The neural network architecture I'm gonna use is a pretrained transformer model called Roberta, which is an optimized version of Bert. [pytorch-bert-pretrained](https://pypi.org/project/pytorch-pretrained-bert/).
I'll fine tune this model for a specific classification task.

BERT stands for Bidirectional Encoder Representations from Transformers, the backbone of BERT is the [Transformer Architecture](https://arxiv.org/pdf/1706.03762.pdf).

The dataset is the Sentiment dataset with 1.6 million tweets from [twitter sentiment data](https://www.kaggle.com/kazanova/sentiment140) and the task is predicting if a tweet has a positive or a negative sentiment.
The dataset is known so we can compare our results with those of other people on kaggle.


**Work breakdown**:

| hours | description |
| --- | ----------- |
| 15h | data preprocessing and literature |
| 15h | model building |
| 20h | build application and documentation |

### **5.References**:
I took a lot of the code and logic from [fast.ai and transformers](https://www.kaggle.com/maroberti/fastai-with-transformers-bert-roberta), which made an awsome notebook, where the transformers library and fast.ai are used in a combined fashion.


## **Exc.2) Hacking**:

### **Prerequesits:**
To build and train the sentiment classifier I used a jupyter notebook, which can be run by setting up a conda python=3.7 environment and installing the following dependencies:

-pip install transformers
-pip install fastai

The rest of the dependencies should be included by conda.
Jupyter notebooks are very convinient for handling big amounts of data, since you don't have to start over the whole program if a particular operation fails. This saves a lot of time and simplifies the model building process significantly.

### **Training:**
The training process was straight forward and I barely used any preprocessing of the data, since BERT based models are made for dealing with stopwords and context information. As a target metric I used the accuracy, which is the most common used metric for classification tasks.
For the training I split the roberta layers into 3 blocks and trained them seperatly on 80% of the twitter sentiment data.
20% of the data I used as a test set to check the model performance on unseen data.
The training of the embedding layer didn't give use any improvement, so I only trained the classification layer and the 12 transformer layers for 1 epoch and that's it.
The complete description of what steps where made is revealed in form of markedown comments in the notebook, which should it make easy to understand what is going on in the code.

###**Workload:**
The real workload for data preprocessing, literature search, model building and documentation took me much more than the 30h I proclaimed. It was around 40-45 hours and I lost most time on finding a useful api and getting used to an appropriate implementation of the transformers architecture.
So the actual work I did is more like:

| hours | description |
| --- | ----------- |
| 8h | data preprocessing and literature |
| 35h | model building and testing lot's of different fine tuning approaches |
| 2h | documentation |

One the other hand the final notebook I used is very short and I only had to make minor modifications compared tho the 
[fast.ai and transformers](https://www.kaggle.com/maroberti/fastai-with-transformers-bert-roberta) notebook to achieve this result.

### **Results:**
With only 2 epochs of training the final model was able to achieve an accuracy of 83% on the test set.
The classification reports shows that both classes are treated equally and the model performs also well on other metrics:

|  class | precision  |  recall |  f1-score |  support |
|--------|------------|---------|-----------|----------|
|   0    |    0.82    |  0.85   |   0.84    |  160080  |
|   1    |    0.84    |  0.82   |   0.83    |  159920  |

I used the [twitter sentiment data](https://www.kaggle.com/kazanova/sentiment140) because it's a known dataset on kaggle, where we can compare the results of different ml approaches.
The first example for comparission is a classical  TF-IDF and Naive Bayes model [TFIDF-NB](https://www.kaggle.com/harivikneshs/simple-sentiment-analysis-using-nb-and-tfidf), which has an accuracy of ~75%  and the second example is a Word2Vec embedding with an LSTM on top of it [Word2Vec-LSTM](https://www.kaggle.com/prashant268/sentiment-analysis-lstm) which has an accuracy of 79,7%.
There are much more kernels on kaggle to this dataset, the above mentioned are just for illustration.

### **Conclusion**:
This simple transformers fine tuning approach gives us state of the art results on a known classification problem. So far as I saw no approach on kaggle got such a high accuracy on this particular dataset. So I think I can claim that I beat the classics with the transformer architecture :)
If I would have more time, I would train the whole model for another epoch or two and unfreeze all layers during that, which should improve the accuracy even further.










