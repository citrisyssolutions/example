from unittest import TestCase
from application.exception.errors import ValidationError

from application.dto.request.room.add_room import AddRoomRequest

class TestAddRoomRequest(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_validate_all_params(self):
        # Arrange
        room_type = "Delux"
        room_name = "This is room"

        # Act
        add_room_dto = AddRoomRequest(
            room_type=room_type,
            room_name=room_name
        )

        # Assert
        self.assertEqual("Delux", add_room_dto.room_type)

    def test_raise_error_if_property_missing(self):
        # Arrange
        room_name = "This is room"

        # Act
        with self.assertRaises(Exception) as context:
            add_room_dto = AddRoomRequest(
                room_name=room_name
            )

        # Assert
        self.assertTrue(TypeError == context.exception.__class__)

    def test_raise_error_if_wrong_room_type_passed(self):
        # Arrange
        room_name = "This is room"
        room_type = "Dummy"

        # Act
        with self.assertRaises(Exception) as context:
            add_room_dto = AddRoomRequest(
                room_name=room_name,
                room_type=room_type
            )

        # Assert
        self.assertTrue(ValidationError == context.exception.__class__)
