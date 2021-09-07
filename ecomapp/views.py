from django.shortcuts import render

# Create your views here.

def indexview(request):
    context = {

    }
    return render(request, 'home/index.html', context)
