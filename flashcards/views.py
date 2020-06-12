from django.shortcuts import render, redirect
from .forms import FlashCreationForm,CourseRegistrationForm
from .models import FlashCards, Courses
from django.contrib.auth.decorators import login_required
from django.utils import timezone

@login_required
def index(request):
    flash_cards=FlashCards.objects.all()
    print(flash_cards)
    return render(request, 'index.html', {'flash_cards': flash_cards})

@login_required
def flash_creation(request):
    current_user=request.user
    # courses=Courses.objects.all()
    if request.method == 'POST':
        form=FlashCreationForm(request.POST)
        if form.is_valid():  # and current_user=='small_bro'
            form.save()
            return redirect('index')
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
        form_save = form.save(commit=False)
        form_save.date_updated = timezone.now()
        form_save.save()
        return redirect('index')
    return render(request, 'update_flash.html', {'form':form})

@login_required
def course_registration(request):
    if request.method == 'POST':
        form = CourseRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('register_course')
    else:
        form = CourseRegistrationForm()
    return render(request, 'course_registration.html', {'form': form})

def get_science(request):
    courses = FlashCards.objects.filter(flash_course='sciences')
    return render(request, 'sciences.html', {'courses':courses})

def get_languages(request):
    course = FlashCards.objects.filter(flash_course='languages')
    return render(request, 'languages.html', {'course':course})

def get_religious(request):
    course = FlashCards.objects.filter(flash_course='religious')
    return render(request, 'religious.html', {"course":course})

def get_courses(request):
    courses = Courses.objects.all()
    print(courses)
    return render(request, 'navbar.html', {'courses':courses})