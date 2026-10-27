from django import forms


class PostForm(forms.Form):
    title = forms.CharField(
        max_length=200,
    )
    content = forms.CharField()
    rating = forms.IntegerField(
        min_value=0,
        max_value=100,
    )


