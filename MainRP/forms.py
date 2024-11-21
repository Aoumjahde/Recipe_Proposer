from django import forms

class RecipeForm(forms.Form):
    user_name = forms.CharField(label='Your Name', max_length=100)
    ingredients = forms.CharField(widget=forms.Textarea, label='Insert ingredients separated by a comma ",".')