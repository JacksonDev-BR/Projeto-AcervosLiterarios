from django.shortcuts import render

def listar_tarefas(request):
    # O Django procura por: tarefas/templates/tarefas/listar_tarefas.html
    return render(request, 'tarefas/listar_tarefas.html')

def dasshboard(request):
    # O Django procura por: tarefas/templates/tarefas/dasshboard.html
    return render(request, 'tarefas/dasshboard.html')