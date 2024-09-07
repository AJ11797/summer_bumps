class Rower:
    def __init__(self, name: str, points: float, start_pos: int, sort_by: int):
        self.name = name
        self.points = float(points)
        self.start_position = int(start_pos)
        self.finish_position = int(start_pos)
        self.active = True
        self.sort_by = int(sort_by)

    def __lt__(self, other):
        return self.finish_position < other.finish_position

    def __str__(self):
        return self.name
