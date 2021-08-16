from django.urls import path
from .views import (
	price_list_view,
	price_create,
	price_detail,
	price_update,
	price_delete
	)

urlpatterns = [
    path('list/', price_list_view , name='price_list'),
    path('new/', price_create , name='price_new'),
    path('<int:id>/', price_detail , name='price_detail'),
    path('<int:id>/edit', price_update , name='price_update'),
    path('<int:id>/delete', price_delete , name='price_delete'),
    ]