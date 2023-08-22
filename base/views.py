from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Account, Card
from .serializers import UserSerializer, AccountSerializer, CardSerializer
from rest_framework.views import APIView
from rest_framework import status
from django.http import Http404
# Create your views here.

@api_view(['GET'])
def endpoints(request):
  data = [
    '/users',
    '/users/:id',
    '/accounts',
    '/accounts/:id',
    '/cards',
    '/cards/:id',
    'account-transaction/<int:pk>',
    'card-transaction/<int:pk>'
  ]
  return Response(data)


class UsersList(APIView):
  def get(self, request, format=None):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class UserDetail(APIView):
  """
  Retrieve, update or delete a user instance.
  """
  def get_object(self, pk):
      try:
          return User.objects.get(pk=pk)
      except User.DoesNotExist:
          raise Http404

  def get(self, request, pk, format=None):
      user = self.get_object(pk)
      serializer = UserSerializer(user)
      return Response(serializer.data)

  def put(self, request, pk, format=None):
      user = self.get_object(pk)
      serializer = UserSerializer(user, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      user = self.get_object(pk)
      user.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  
  
class AccountsList(APIView):
  def get(self, request, format=None):
    accounts = Account.objects.all()
    serializer = AccountSerializer(accounts, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = AccountSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class AccountDetail(APIView):
  """
  Retrieve, update or delete a user instance.
  """
  def get_object(self, pk):
      try:
          return Account.objects.get(pk=pk)
      except Account.DoesNotExist:
          raise Http404

  def get(self, request, pk, format=None):
      account = self.get_object(pk)
      serializer = AccountSerializer(account)
      return Response(serializer.data)

  def put(self, request, pk, format=None):
      account = self.get_object(pk)
      serializer = AccountSerializer(account, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      account = self.get_object(pk)
      account.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
  
  
class CardsList(APIView):
  def get(self, request, format=None):
    cards = Card.objects.all()
    serializer = CardSerializer(cards, many=True)
    return Response(serializer.data)

  def post(self, request, format=None):
    serializer = CardSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class CardDetail(APIView):
  """
  Retrieve, update or delete a user instance.
  """
  def get_object(self, pk):
      try:
          return Card.objects.get(pk=pk)
      except Card.DoesNotExist:
          raise Http404

  def get(self, request, pk, format=None):
      card = self.get_object(pk)
      serializer = CardSerializer(card)
      return Response(serializer.data)

  def put(self, request, pk, format=None):
      card = self.get_object(pk)
      serializer = CardSerializer(card, data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

  def delete(self, request, pk, format=None):
      card = self.get_object(pk)
      card.delete()
      return Response(status=status.HTTP_204_NO_CONTENT)
    
@api_view(['PUT'])
def make_account_transaction(request, pk):
  print('make_account_transaction pk ', pk)
  account = Account.objects.get(pk=pk)
  t_type = request.data['t_type']
  amount = request.data['amount']
  
  if t_type.upper() == 'OUTCOME' and amount >= account.balance:
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
  if t_type.upper() == 'INCOME':
    account.balance += amount 
  
  if t_type.upper() == 'OUTCOME' :
    account.balance -= amount 
  
  account.save()
  serializer = AccountSerializer(account, many=False)
  return Response(serializer.data)
    
@api_view(['PUT'])
def make_card_transaction(request, pk):
  card = Card.objects.get(pk=pk)
  t_type = request.data['t_type']
  amount = request.data['amount']
  
  if t_type.upper() == 'OUTCOME' and amount >= card.balance:
    return Response(status=status.HTTP_400_BAD_REQUEST)
  
  if t_type.upper() == 'INCOME':
    card.balance += amount 
  
  if t_type.upper() == 'OUTCOME':
    card.balance -= amount 
  
  card.save()
  serializer = CardSerializer(card, many=False)
  return Response(serializer.data)
  
  
