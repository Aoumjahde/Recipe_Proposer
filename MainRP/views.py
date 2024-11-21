from django.http import HttpResponse
from MainRP.forms import RecipeForm
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            ingredients = form.cleaned_data['ingredients']
            return HttpResponse(f"Thank you, {user_name}. Your message has been received!")
    else:
        form = RecipeForm()

    return render(request, 'MainRP/recipeform.html', {'form': form})