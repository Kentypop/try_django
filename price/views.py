from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Price
from .forms import PriceForm
from django.contrib.auth.models import User


# Create your views here.
def price_list_view(request):
	#List out all price 
	context={
		#This is one way to sort, but lets use model manager
		#'prices': Price.objects.all().order_by('-price')
		'prices': Price.objects.all().maxtomin()
	}
	return render(request, 'price/price_list.html', context)

@staff_member_required
def price_create(request):
	#Create object
	form= PriceForm(request.POST)
	if not request.user.is_superuser or not request.user.is_staff:
		return redirect('price_list')
	if form.is_valid():
			obj= form.save(commit=False)
			#obj.author = User.objects.get(pk=request.user.id)
			obj.author = request.user
			obj.save()
			return redirect('price_list')
	return render(request, 'price/price_create.html', {'form': form})	

def price_detail(request, id):
	#Another way of loading, using et_object_or_404 shows page not found if request failed
	#obj= Price.objects.get(id=id)
	obj= get_object_or_404(Price, id=id)
	context= {'object': obj}
	return render(request, 'price/price_detail.html', context)

@staff_member_required
def price_update(request, id):
	#Look up the object
	obj= get_object_or_404(Price, id=id)
	#instance= obj need to pass the instance to form in order to update
	form= PriceForm(request.POST or None, instance= obj)
	if form.is_valid():
		form.save()
	context={'form': form, "name": f"Update {obj.name}"}
	return render(request, 'price/price_create.html', context )

@staff_member_required
def price_delete(request, id):
	obj= get_object_or_404(Price, id=id)
	form= PriceForm(request.POST or None)
	if request.method == 'POST':
		obj.delete()
		return redirect('price_list')
	context= {'object': obj}
	return render(request, 'price/price_delete.html', context)		
