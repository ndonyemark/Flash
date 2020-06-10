from django import forms
from .models import FlashCards, Courses

class FlashCreationForm(forms.ModelForm):
    class Meta:
        model=FlashCards
        fields=['flash_title', 'flash_body', 'flash_course']

class CourseRegistrationForm(forms.ModelForm):
    class Meta:
        model=Courses
        fields=['course_name']