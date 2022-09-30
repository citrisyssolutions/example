from unittest import TestCase

from booking.dto.request.room.add_room import AddRoomRequest

class TestAddRoomRequest(TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        pass

    def test_validate_all_params(self):
        # Assign
        add_room_dto = AddRoomRequest(
            room_type="Delux",
            room_name="This is room"
        )
        # Action

        # Assert
        self.assertEqual("Delux", add_room_dto.room_type)