from django import forms

from django.forms import ModelForm
from .models import Order

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
import datetime #for checking renewal date range.


# class RenewBookForm(forms.Form):
#     renewal_date = forms.DateField(help_text="Enter a date between now and 4 weeks (default 3).")
#
#     def clean_renewal_date(self):
#         data = self.cleaned_data['renewal_date']
#
#         # Check date is not in past.
#         if data < datetime.date.today():
#             raise ValidationError(_('Invalid date - renewal in past'))
#
#         # Check date is in range librarian allowed to change (+4 weeks).
#         if data > datetime.date.today() + datetime.timedelta(weeks=4):
#             raise ValidationError(_('Invalid date - renewal more than 4 weeks ahead'))
#
#         # Remember to always return the cleaned data.
#         return data

class OrderForm(forms.Form):
    fund_id = forms.CharField(label='基金代码', help_text="请输入基金代码。")
    trade_direction = forms.ChoiceField(choices=Order.DIRECTIONS, label='交易方向', help_text="请选择买入还是卖出基金。")
    trading_share = forms.IntegerField(label='交易份额', help_text="请输入交易份额。")

