import pandas as pd
import json

def indexing(path):
    # create vocabulary
    data = pd.read_csv(path)
    vocab = {}
    count = 1
    for i, caption in enumerate(data['caption']):
        caption = caption.split(' ')
        for j in caption:
            # if the word is not in vocab then add a key of this word to dictionary
            # then add the path of image to values of this key
            if j not in vocab.keys():
                vocab.update({j:[data['image'][i]]})
                count += 1
                print (count)
            # else add the path of of image to exist key
            else:
                if (data['image'][i] not in vocab[j]):
                    vocab[j].append(data['image'][i])
        with open ('final.json', 'w') as final:
            json.dump(vocab, final)
        
        


