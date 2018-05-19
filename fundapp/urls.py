from django.urls import include, path
from . import views

app_name = 'fundapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('funds/', views.FundListView.as_view(), name='funds'),
    path('fund/<int:pk>', views.FundDetailView.as_view(), name='fund-detail'),
]


urlpatterns += [
    path('myorders/', views.OrdersByUserListView.as_view(), name='my-orders'),
]


urlpatterns += [
    path('fund/create/', views.FundCreate.as_view(), name='fund_create'),
    path('fund/<int:pk>/update/', views.FundUpdate.as_view(), name='fund_update'),
    path('fund/<int:pk>/delete/', views.FundDelete.as_view(), name='fund_delete'),
]