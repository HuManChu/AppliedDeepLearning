import random as rnd

#fastai
from fastai.text import *

# nltk
import pandas as pd

# sklearn
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"


'''
The seed_all method sets the seed in all necessary classes to get reproducable results.
Taken from: https://www.kaggle.com/maroberti/fastai-with-transformers-bert-roberta
'''
def seed_all(seed_value):
    rnd.seed(seed_value)  # Python
    np.random.seed(seed_value)  # cpu vars
    torch.manual_seed(seed_value)  # cpu  vars

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed_value)
        torch.cuda.manual_seed_all(seed_value)  # gpu vars
        torch.backends.cudnn.deterministic = True  # needed
        torch.backends.cudnn.benchmark = False

'''
The load_and_process_data function takes the path to the data, the encoding and the column names of the data and loads it.
Afterwards we drop the NAs, rename the columns, clean the data and set label 4 to 1, which is more common.
'''
def load_and_process_data(file: str, label: str, text: str, encoding: str, column_names: str, random_state = 123, test_size=0.2):
    df = pd.read_csv(file,encoding = encoding, names = column_names)
    df = df.dropna()
    df["label"] = df[label]
    df["text"] = df[text]
    df = df[["label", "text"]]
    df["text"] = df["text"].apply(lambda x : _preprocess_txt(x))
    df["label"] = df["label"].apply(lambda x : 0 if x==0 else 1)
    train, test = train_test_split(df, test_size=test_size, random_state=random_state)
    return train, test


def _preprocess_txt(text):
    # Remove link,user and special characters
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
    return text

'''
The get_classification_report function calculates the model predictions for the test set and calculates the precision, recall and
accuracy.
'''
def get_classification_report(learner,test,data):
    """
    the get_preds method does not yield the elements in order by default
    we borrow the code from the RNNLearner to resort the elements into their correct order
    """
    preds = learner.get_preds(DatasetType.Test)[0].detach().cpu().numpy()
    sampler = [i for i in data.dl(DatasetType.Test).sampler]
    reverse_sampler = np.argsort(sampler)
    preds = preds[reverse_sampler, :]
    test["preds"] = np.argmax(preds,axis=1)
    report = classification_report(test["label"], test["preds"])
    return report