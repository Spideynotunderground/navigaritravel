from django.shortcuts import render, redirect

from .forms import TourForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def forma(request):
    if request.method == 'POST':
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:success')
    else:
        form = TourForm()
    
    return render(request, 'form.html', {'form': form})


def success(request):
    return render(request, 'success.html')