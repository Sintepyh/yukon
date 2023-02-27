from django.shortcuts import redirect
from django.views.generic import ListView, DetailView, CreateView
from .models import Product
from .forms import ProductForm

class ProductListView(ListView):
    model = Product
    template_name = 'products/products_home.html'
    context_object_name = 'products'
    ordering = ['-date']

class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/products_detail.html'
    context_object_name = 'product'

class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/create.html'
    success_url = '/'

    def form_invalid(self, form):
        return super().form_invalid(form)
