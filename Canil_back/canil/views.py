from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from datetime import datetime

@csrf_exempt
@require_POST
def submit_form(request):
    data = json.loads(request.body)
    calend = data.get('data')
    bigDogs = data.get('bigDogs')
    smallDogs = data.get('smallDogs')

    if(calend == ''):
        return JsonResponse ({'melhor_canil': '', 'valor' : ''})
    

    bigDogs = float(bigDogs)
    smallDogs = float(smallDogs)

    
    
    
    if(final_semana(calend) ):
        

        Meu_Canino_Feliz = ((20*20/100+20)*smallDogs) + ((40*20/100+40)*bigDogs)

        Vai_Rex = (20*smallDogs) + (55*bigDogs)

        ChowChawgas = (30*smallDogs) + (45*bigDogs)

        
    
    else:
        Meu_Canino_Feliz = (20*smallDogs) + (40*bigDogs)

        Vai_Rex = (15*smallDogs) + (50*bigDogs)

        ChowChawgas = (30*smallDogs) + (45*bigDogs)

    data = [
    {"Nome": "Meu Canino Feliz", "Valor": Meu_Canino_Feliz, "Distancia": 2},
    {"Nome": "Vai Rex", "Valor": Vai_Rex, "Distancia": 1.7},
    {"Nome": "ChowChawgas", "Valor": ChowChawgas, "Distancia": 0.8}
]
        
    menor = min(data, key=lambda x: (x["Valor"], x["Distancia"]))
    print(menor)

    return JsonResponse({'melhor_canil':menor["Nome"], 'valor': menor["Valor"]})
    

    # Aqui você pode processar os dados do formulário, como salvar no banco de dados ou enviar um email
    print(f'Data: {data}, Cachorrão: {bigDogs}, Cachorrinho: {smallDogs}')
    
    return JsonResponse({'data': 'Obrigado pelo contato!'})

    
# Create your views here.

def final_semana(data):
    converter = datetime.strptime(data, '%Y-%m-%d')
    dia_semana = converter.weekday()
   
    return dia_semana in (5,6)


