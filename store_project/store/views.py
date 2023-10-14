from django.shortcuts import render
from .models import Product, Category, Order



def product_list(request):
    category_list = Category.objects.all()
    search_query = request.GET.get('search', None)
    if search_query:
        product_list = Product.objects.filter(title__icontains=search_query)
    else:
        product_list = Product.objects.all()
    return render(
        request, 
        "store/product_list.html", 
        context={'product_list': product_list, 'category_list': category_list}
    )

def product_detail(request, pk):
    category_list = Category.objects.all()
    product = Product.objects.get(pk=pk)
    return render(
        request, 
        "store/product_detail.html", 
        context={'product': product, 'category_list': category_list}
    )

def category_detail(request, pk):
    category_list = Category.objects.all()
    category = Category.objects.get(pk=pk)
    return render(
        request, 
        "store/category_detail.html", 
        context={'category': category, 'category_list': category_list}
    )

def save_order(request):
    category_list = Category.objects.all()

    order = Order.objects.create(
        user_name = request.POST['user_name'],
        user_email = request.POST['user_email'],
        product_id = request.POST['product_id']
    )
    return render(request, 
        "store/save_order.html", 
        context={'category_list': category_list, 'order': order}
    )

