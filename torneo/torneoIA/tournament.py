from team import Team


class Tournament:
    def __init__(self, name: str, max_teams: int):
        self._name = name
        self._max_teams = max_teams
        self._teams = []

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def teams(self) -> list:
        return self._teams

    def get_team(self, name: str) -> Team | None:
        for team in self._teams:
            if team.name == name:
                return team
        return None

    def add_team(self, team: Team) -> bool:
        """Adds a team to the tournament if there is capacity and it's not a duplicate."""
        if len(self._teams) < self._max_teams and team not in self._teams:
            self._teams.append(team)
            return True
        return False

    def register_match(self, match_result: str):
        """
        Registers a match result from a string.
        Format expected: 'Home-Away HomeScore-AwayScore' (e.g., 'Celta-Betis 2-1')
        """
        try:
            teams_part, scores_part = match_result.split()
            home_name, away_name = teams_part.split('-')
            home_score, away_score = map(int, scores_part.split('-'))

            home_team = self.get_team(home_name)
            away_team = self.get_team(away_name)

            if not home_team or not away_team:
                raise ValueError(f"Team not found in tournament: {home_name} or {away_name}")

            if home_score > away_score:
                home_team.add_win()
                away_team.add_loss()
            elif home_score < away_score:
                home_team.add_loss()
                away_team.add_win()
            else:
                home_team.add_draw()
                away_team.add_draw()

        except ValueError as e:
            print(f"Error registering match: {e}")
        except Exception:
            print("Invalid format. Please use 'Home-Away Score-Score'.")

    def get_standings(self) -> list:
        """Returns the list of teams sorted by points in descending order."""
        # Clean Code: Let Python handle the sorting natively.
        return sorted(self._teams, key=lambda team: team.points, reverse=True)
