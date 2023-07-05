import numpy as np
import pickle
import pandas as pd


path = "data/raw/cifar-10-batches-py/"


def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


batch = unpickle(path + "data_batch_1")

data = batch[b'data']
labels = batch[b'labels']


# Load the data
for data_batch in ["data_batch_2",
                   "data_batch_3",
                   "data_batch_4",
                   "data_batch_5"]:
    batch = unpickle(path + data_batch)
    data = np.concatenate((data, batch[b'data']), axis=0)
    labels = np.concatenate((labels, batch[b'labels']), axis=0)


df_train = pd.DataFrame(data)
df_train['label'] = labels
df_train.to_csv('data/processed/train.csv', index=False)


test_batch = unpickle(path + "test_batch")
df_test = pd.DataFrame(test_batch[b'data'])
df_test['label'] = test_batch[b'labels']
df_test.to_csv('data/processed/test.csv', index=False)
