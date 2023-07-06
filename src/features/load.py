import pickle
from matplotlib import pyplot as plt
with open('clustered_images.pickle', 'rb') as f:
    clustered_images = pickle.load(f)
print(clustered_images[0])
