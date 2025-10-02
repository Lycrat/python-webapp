import pytest
from application.data_access import *
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_connection():
    with patch('application.data_access.get_connection') as mock_get_connection:
        mock_conn = MagicMock()
        mock_cursor = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
        mock_get_connection.return_value = mock_conn
        yield mock_cursor


def test_get_joke(mock_connection):
    mock_connection.fetchone.return_value = (1, "Why did the chicken cross the road?", "To get to the other side!")
    result = get_joke()
    assert result == (1, "Why did the chicken cross the road?", "To get to the other side!")
    mock_connection.execute.assert_called_once_with("SELECT * FROM vGetJokes ORDER BY RAND()")


def test_get_jokes_count(mock_connection):
    mock_connection.fetchone.return_value = (42,)
    result = get_jokes_count()
    assert result == (42,)
    mock_connection.execute.assert_called_once_with("SELECT COUNT(*) FROM jokes")

def test_add_joke_to_database(mock_connection):
    setup = "Why did the scarecrow win an award?"
    punchline = "Because he was outstanding in his field!"
    add_joke_to_database(setup, punchline)
    mock_connection.execute.assert_called_once_with("CALL pAddJoke(%s, %s);", (setup, punchline))

def test_add_user(mock_connection):
    username = "test_user"
    password = "secure_password"
    add_user(username, password)
    mock_connection.execute.assert_called_once_with("CALL pAddUser(%s, %s);", (username, password))

def test_get_user(mock_connection):
    username = "test_user"
    mock_connection.fetchone.return_value = (1, "test_user", "hashed_password")
    result = get_user(username)
    assert result == (1, "test_user", "hashed_password")
    mock_connection.execute.assert_called_once_with("SELECT * FROM users WHERE username = %s", (username,))