from django.urls import path

from .views import BranchesApiView, BankApiView
 

urlpatterns = [
    path('branches/autocomplete/', BranchesApiView.as_view()),
    path('branches/', BankApiView.as_view()),
]