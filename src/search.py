import json
from numpy import dot
from numpy.linalg import norm
from scipy import spatial

def cos_sim (a, b):
  result = 1 - spatial.distance.cosine(a, b)
  return result

class search:
    def __init__(self):
        with open('./src/database/inverted_index.json') as d:
            self.data = json.load(d)
    
    def pair(self, query, reader, extract, features):
              # preprocess query -> query clean
        # query clean -> truy vấn vào final.json lấy các ảnh chứa từ đó ra
        img_list = []
        query = reader.preprocess_sentence(query)
        for i in query:
          try:
            for j in self.data[i]:
                if (j not in img_list):
                    img_list.append(j)
                else: pass
          except: pass
        # đưa query -> vector
        #query = reader.preprocess_sentence(query)
        query = ' '.join(query)
        query_vector = extract.extract_sentence(query)
        # define cosine threshold if cosine > threshold -> return this image
        threshold = 0.9
        result = {}
        count = 0
        # with open('./src/database/features.json') as fe:
        #     features = json.load(fe)
        # for i in features:
        #   for j in range (len(features[i])):
        #     features[i][j] = float(features[i][j])
        for i in img_list:
            try:
              img_path = str(i)
              cos = cos_sim(query_vector, features[i])
              if (cos > threshold):
                result.update({img_path: cos})
            except: pass
        # {key: value for key, value in sorted(result.items(), key=lambda item: item[1])}
        path = []
        for index, link in enumerate (result):
          if (index < 20):
            path.append(link)
          else:
            break
        return path