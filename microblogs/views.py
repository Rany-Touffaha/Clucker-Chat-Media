from django.shortcuts import redirect, render
from .forms import SignUpForm, PostForm


def home(request):
    return render(request, 'home.html')


def feed(request):
    form = PostForm()
    return render(request, 'feed.html', {'form': form})


def log_in(request):
    #form = PostForm()
    #return render(request, 'feed.html', {'form': form})
    return render(request, 'log_in.html')


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('feed')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})
