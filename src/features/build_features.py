import pickle


path = "../../data/raw/cifar-10-batches-py/"
import os

chemin_actuel = os.path.dirname(os.path.abspath(__file__))
print("Chemin d'accès relatif :", chemin_actuel)
def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='bytes')
    return dict


batch = unpickle(path + "data_batch_1")

data = batch[b'data']

from sklearn.cluster import KMeans
import numpy as np
def cluster_image(image, num_clusters):

    image_2d = image.reshape(-1, 3)


    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(image_2d)

    pixel_labels = kmeans.labels_


    clustered_image = kmeans.cluster_centers_[pixel_labels]
    clustered_image = clustered_image.reshape(image.shape)

    return clustered_image

clustered_images = []

for image_index in range(len(data)):
    img_flat = data[image_index, :]

    r = img_flat[0:1024].reshape(32, 32)
    g = img_flat[1024:2048].reshape(32, 32)
    b = img_flat[2048:].reshape(32, 32)
    img = np.dstack((r, g, b))
    n_factors = 2


    

    clustered_img = cluster_image(img, num_clusters=5)
    clustered_images.append(clustered_img)
from matplotlib import pyplot as plt

with open('clustered_images.pickle', 'wb') as f:
    pickle.dump((clustered_images), f)

with open('clustered_images.pickle', 'rb') as f:
    clustered_images = pickle.load(f)
