from django import forms


class RecipesSearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100, 
        label='Filter by', 
        widget=forms.TextInput(
            attrs={"placeholder": "Ingredient or Recipe"}
        )    )
