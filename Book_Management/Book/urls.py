from django.urls import path
from Book.views import home,StoreBook

urlpatterns = [
    path('',home),
    path('StoreBook/',StoreBook,name="Uploadbook")
]

#class="bg-white border-gray-200 dark:bg-gray-900"
# upload,show book,about us, contact