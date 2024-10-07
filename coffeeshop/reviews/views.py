from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import Review
from .forms import ReviewForm

def review_list(request):
    reviews = Review.objects.all().order_by('-pub_date')
    return render(request, 'reviews/review_list.html', {'reviews': reviews})

@login_required(login_url='/login/')
def add_review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author = request.user
            review.pub_date = timezone.now()
            review.save()
            return redirect('review_list')
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'reviews/register.html', {'form': form})
