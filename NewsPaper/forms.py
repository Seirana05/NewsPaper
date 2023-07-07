from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title',
            'text',
            'postCategory',
            'author'


        ]

        def clean(self):
            cleaned_data = super().clean()
            text = cleaned_data.get("text")
            title = cleaned_data.get("title")

            if title == text:
                raise ValidationError(
                    "Описание не должно быть идентично названию."
                )

            return cleaned_data