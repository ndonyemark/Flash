from django.shortcuts import render, redirect
from .forms import FlashCreationForm
from .models import FlashCards
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    flash_cards=FlashCards.objects.all()
    return render(request, 'index.html', {'flash_cards': flash_cards})

@login_required
def flash_creation(request):
    current_user=request.user
    if request.method == 'POST':
        form=FlashCreationForm(request.POST)
        if form.is_valid():  # and current_user=='small_bro'
            form.save()
            return redirect('post_flash')
    else:
        form=FlashCreationForm()
    return render(request, 'flash_creation.html', {'form': form})

@login_required
def flash_detail(request, flash_id):
    flash_card = FlashCards.objects.get(id=flash_id)
    return render(request, 'flash_detail.html', {'flash_card':flash_card})

@login_required
def delete_flash_card(request, flash_id):
    flash_card = FlashCards.objects.get(id=flash_id)
    if request.method == 'POST':
        flash_card.delete()
        return redirect('index')
    return render(request, 'delete_flash.html', {'flash_card':flash_card})

@login_required
def update_flash_card(request, flash_id):
    flash_card = FlashCards.objects.get(id=flash_id)
    form = FlashCreationForm(request.POST or None, instance=flash_card)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'update_flash.html', {'form':form})