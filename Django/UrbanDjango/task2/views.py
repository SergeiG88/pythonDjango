from django.shortcuts import render

def class_view(request):
    # data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request, 'second_task/class_template.html')

def function_view(request):
    return render(request, 'second_task/func_template.html')
