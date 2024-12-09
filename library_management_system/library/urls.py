from django.urls import path
from .views import index, book_list, borrow_request_list, borrow_book

app_name = 'library'
urlpatterns = [
    path('', index, name='index'),
    path('books/', book_list, name='book_list'),
    path('borrow-requests/', borrow_request_list, name='borrow_request_list'),
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
]
