from django.shortcuts import render

# Create your views here.

def home(request):
    print('Process')

    context = {
        'text': 'Welcome Home.',
    }
    return render(request, 'home/index.html', context)