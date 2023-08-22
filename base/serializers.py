from rest_framework.serializers import ModelSerializer
from .models import User, Account, Card
        
class UserSerializer(ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'
        
class AccountSerializer(ModelSerializer):
  user = UserSerializer()
  class Meta:
    model = Account
    fields = ['id','balance', 'user']
        
class CardSerializer(ModelSerializer):
  account = AccountSerializer()
  class Meta:
    model = Card
    fields = ['id','balance', 'account']