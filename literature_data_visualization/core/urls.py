from django.urls import path
from .views import HistogramView
from .views import DemoHistogramView
from .views import demo_view

urlpatterns = [
    path('histogram/', HistogramView.as_view(), name='histogram'),
    path('demo/books/', DemoHistogramView.as_view(), name='histogram'),
    path('demo/api/', demo_view, name='book_data'),

]
