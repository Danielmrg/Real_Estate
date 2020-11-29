from django import forms
from .models import *


class AdvertForm(forms.ModelForm):

    class Meta:
        model = Advertising
        fields = [
            'user',
            'image',
            'title',
            'price',
            'address',
            'description',
            'send_in_estate',
            'send_in_publish',
            'category',
            'status',
            'slug',
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'status': forms.HiddenInput(),
            'slug': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'placeholder': 'عنوان'},),
        }
        help_texts = {
            'price': ('چنان چه چیزی وارد نکنید توافقی خواهد بود.'),
            'address': ('چنان چه چیزی وارد نکنید نام بنگاه خواهد بود.'),
        }
