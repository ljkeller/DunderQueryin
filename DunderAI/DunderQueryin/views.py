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
        
        # 'redirect' response to prevent post -> user hits back -> posts again
        return HttpResponseRedirect('/')
        # TODO: take to results page
        # character = dunder_ai.predict(quote)
        # return HttpResponseRedirect(reverse('query:result', args=(character,)))