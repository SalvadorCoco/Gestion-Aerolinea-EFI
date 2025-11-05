import pytest

from apps.accounts.models import Account
from django.urls import reverse


# Testea que liste los usuarios correctamente
@pytest.mark.django_db 
def test_get_all_accounts(api_client):
    user_1 = Account.objects.create_user(username='account1', email='acc1@test.com')
    user_2 = Account.objects.create_user(username='account2', email='acc2@test.com', is_active=False)

    url = reverse('account-list')
    response = api_client.get(url)
    body = response.json()

    assert response.status_code == 200
    assert body == [
        {
            'username': user_1.username,
            'email': user_1.email,
            'first_name': '',
            'last_name': '',
            'is_active': True,
            'pk': user_1.pk,
            'role_id': None,
        },
        {
            'username': user_2.username,
            'email': user_2.email,
            'first_name': '',
            'last_name': '',
            'is_active': user_2.is_active,
            'pk': user_2.pk,
            'role_id': None,
        }
    ]

# Testea que si no hay usuarios, devuelva una lista vacia
@pytest.mark.django_db
def test_get_all_accounts_empty_account(api_client):
    url = reverse('account-list')
    response = api_client.get(url)
    body = response.json()

    assert response.status_code == 200
    assert body == []

# Testea la cantidad de usuarios devueltos
@pytest.mark.django_db
def test_get_all_accounts_with_11_account(api_client):
    for x in range(11):
        Account.objects.create_user(username=f'account{x}', email=f'acc{x}@test.com')

    url = reverse('account-list')
    response = api_client.get(url)
    body = response.json()

    assert response.status_code == 200
    assert len(body) == 11

# Testea la creacion de un usuario llamando a /api/accounts/ [POST]
""" {
    "username": "",
    "email": "",
    "first_name": "",
    "last_name": "",
    "is_active": false,
    "password": "",
    "role_id": null
} """
@pytest.mark.django_db
def test_account_create(api_client):

    accounts = Account.objects.all()
    assert accounts.count() == 0

    payload = {
        "username": "test_account",
        "email": "test_account@test.com",
        "first_name": "Test Name",
        "last_name": "Test Lastname",
        "is_active": True,
        "password": "test123",
        "role_id": None
    }
    url = reverse('account-list')
    response = api_client.post(url, data=payload, format='json')

    body = response.json()
    accounts = Account.objects.all()
    user = accounts.first()

    assert response.status_code == 201
    assert 'password' not in body
    assert body['username'] == payload['username']
    assert body['email'] == payload['email']
    assert body['first_name'] == payload['first_name']
    assert body['last_name'] == payload['last_name']
    assert body['is_active'] == payload['is_active']
    assert body['role_id'] == payload['role_id']

    assert accounts.count() == 1
    assert accounts.first().email == payload['email']

    assert user.check_password(payload['password']) is True


# Testea la recuperacion de un usuario llamando a /api/accounts/<int:pk>/ [GET]
@pytest.mark.django_db
def test_account_retrieve(api_client):
    
    user_1 = Account.objects.create_user(username='account1', email='acc1@test.com')
    user_2 = Account.objects.create_user(username='account2', email='acc2@test.com', is_active=False)

    url = reverse('account-detail', args=[user_2.pk])
    response = api_client.get(url)
    
    status = response.status_code
    body = response.json() 

    assert status == 200
    assert body['username'] == user_2.username
    assert body['email'] == user_2.email
    assert body['is_active'] == user_2.is_active 
    
# testea la recuperacion de un usuario que no existe llamando a /api/accounts/<int:pk>/ [GET]
@pytest.mark.django_db
def test_account_retrieve_account_not_found(api_client):
    url = reverse('account-detail', args=["99"])
    response = api_client.get(url)
    
    status = response.status_code
    body = response.json() 

    assert status == 404
    assert body['detail'] == "No Account matches the given query."

# testea la actualizacion de un usuario llamando a /api/accounts/<int:pk>/ [PUT]
@pytest.mark.django_db
def test_account_update_put(api_client):
    user = Account.objects.create_user(username='account', email='acc1@test.com', first_name='First', last_name='Last')
    payload = {
        "username": "updated_account",
        "email": "acc1@text.com",
        "first_name": "First",
        "last_name": "Last",
    }
    url = reverse('account-detail', args=[user.pk])
    response = api_client.put(url, data=payload, format='json')

    assert response.status_code == 200
    user.refresh_from_db()
    assert user.username == payload['username']
    assert user.last_name == payload['last_name']   

# testea la actualizacion de un usuario llamando a /api/accounts/<int:pk>/ [PATCH]
@pytest.mark.django_db
def test_account_update_patch(api_client):
    user = Account.objects.create_user(username='account1', email='acc1@test.com', first_name='First', last_name='Last')
    payload = {
        "username": "updated_account",
        "email": "acc1@text.com",
        "first_name": "First",
        "last_name": "Last",
    }
    url = reverse('account-detail', args=[user.pk])
    response = api_client.patch(url, data=payload, format='json')

    assert response.status_code == 200
    user.refresh_from_db()
    assert user.username == payload['username']
    assert user.last_name == payload['last_name']

# testea la desactivacion (soft delete) de un usuario llamando a /api/accounts/<int:pk>/ [DELETE]
@pytest.mark.django_db
def test_account_soft_delete(api_client):
    user = Account.objects.create_user(username='account1', email='acc1@test.com', first_name='First', last_name='Last', is_active=False)

    # En caso de que el usuario ya este desactivado
    url = reverse('account-detail', args=[user.pk])
    response = api_client.delete(url)
    body = response.json()
    assert response.status_code == 400
    assert body['detail'] == f"{user.username} is already deactivated."

    # En caso de que el usuario este activo
    user.is_active = True
    user.save()
    response = api_client.delete(url)
    body = response.json()
    assert response.status_code == 200
    assert body['detail'] == f"{user.username} deactivated successfully."


        