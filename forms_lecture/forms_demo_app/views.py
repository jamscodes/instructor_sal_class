from django.shortcuts import render, redirect
from .forms import First_Form, DB_Form

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = First_Form(request.POST)
        if form.is_valid():
            return redirect('/success/')
    else:
        context = {
            'form': First_Form(),
            'model_form': DB_Form()
        }
    return render(request, 'index.html', context)