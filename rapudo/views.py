from django.shortcuts import render
from.models import Product
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def test(request):
    return render(request,'test.html')


def insertProducts (request):
    if request.method == 'POST':
        product_name = request.POST['product_name']
        product_price = request.POST['product_price']
        product_description = request.POST['product_description']
        # product_image = request.FILES['product_image']

        product = Product(product_name=product_name,
                          product_price=product_price,
                          product_description=product_description)
        product.save()

    return render(request,'insert-products.html')




