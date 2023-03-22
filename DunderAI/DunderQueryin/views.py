from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

def dunder_ai(request):
    return render(request, 'DunderQueryin/dunder_ai.html', {})

def query(request):
    try:
        quote = request.POST['quote']
    except (KeyError):
        return render(request, 'DunderQueryin/dunder_ai.html', {'error_message': 'Something went wrong with your quote!'})
    else:
        print(quote)
        # Predict here

        # Not sending HTPP response, but I should be
        # workaround to render correctly on this webpage
        return render(request, 'DunderQueryin/dunder_ai.html', {'model_prediction': 'Kevin'})