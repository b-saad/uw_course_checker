import pytest

def test_handler(app):
    result = app.handler(None, None)

    assert result["status"]
