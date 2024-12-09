from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Book, BorrowRequest
from .forms import BorrowRequestForm

@login_required
def index(request):
    return render(request, 'library/index.html')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library/book_list.html', {'books': books})

@login_required
def borrow_request_list(request):
    borrow_requests = BorrowRequest.objects.filter(user=request.user)
    return render(request, 'library/borrow_request_list.html', {'borrow_requests': borrow_requests})

@login_required
def borrow_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BorrowRequestForm(request.POST)
        if form.is_valid():
            borrow_request = form.save(commit=False)
            borrow_request.user = request.user
            borrow_request.book = book
            borrow_request.save()
            return redirect('borrow_request_list')
    else:
        form = BorrowRequestForm()
    return render(request, 'library/borrow_book.html', {'form': form, 'book': book})
