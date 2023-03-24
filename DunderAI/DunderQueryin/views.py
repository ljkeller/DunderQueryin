from django.shortcuts import render
from django.http import HttpResponseRedirect

from fastai.text.all import *

# TODO: Should we serve this through static/DunderQueryin?
MODEL_PATH='data/model'

def quote_to_prediction(quote):
    learner = load_learner(MODEL_PATH)
    character, character_tensor, tensors = learner.predict(quote)
    return character, tensors[character_tensor].item()

def build_render_context(character, probability, quote, max_quote_len=128):
    model_results_context = {}
    model_results_context['character_prediction'] = character
    model_results_context['prediction_probability'] = "{:.1f}".format(probability*100)
    model_results_context['user_quote'] = quote if len(quote) < max_quote_len else quote[:max_quote_len-3] + "..."
    return model_results_context

def dunder_ai(request):
    return render(request, 'DunderQueryin/dunder_ai.html', {})

def query(request):
    try:
        # TODO: Enforce 'normal' quote input (regex?)
        quote = str.strip(request.POST['quote'])
        if not quote: return HttpResponseRedirect('/')
    except (KeyError):
        return render(request, 'DunderQueryin/dunder_ai.html', {'error_message': 'Something went wrong with your quote!'})
    else:
        character_prediction, prediction_probability = quote_to_prediction(quote)

        # Not sending HTPP response, but I should be
        # workaround to render correctly on this webpage
        return render(request, 'DunderQueryin/dunder_ai.html', build_render_context(character_prediction, prediction_probability, quote))