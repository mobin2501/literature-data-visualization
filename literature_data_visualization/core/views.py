import json

from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Book


class HistogramView(TemplateView):
    template_name = 'core/pages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Book.objects.all()
        data = [{"title": book.title, "pages": book.pages} for book in books]
        context['data'] = json.dumps(data)
        return context


class DemoHistogramView(TemplateView):
    template_name = 'core/demo_page.html'


def demo_view(request):
    books = Book.objects.all().values('pages', 'title')
    return JsonResponse(list(books), safe=False)
