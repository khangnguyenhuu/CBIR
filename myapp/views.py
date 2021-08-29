from django.shortcuts import render
from django.http import HttpResponse
from .query import Query
from src.feature_extract import Extract_Features
from src.model import loading_model
from src.models import *
from src.preprocess import *
from src.search import *
# Create your views here.

model = loading_model()
model = model.load_model()
reader = Reader()
extract = Extract_Features(model)
with open('./src/database/features.json') as fe:
    features = json.load(fe)
for i in features:
    for j in range (len(features[i])):
        features[i][j] = float(features[i][j])

def get_query (request):
    return render (request, 'index.html')

def process(request):
    if request.method == "POST":
        m = Query(request.POST)
        if m.is_valid():
            query = m.cleaned_data['query']
            searcher = search()
            path = searcher.pair(query, reader, extract, features)
            list_image = []
            for i in path:
                img_path = 'Images/' + i
                list_image.append(img_path)
            context = {'query': query, 'list_image': list_image}
            return render(request, 'print_query.html', context)
    
