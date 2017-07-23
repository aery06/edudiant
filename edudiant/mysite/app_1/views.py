from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app_1/index.html', {'index' : index});

def connection(request):
    return render(request, 'app_1/connection.html', {'connection' : connection});

def resources(request):
    return render(request, 'app_1/resources.html', {'resources' : resources });

def vedios(request):
    return render(request, 'app_1/vedios.html', {'vedios' : vedios});

def audio(request):
    return render(request, 'app_1/audio.html', {'audio' : audio});

def docs(request):
    return render(request, 'app_1/docs.html', {'docs' : docs});

#    returnces render(request, 'app_1/.html', {'' : }