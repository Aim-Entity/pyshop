from django.shortcuts import render
from .models import Item
from .filters import ItemFilter
from django.views.generic import ListView, DetailView


class ItemList(DetailView):
    model = Item
    template_name = "home/item.htm"


class VegetableList(ListView):
    model = Item
    template_name = "home/home.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Vegetable")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class FruitList(ListView):
    model = Item
    template_name = "home/fruit.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Fruit")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class DairyList(ListView):
    model = Item
    template_name = "home/dairy.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Dairy")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class MeatList(ListView):
    model = Item
    template_name = "home/meat.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Meat")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class SugarList(ListView):
    model = Item
    template_name = "home/sugar.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Sugar")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class BreadList(ListView):
    model = Item
    template_name = "home/bread.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Bread")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class PreList(ListView):
    model = Item
    template_name = "home/pre.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Pre-Packed")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class CanList(ListView):
    model = Item
    template_name = "home/can.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Can")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context


class MiscList(ListView):
    model = Item
    template_name = "home/misc.htm"
    paginate_by = 1

    def get_queryset(self):
        queryset = Item.objects.filter(category="Misc")

        if self.request.GET.get('category'):
            queryset = queryset.filter(price=self.request.GET.get('category'))
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = ItemFilter(
            self.request.GET, queryset=self.get_queryset())
        return context
