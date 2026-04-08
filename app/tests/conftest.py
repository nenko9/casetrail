import pytest
import os

os.environ["DATABASES"]="/app/db.sqlite3"
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings")

@pytest.fixture
def pages():
    pages=[
        "/",
        "/home",
        "/documents",
        "/about",
    ]
    return pages