from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

from .models import FundInfo



def index(request):
    latest_fund_list = FundInfo.objects.all()[:5]
    context = {
        'latest_fund_list': latest_fund_list,
    }
    return render(request, 'fundapp/index.html', context)

