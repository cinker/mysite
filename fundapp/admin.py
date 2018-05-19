from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Order, FundInfo, FundPara, FundTrade, Trader

admin.site.register(Order)
admin.site.register(FundInfo)
admin.site.register(FundTrade)
admin.site.register(FundPara)
admin.site.register(Trader)