from django.shortcuts import render
from django.http import JsonResponse


def getRoutes(request):

    routes = [
        'api/products/',
        'api/products/upload/',
        'api/products/<id>/reviews/',
        'api/products/top/',
        'api/products/<id>/',

        'api/products/delete/<id>/',
        'api/products/<update>/<id>/',
    ]

    return JsonResponse(routes, safe=False)


def getProducts(request):
    
    products = [
        {
            'name': 'Product 1',
            'price': 200,
            'image': '/images/airpods.jpg',
            'brand': 'Apple',
            'rating': 4.5,
            'numReviews': 10,
            'countInStock': 6,
        },
        {
            'name': 'Product 2',
            'price': 250,
            'image': '/images/phone.jpg',
            'brand': 'Apple',
            'rating': 4.0,
            'numReviews': 10,
            'countInStock': 6,
        },
        {
            'name': 'Product 3',
            'price': 250,
            'image': '/images/camera.jpg',
            'brand': 'Apple',
            'rating': 4.8,
            'numReviews': 17,
            'countInStock': 6,
        }
    ]

    return JsonResponse(products, safe=False)