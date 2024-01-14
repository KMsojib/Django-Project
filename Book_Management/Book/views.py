from django.shortcuts import render
from Book.forms import BookStoreForm
# Create your views here.
def home(request):
    return render(request,'upload_book.html')


def StoreBook(request):
    book = BookStoreForm()
    return render(request,'upload_book.html',{'Book': book})