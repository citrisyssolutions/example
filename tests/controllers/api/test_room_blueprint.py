from unittest import TestCase
from unittest import mock
from application.app import app

EXAMPLE_ROOM = {"room_id": 1, "room_name": "TestRoom", "room_type": "Delux"}


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
        self.assertEqual(response.json, expected_response)

    @mock.patch("booking.repositories.room.RoomRepository.insert", return_value=EXAMPLE_ROOM)
    def test_add_new_room(self, *mocks) -> None:
        # Arrange
        url = "/api/room/"
        input = {"room_name": "TestRoom", "room_type": "Delux"}
        expected_response = EXAMPLE_ROOM

        # Act
        response = self.test_client.post(url, json=input)

        # Assert
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, expected_response)

    @mock.patch("booking.repositories.room.RoomRepository.insert", return_value=EXAMPLE_ROOM)
    def test_add_new_room_raise_error_if_room_type_missing(self, *mocks) -> None:
        # Arrange
        url = "/api/room/"
        input = {"room_name": "TestRoom"}
        expected_response = EXAMPLE_ROOM

        # Act
        response = self.test_client.post(url, json=input)

        # Assert
        self.assertEqual(response.status_code, 500)
