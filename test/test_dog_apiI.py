import requests
import pytest

@pytest.mark.parametrize('count', [1, 3, 50], ids=['one_message', 'three_messages', 'fifty_messages'])
def test_count_number_of_messages(count):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{count}")
    assert response.json()
    assert len(response.json()["message"]) == count
    assert response.status_code == 200

@pytest.mark.parametrize('count', [1, 3, 50], ids=['one_message', 'three_messages', 'fifty_messages'])
def test_200_success_code_response(count):
    response = requests.get(f"https://dog.ceo/api/breeds/image/random/{count}")
    assert response.status_code == 200
    assert response.json()
    assert response.json()["status"] == "success"

def test_max_50_number_of_message():
    response = requests.get("https://dog.ceo/api/breeds/image/random/51")
    assert response.status_code == 200
    assert len(response.json()["message"]) == 50
    assert response.json()

def test_image_urls_not_equal():
    url = "https://dog.ceo/api/breeds/image/random"

    response_first_image = requests.get(url)
    json_first_image = response_first_image.json()
    message_first_image = json_first_image["message"]

    response_second_image = requests.get(url)
    json_second_image = response_second_image.json()
    message_second_image = json_second_image["message"]

    assert message_first_image != message_second_image



def test_randon_breeds_image():
    response = requests.get("https://dog.ceo/api/breed/african/images/random")
    json = response.json()
    assert response.status_code == 200
    assert "message" in json
    assert json["message"] != ""
    assert json["status"] == "success"


def test_dog_breed_images_contain_name():
    response = requests.get("https://dog.ceo/api/breed/hound/afghan/images")
    assert response.status_code == 200
    for data in response.json()["message"]:
        assert "afghan" in data, "Отсутствует признак породы в ссылках с картинками"
