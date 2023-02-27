from .models  import Product
from django.forms import ModelForm, TextInput, Textarea, FileInput


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'preview', 'description', 'price', 'number']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назва товару'
            }),
            "preview": FileInput(attrs={
                'class': 'form-control',
                'placeholder': 'Превю товару'
            }),
            "description": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опис товару'
            }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'ціна'
            }),
            "number": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'кількість'
            })
        }