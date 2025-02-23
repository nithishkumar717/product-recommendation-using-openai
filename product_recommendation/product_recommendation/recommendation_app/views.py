from django.shortcuts import render

def product_list(request):
    # Dummy product data for demonstration
    products = [
        {'id': 1, 'name': 'Product A', 'price': 100, 'rating': 4.5},
        {'id': 2, 'name': 'Product B', 'price': 150, 'rating': 4.0},
        {'id': 3, 'name': 'Product C', 'price': 200, 'rating': 5.0},
    ]
    return render(request, 'product_list.html', {'products': products})
