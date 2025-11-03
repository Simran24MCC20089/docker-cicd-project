from app.utils import get_greeting

def test_greeting():
    assert "Hello" in get_greeting("Simran")
    assert "Guest" in get_greeting("")
