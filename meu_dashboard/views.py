from django.shortcuts import render
from .models import Vendas, Produto, Vendedor
from django.http import JsonResponse
from django.db.models import Sum
from datetime import datetime


def home(request):
    return render(request, 'home.html')

def total_vendido(request):
    total = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
    
    if request.method == "GET":
        return JsonResponse({'total': total})
    
def lucro_liquido(request):
    despesa_fixa = 26500 * 12
    faturamento = Vendas.objects.all().aggregate(Sum('total'))['total__sum'] 

    lucro = faturamento - despesa_fixa

    if request.method == "GET":
        return JsonResponse({'lucro': lucro})
    
    
def despesa_anual(request):
    faturamento = Vendas.objects.all().aggregate(Sum('total'))['total__sum']
  
    despesa_fixa = 26500 * 12
   
    despesa_anual = despesa_fixa / faturamento * 100

    
    if request.method == "GET":
        return JsonResponse(data={'despesa_anual': despesa_anual})
    


def relatorio_faturamento(request):
    x = Vendas.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []
    
    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        y = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        labels.append(meses[mes-1])
        data.append(y)
        

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)        

  

def relatorio_produtos(request):
    produtos = Produto.objects.all()
    label = []
    data = []
    for produto in produtos:
        vendas = Vendas.objects.filter(nome_produto=produto).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(produto.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})

def relatorio_funcionario(request):

    vendedores = Vendedor.objects.all()
    label = []
    data = []
    for vendedor in vendedores:
        vendas = Vendas.objects.filter(vendedor=vendedor).aggregate(Sum('total'))
        if not vendas['total__sum']:
            vendas['total__sum'] = 0
        label.append(vendedor.nome)
        data.append(vendas['total__sum'])

    x = list(zip(label, data))

    x.sort(key=lambda x: x[1], reverse=True)
    x = list(zip(*x))
    
    return JsonResponse({'labels': x[0][:3], 'data': x[1][:3]})


def relatorio_despesas(request):
    x = Vendas.objects.all()
    
    meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
    data = []
    labels = []

    despesa_fixa = 26500 

    mes = datetime.now().month + 1
    ano = datetime.now().year
    for i in range(12): 
        mes -= 1
        if mes == 0:
            mes = 12
            ano -= 1
        
        f = sum([i.total for i in x if i.data.month == mes and i.data.year == ano])
        if f == 0:
            f = 1

        y = (despesa_fixa / f) * 100       
        labels.append(meses[mes-1])       
        data.append(y)
        

    data_json = {'data': data[::-1], 'labels': labels[::-1]}
     
    return JsonResponse(data_json)