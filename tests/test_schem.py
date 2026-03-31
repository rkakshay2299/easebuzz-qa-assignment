from pydantic import BaseModel


class PostSchema(BaseModel):
    userId: int
    id: int
    title: str
    body: str


def test_schema_validation(get_response):
    response = get_response("/posts")
    data = response.json()

    for post in data:
        PostSchema(**post)