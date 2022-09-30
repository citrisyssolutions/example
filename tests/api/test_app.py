from unittest import TestCase
from booking.app import app

class TestApp(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    def setUp(self) -> None:
        self.test_client = app.test_client()

    def test_ping(self) -> None:
        # Arrange
        url = "/api/ping"

        # Act
        response = self.test_client.get(url)

        # Assert
        self.assertEqual(response.status_code,200)