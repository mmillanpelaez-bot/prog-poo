class Team:
    def __init__(self, name: str):
        self._name = name
        self._wins = 0
        self._losses = 0
        self._draws = 0

    @property
    def name(self) -> str:
        return self._name

    @property
    def points(self) -> int:
        return (self._wins * 3) + self._draws

    @property
    def matches_played(self) -> int:
        return self._wins + self._losses + self._draws

    def add_win(self):
        self._wins += 1

    def add_loss(self):
        self._losses += 1

    def add_draw(self):
        self._draws += 1

    def __str__(self) -> str:
        return f"{self._name} - W:{self._wins} D:{self._draws} L:{self._losses} (Points: {self.points})"
