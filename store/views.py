from .models import Product, Order
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.views.generic import (
    ListView, DetailView,
     CreateView, DeleteView,
     UpdateView
     )
# Create your views here.

def home(request):
    return render(request, 'store/home.html')

def about(request):
    return render(request, 'store/about.html')


# Product Classes

class ProductListView(ListView):
    model = Product
    template_name = 'store/product/product_list.html'
    context_object_name = 'products'
    ordering = ['-pk']
    paginate_by=2

class ProductCreateView(CreateView):
    model = Product
    fields = ["ProductName", "SupplierId", "UnitPrice"]
    template_name = 'store/product/product_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

class ProductDetailView(DetailView):
    model = Product
    template_name = 'store/product/product_detail.html'

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["ProductName", "SupplierId", "UnitPrice"]
    template_name = 'store/product/product_form.html'

    def form_valid(self, form):
            return super().form_valid(form)

# class ProductDeleteView(DeleteView):
#     model = Product
#     success_url = '/'
#     context_object_name = 'product'
#     template_name = "'store/product/product_confirm_delete.html"

#     def get_object(self):
#         id_ = self.kwargs.get("id")
#         return get_object_or_404(Product, id=id_)
    

def delete_product_view(request, id):
    obj = get_object_or_404(Product, id = id)
    context ={"product": obj}
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "store/product/product_confirm_delete.html", context)



# Order Classes

class OrderListView(ListView):
    model = Order
    template_name = 'store/order/order_list.html'
    context_object_name = 'orders'
    ordering = ['-OrderDate']
    paginate_by=2


class OrderDetailView(DetailView):
    model = Order
    template_name = 'store/order/order_detail.html'

class OrderCreateView(CreateView):
    model = Order
    fields = ["OrderDate", "OrderNumber", "CustomerId", "TotalAmount"]
    template_name = 'store/order/order_form.html'

    def form_valid(self, form):
        return super().form_valid(form)

class OrderUpdateView(UpdateView):
    model = Order
    fields = ["OrderDate", "OrderDate", "CustomerId", "TotalAmount"]
    template_name = 'store/order/order_form.html'

    def form_valid(self, form):
            return super().form_valid(form)

def delete_order_view(request, id):
    obj = get_object_or_404(Order, id = id)
    context ={"Order": obj}
 
    if request.method =="POST":
        obj.delete()
        return HttpResponseRedirect("/")
 
    return render(request, "store/order/order_confirm_delete.html", context)

