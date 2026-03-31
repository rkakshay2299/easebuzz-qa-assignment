



def test_status_code(get_response):
    response = get_response("/posts")
    assert response.status_code == 200


def test_response_time(get_response):
    response = get_response("/posts")
    assert response.elapsed.total_seconds() < 2