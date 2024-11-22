from django.http import HttpResponse
from MainRP.forms import RecipeForm
from django.shortcuts import render
import openai
import os

openai.api_key = os.environ.get("OPENAI_API_KEY")  ##TODOCUMENT
if not openai.api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set.")

def index(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            ingredients = form.cleaned_data['ingredients']
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system",
                     "content": "You are an assistant programmed to give advice about recipes to do given a certain set of ingredients. I'd advise for you to attain to standard, known recipes and to not create new ones. Whenever you give advice, call the user by name."},
                    {"role": "user", "content": 'user name: ' + user_name + ' ingredients: ' + ingredients}
                ],
                max_tokens=150,
                temperature=0.7
            )
            return render(request, 'MainRP/recipe_display.html', {'recipe_paragraph': response.choices[0].message.content})
    else:
        form = RecipeForm()

    return render(request, 'MainRP/recipeform.html', {'form': form})

