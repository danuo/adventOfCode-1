class Seat:
    def __init__(self, coordinates: tuple[int, int]):
        self._adjacent_seats = dict()
        self._coordinates = coordinates
        self.is_empty = True
        self.is_empty_next = None

    def update_state(self):
        self.is_empty = self.is_empty_next

    def add_adjacent_seat(self, seat: "Seat"):
        coords = seat.coordinates
        self._adjacent_seats.update({coords: seat})

    @property
    def coordinates(self):
        return self._coordinates

    @property
    def adjacent_seats(self):
        return self._adjacent_seats
