import pytest


@pytest.mark.parametrize("endpoint", [
    "/posts",
    "/comments",
    "/users"
])
def test_multiple_endpoints(get_response, endpoint):
    response = get_response(endpoint)
    assert response.status_code == 200 , "Expected 200 but got different status"