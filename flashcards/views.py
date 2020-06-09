from django.shortcuts import render, redirect
from .forms import FlashCreationForm
from .models import FlashCards

def index(request):

    return render(request, 'index.html')

def flash_creation(request):
    current_user=request.user
    if request.method == 'POST':
        form=FlashCreationForm(request.POST)
        if form.is_valid():  # and current_user=='small_bro'
            form.save()
            return redirect('flash_creation')
    else:
        form=FlashCreationForm()
    return render(request, 'flash_creation.html', {'form': form})

