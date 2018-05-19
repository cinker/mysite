from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import FundInfo
from django.shortcuts import get_object_or_404
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import OrderForm
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Order
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views import generic
from django.urls import reverse_lazy


@login_required
def index(request):
    num_fund = FundInfo.objects.all().count()
    context = {'num_fund': num_fund}
    return render(
        request,
        'fundapp/index.html',
        context
    )

from django.contrib.auth.mixins import LoginRequiredMixin

class OrdersByUserListView(LoginRequiredMixin, generic.ListView):
    """
    Generic class-based view listing books on loan to current user.
    """
    model = Order
    template_name = 'fundapp/orders_list_by_user.html'
    paginate_by = 10

    def get_queryset(self):
        return Order.objects.filter(trader=self.request.user).order_by('trade_ts')


class NewOrder(PermissionRequiredMixin, CreateView):
    model = FundInfo
    # fields = ['fund_code', 'trade_direction', 'trading_share']
    fields = '__all__'
    # def form_valid(self, form):
    #     form.instance.trader = self.request.user
    #     return super().form_valid(form)

    permission_required = 'catalog.can_mark_returned'

class OrderListView(generic.ListView):
    """
    Generic class-based view for a list of orders.
    """
    model = FundInfo
    paginate_by = 10


class OrderDetailView(generic.DetailView):
    """
    Generic class-based detail view for a order.
    """
    model = FundInfo

#Classes created for the forms challenge
class FundCreate(PermissionRequiredMixin, CreateView):
    model = FundInfo
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class FundUpdate(PermissionRequiredMixin, UpdateView):
    model = FundInfo
    fields = '__all__'
    permission_required = 'catalog.can_mark_returned'

class FundDelete(PermissionRequiredMixin, DeleteView):
    model = FundInfo
    success_url = reverse_lazy('funds')
    permission_required = 'catalog.can_mark_returned'


# def new_order(request):
#     order_inst = get_object_or_404(Order)
#
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#
#         if form.is_valid():
#             order_inst.fund_id = form.cleaned_data['fund_id']
#             order_inst.trade_direction = form.cleaned_data['trade_direction']
#             order_inst.trading_share = form.cleaned_data['trading_share']
#             order_inst.save()
#
#             return HttpResponseRedirect(reversed('index'))
#     else:
#         form = OrderForm(initial={'trading_ts': datetime.datetime.now()})
#     return render(request, 'fundapp/order_form.html', {'form': form, 'Order_inst': Order_inst})
#
#
