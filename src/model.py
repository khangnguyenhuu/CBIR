# model.py
from src.models import InferSent
import torch
import pandas as pd

class loading_model:
    def load_model(self):
        # extract the features from a text
        data = pd.read_csv('./src/database/captions.csv')
        sentences = data['caption']

        V = 2
        MODEL_PATH = './src/encoder/infersent2.pkl'
        params_model = {'bsize': 64, 'word_emb_dim': 300, 'enc_lstm_dim': 2048,
                        'pool_type': 'max', 'dpout_model': 0.0, 'version': V}
        model = InferSent(params_model)
        model.load_state_dict(torch.load(MODEL_PATH))

        W2V_PATH = './src/GloVe/glove.840B.300d.txt'
        model.set_w2v_path(W2V_PATH)

        model.build_vocab(sentences, tokenize=True)
        print ('--------------load model sucess----------')
        return model