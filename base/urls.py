from django.urls import path
from . import views


urlpatterns = [
    path('', views.endpoints),
    path('users', views.UsersList.as_view()),
    path('users/<int:pk>', views.UserDetail.as_view()),
    path('accounts', views.AccountsList.as_view()),
    path('accounts/<int:pk>', views.AccountDetail.as_view()),
    path('cards', views.CardsList.as_view()),
    path('cards/<int:pk>', views.CardDetail.as_view()),
    path('account-transaction/<int:pk>', views.make_account_transaction),
    path('card-transaction/<int:pk>', views.make_card_transaction),
    
]