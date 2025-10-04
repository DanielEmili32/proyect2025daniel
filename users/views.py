from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.urls import reverse_lazy
from users.models import Product

# Vista de prueba
def test_view(request):
    return HttpResponse("<h1>¡Hola! Esta es una vista de prueba.</h1>")

def home(request):
    user = request.user
    context = {
        'title': 'Proyecto 2025',
        'message': 'Bienvenido al proyecto de prueba'
    }
    return render(request, 'home.html', context)

def welcome(request):
    return render(request, "base.html")

def about(request):
    context = {
        "products": Product.objects.filter(is_active=True)
    }
    return render(request, "about.html", context=context)

def create_product(request):
    if request.method == "GET":
        return render(request, "product/create.html")
    else:
        product = Product()
        product.name = request.POST.get('name_product', '')
        # validar/conversión segura del stock
        try:
            product.stock = int(request.POST.get('stock_product', 0))
        except (TypeError, ValueError):
            product.stock = 0
        product.save()
        return redirect(reverse_lazy("about"))

@require_POST
def delete_product(request, pk):
    """
    Borrado suave: marca is_active=False para que deje de aparecer en about.
    """
    # Opcional: restringir por permisos
    # if not request.user.is_staff:
    #     return HttpResponseForbidden()

    product = get_object_or_404(Product, pk=pk)
    product.is_active = False
    product.save()
    messages.success(request, f'Producto \"{product.name}\" eliminado correctamente.')
    return redirect(reverse_lazy('about'))
