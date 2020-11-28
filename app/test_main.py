from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {
        "Name": "Deniss Kashin",
        "Project": "Numbersapi test assignment",
        "Version": "0.0.1",
        "Time spent": "4 hours"
    }


def test_fragment():
    response = client.get("/fragment/5?data_type=trivia&default=default&not_found=floor")
    assert response.status_code == 200
    json = response.json()
    assert json['found']
    assert json['number'] == 5
    assert json['type'] == 'trivia'
    assert 'text' in json and len(json['text']) > 0


def test_fragment_date():
    response = client.get("/fragment_date/2/10")
    assert response.status_code == 200
    json = response.json()
    assert json['found']
    assert json['type'] == 'date'
    assert 'year' in json
    assert 'text' in json and len(json['text']) > 0


def test_random():
    response = client.get("random/10/20")
    assert response.status_code == 200
    json = response.json()
    assert json['found']
    assert json['type'] == 'trivia'
    assert 'number' in json and json['number'] >= 10 and json['number'] <= 20
    assert 'text' in json and len(json['text']) > 0


def test_batch_math():
    response = client.get("batch/1..3,10?data_type=math")
    assert response.status_code == 200
    json = response.json()
    assert '1' in json and '2' in json and '3' in json and '10' in json
    assert len(json['1']) > 0 and len(json['2']) > 0 and len(json['2']) > 0 and len(json['10']) > 0


def test_batch_trivia_by_default():
    response = client.get("batch/1..3,10")
    assert response.status_code == 200
    json = response.json()
    assert '1' in json and '2' in json and '3' in json and '10' in json
    assert len(json['1']) > 0 and len(json['2']) > 0 and len(json['2']) > 0 and len(json['10']) > 0


def test_batch_failed_if_str():
    response = client.get("batch/a..c,z")
    assert response.status_code == 400
