from apps.accounts.models import Account
from rest_framework import serializers


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False, allow_blank=False)

    class Meta:
        model = Account
        fields = ['pk', 'username', 'email', 'first_name', 'last_name', 'is_active', 'password', 'role_id']

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        account = Account(**validated_data)
        if password:
            account.set_password(password) # Hashea la contraseña si es que la hay
        else:
            account.set_password(Account.objects.make_random_password()) # Genera una contraseña aleatoria si no la hay
        account.save()
        return account
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance