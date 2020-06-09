from django import forms
from .models import FlashCards

class FlashCreationForm(forms.ModelForm):
    class Meta:
        model=FlashCards
        fields=['flash_title', 'flash_body', 'flash_course']