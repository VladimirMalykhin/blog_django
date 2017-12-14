import pytest
from todo_app.models import Blog
from django.contrib import auth
from django.contrib.auth.models import User


def create_test_user():
    u1 = User.objects.create_user(username='test', password='test')
    return u1


def create_test_users():
    u1 = auth.authenticate(username='vova', password='Xtvgbjy12')
    return u1


@pytest.mark.django_db
def test_list_view(client):
    response = client.get('/')
    assert response.status_code == 200
    author = 'vova'
    obj = Blog.objects.filter(author=author)
    assert obj.count() == 0


@pytest.mark.django_db
def test_create_view(client):
    u1 = create_test_user()
    client.force_login(u1)
    response = client.post('/create/', {'title': 'asd2', 'body': 'asd'})
    response2 = client.get('/create/')
    obj = Blog.objects.get(title='asd2')
    assert obj.id > 0
    assert response.status_code == 200
    assert response2.status_code == 200


@pytest.mark.django_db
def test_view(client):

    check_id = 6
    response = client.get('/view/' + str(check_id))
    response2 = client.post('/view/' + str(check_id))
    assert response.status_code == 301
    assert response2.status_code == 301


@pytest.mark.django_db
def test_edit_article(client):
    u1 = create_test_user()
    client.force_login(u1)

    test_name = 'test'
    client.post('/create/', {
        'title': test_name,
        'body': test_name,
    })
    obj = Blog.objects.get(title=test_name)

    edit_name = 'another_test_name'
    client.post('/update/' + str(obj.id) + '/', {
        'title': edit_name,
        'body': test_name,
    })

    new_obj = Blog.objects.get(id=obj.id)
    assert new_obj.title == edit_name


@pytest.mark.django_db
def test_delete_article(client):
    u1 = create_test_user()
    client.force_login(u1)

    test_name = 'test'
    client.post('/create/', {
        'title': test_name,
        'body': test_name,
    })
    obj = Blog.objects.get(title=test_name)

    address = '/delete/' + str(obj.id) + '/'
    client.post(address)
    response = client.get('/delete/' + str(6))
    assert response.status_code == 301
