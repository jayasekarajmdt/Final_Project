from django.shortcuts import render
from .models import freelancer

# Create your views here.
def Search(request):

    types = request.POST.get('type')

    flancer = freelancer.objects.all()

    context = {
        'users': flancer,
    }

    return render(request, 'freelancers/results.html', context)



def SearchByType(request):

    type = request.POST.get('types','')
    print(type)
    flancer_list=[]

    flancer = freelancer.objects.filter(types__contains=type)

    context = {
        'users': flancer,
    }

    return render(request, 'freelancers/results.html', context)


def SearchByTypeAndPrice(request):

    type = request.POST.get('types','')
    price=request.POST.get('price','')
    print(type)
    

    flancer = freelancer.objects.filter(types__contains=type).filter(price__gte=price)

    context = {
        'users': flancer,
    }

    return render(request, 'freelancers/results.html', context)



def SearchByTypeAndGender(request):

    type = request.POST.get('types','')
    prc=request.POST.get('gender','')
    flancer_list=[]
    print(type)
    
    
    flancer = freelancer.objects.filter(types__contains=type).filter(gender__contains=prc)

    context = {
        'users': flancer,
    }

    return render(request, 'freelancers/results.html', context)