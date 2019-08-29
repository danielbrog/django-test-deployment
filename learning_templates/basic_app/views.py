from django.shortcuts import render
from basic_app.models import Hit
from . import forms

# Create your views here.
def index(request):
    form = forms.NameSearch()
    data = Hit.objects.order_by('date')
    

    if request.method == 'POST':
        form = forms.NameSearch(request.POST)
        if form.is_valid():
            data = Hit.objects.filter(battername__icontains=form.data['name'])


    context_dict = {'hit_data':data, 'form':form}

    return render(request,'basic_app/index.html', context=context_dict)

def other(request):
    return render(request, 'basic_app/other.html')

def relative(request):
    return render(request,'basic_app/relative_url_templates.html')

def batterInfo(request, id):
    data = Hit.objects.filter(batterid__exact=id)
    context_dict={'hit_data':data}

    return render(request,'basic_app/hit_table.html', context=context_dict)