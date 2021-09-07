from django.shortcuts import render

# Create your views here.

def profileView(request):
    context = {

    }
    return render(request, 'home/profile.html', context)
def historyView(request):
    context = {

    }
    return render(request, 'home/order-history.html', context)