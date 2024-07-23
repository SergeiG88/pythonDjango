from django.shortcuts import render

def index(request):
    title = 'мой сайт'
    text = 'my text'
    context = {
        'title': title,
        'text': text,
    }
    return render(request, 'index.html', context)
