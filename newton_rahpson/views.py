from django.shortcuts import render, HttpResponse

import json

def calcular(request):
    if request.method == 'POST':
        expressao = json.loads(request.body)['expressao']
        # Aqui você pode processar a expressão, por exemplo, usando uma biblioteca de álgebra simbólica
        resultado = f"Você digitou: {expressao}"
        return HttpResponse(json.dumps({'resultado': resultado}), content_type='application/json')
    else:
        return render(request, 'calc/index.html')