from unittest import TestCase
from booking.app import app

class TestRoomBlueprint(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        return super().setUpClass()
    
    def setUp(self) -> None:
        self.test_client = app.test_client()

    def test_get_room_list(self) -> None:
        # Arrange
        url = "/api/room/"
        expected_response = [{"id": 1, "name": "Room #1"}]

        # Act
        response = self.test_client.get(url)

        # Assert
        self.assertEqual(response.json ,expected_response)