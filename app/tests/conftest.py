import pytest


@pytest.fixture
def pages():
    pages=[
        "login",
        "home",
        "documents",
        "about",
    ]
    return pages