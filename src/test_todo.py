from fastapi.testclient import TestClient

from main import app

client = TestClient(app)
ID = None


def test_create_todo_view():
    endpoint = "/to-do/"
    data = {
        "title": "test",
        "description": "test description"
    }
    response = client.post(endpoint, json=data)
    assert response.status_code == 200
    global ID
    ID = response.json()['id']
    assert response.json() == {
        'id': ID,
        'title': "test",
        'description': 'test description'
    }


def test_todo_list():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()[-1].get('title'), "test"
    assert response.json()[-1].get('description'), "test description"


def test_get_todo_view():
    response = client.get("/to-do/" + str(ID))
    assert response.status_code == 200
    assert response.json() == {
        'id': ID,
        'title': "test",
        'description': 'test description'
    }


def test_update_todo_view():
    data = {'id': ID,
            'title': 'updated task',
            'description': 'updated description'
            }
    response = client.put("/to-do/", json=data)
    assert response.status_code == 200
    assert response.json() == data
    assert response.json() == {
        'id': ID,
        'title': "updated task",
        'description': 'updated description'
    }


def test_delete_todo_view():
    endpoint = "/to-do/" + str(ID)
    response = client.delete(endpoint)
    assert response.status_code == 200
    assert response.json() == {"message": "ToDo item successfully deleted"}
