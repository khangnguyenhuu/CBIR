import pandas as pd
import nltk
from string import digits, punctuation
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
# nltk.download('stopwords')
# nltk.download('punkt')
# nltk.download('wordnet')

class Reader:
    def __init__(self):
        self.data = pd.read_csv('./src/database/captions.csv')
        self.dirs = self.data['image']
        self.captions = self.data['caption']
        stop_words = set(stopwords.words('english'))
        stop_words = list(stop_words)
        self.stop_words = stop_words
        self.Lemmatizer = WordNetLemmatizer()
 
    def preprocess_sentences(self):
        tokenizes = []
        for index, sentence in enumerate (self.captions):
            # lower all word
            sentence = sentence.lower()
            # remove all stop words
            sentence = sentence.translate(str.maketrans('', '', punctuation))
            sentence = sentence.translate(str.maketrans('', '', digits))
            # tokenize sentence
            tmp_sentence = nltk.word_tokenize(sentence)
            tokenizes.append(tmp_sentence)
            
        # Lemmatize    
        for j, word_tokenize in enumerate (tokenizes):
            tokenizes[j] = self.Lemmatizer.lemmatize(tokenizes[i][j])            

        # remove stopwords
        result = []
        index_count = 0
        for sentence in tokenizes:
            result.append([])
            for word in sentence:
                if (word not in self.stop_words):
                    result[index_count].append(word)
            index_count +=1 
        
        return result


    def preprocess_sentence(self, sentence):

        Lemmatizer = WordNetLemmatizer()
        # lower all word
        sentence = sentence.lower()
        # remove all stop words
        sentence = sentence.translate(str.maketrans('', '', punctuation))
        sentence = sentence.translate(str.maketrans('', '', digits))
        # tokenize sentence
        sentence = nltk.word_tokenize(sentence)
        result_sentence = []
        # Lemmatize    
        for i, word_token in enumerate(sentence):
            word_token = self.Lemmatizer.lemmatize(word_token)            
            if (word_token not in self.stop_words):
                result_sentence.append (word_token)
        return result_sentence

    # def write_to_csv(self):
    #     result = self.preprocess()
    #     df = pd.DataFrame({'images': for i in self.data['images'],
    #                         'captions': for j in results})
    #     print (df)


# reader = Reader()
# result = reader.preprocess_sentence('a child is going in the park, with his friends')
# print (result)
