from django.urls import path
from . import views

app_name = "spravochniki"

urlpatterns = [
    path('book-cbv/<int:pk>/', views.BookView.as_view(), name="view-book"),    
    path('book-delete-cbv/<int:pk>/', views.BookDeleteView.as_view(), name="delete-book"),
    path('book-list-cbv/', views.BookListView.as_view(), name="list-book"),   
    path('book-add-cbv/', views.BookCreateView.as_view(), name="add-book"),
    path('book-update-cbv/<int:pk>/', views.BookUpdateView.as_view(), name="update-book"),
    path('added/', views.succes_page, name="success-page"),
    path('send-email/', views.send_email, name="send-email"),
    

]