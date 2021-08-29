from django import forms

class Query(forms.Form):
    query = forms.CharField(max_length = 100)

# class Result(forms.Form):
#     query = 