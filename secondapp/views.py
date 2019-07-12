from django.shortcuts import render

# Create your views here.
def secondapp_practice(request):
    return render(request, 'secondapp/modelpractive.html', {})
