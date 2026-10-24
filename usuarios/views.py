from django.shortcuts import render

def login(request):
    # O Django procura por: tarefas/templates/tarefas/login.html
    return render(request, 'tarefas/login.html')