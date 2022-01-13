from django.shortcuts import render
from matplotlib.style import context
from sympy import content
#from django.http import HttpResponse
from .form import MyForm
# Create your views here.
def index(request):
    form = MyForm
    context={'form':form}
    if request.method == 'GET':
        return render(request,'home.html',context)
    if request.method =='POST':
        form.save()
        context={'form':form}
        return render(request,'home.html',context)
        #if 'to_do' not in request.session:
        #    request.session['to_do'] = []
        #new_item = request.POST.get('new_item')
        #to_do_list = request.session['to_do']
        #to_do_list.append(new_item)
        #request.session['to_do'] = to_do_list
        #return render(request, 'home.html', { 'to_do_list': to_do_list })
#    return HttpResponse("Hello I'm SA110a")
