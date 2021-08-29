# feature extract.py
from src.models import InferSent
import torch
import pandas as pd
from src.model import loading_model
from tqdm import tqdm

class Extract_Features:
    def __init__(self, model):
        self.model = model
    
    def extract_sentence(self, query):
        vector_result = self.model.encode(query)[0]
        return vector_result

# model = loading_model()
# model = model.load_model()

# data = pd.read_csv ('../dataset/captions.csv')

# features = []
# extract = Extract_Features(model)
# f = open('features.txt', 'a+')
# for index, sentence in tqdm (enumerate (data['caption'])):
#     vector = extract.extract_sentence(sentence)
#     vector = list (vector)
#     f.write('{}, {}, {}'.format(data['image'][index], str(vector),  '\n'))
# f.close()


# print (vector)
    
