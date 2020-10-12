from django.shortcuts import render, redirect
from .models import Stock
from.forms import StockCreateForm, StockSearchForm


def home(request):
    title = "Welcome to home page"
    context = {
        'title': title
    }
    return render(request, 'home.html', context)


def list_item(request):
    header = "List of Items"
    form = StockSearchForm(request.POST or None)
    if request.method == 'POST':
        queryset = Stock.objects.filter(category__icontains=form['category'].value(), item_name__icontains=form['item_name'].value())
    else:
        queryset = Stock.objects.all()
    context = {
        "form": form,
        'header': header,
        'queryset': queryset
    }
    return render(request, 'list_items.html', context)


def add_items(request):
    form = StockCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/list_items')
    context = {
        "form": form,
        "title": "Add item",
    }
    return render(request, "add_items.html", context)
