from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'groups/index.html')


def ranking(request):
    return render(request, 'groups/ranking.html')