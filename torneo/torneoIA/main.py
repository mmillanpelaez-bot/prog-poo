import csv
from pathlib import Path
from typing import Dict, List, Optional

# ==========================================
# 1. DOMAIN MODELS (Lógica de negocio pura)
# ==========================================

class Team:
    """Represents a single team and its statistics."""
    
    def __init__(self, name: str):
        self.name: str = name
        self.wins: int = 0
        self.draws: int = 0
        self.losses: int = 0

    @property
    def points(self) -> int:
        """Calculates points dynamically: 3 per win, 1 per draw."""
        return (self.wins * 3) + self.draws

    @property
    def matches_played(self) -> int:
        return self.wins + self.draws + self.losses

    def __str__(self) -> str:
        # Formateo alineado para que la tabla en consola quede perfecta
        return f"{self.name:<12} | W:{self.wins:<2} D:{self.draws:<2} L:{self.losses:<2} | Pts: {self.points}"


class Tournament:
    """Manages the tournament state, teams, and standings."""
    
    def __init__(self, name: str, max_teams: int):
        self.name: str = name
        self.max_teams: int = max_teams
        # Usamos un diccionario para búsquedas O(1) mucho más eficientes
        self._teams: Dict[str, Team] = {}

    def add_team(self, team_name: str) -> None:
        if len(self._teams) >= self.max_teams:
            raise ValueError(f"Cannot add '{team_name}'. Tournament is full ({self.max_teams} teams).")
        if team_name in self._teams:
            raise ValueError(f"Team '{team_name}' is already in the tournament.")
        
        self._teams[team_name] = Team(team_name)

    def get_team(self, name: str) -> Optional[Team]:
        # El método .get() de los diccionarios devuelve None si no encuentra la clave
        return self._teams.get(name)

    def get_all_teams(self) -> List[Team]:
        return list(self._teams.values())

    def register_match(self, home_name: str, away_name: str, home_score: int, away_score: int) -> None:
        """Core logic for updating team stats after a match."""
        home_team = self.get_team(home_name)
        away_team = self.get_team(away_name)

        if not home_team or not away_team:
            raise ValueError(f"Match rejected: '{home_name}' or '{away_name}' not found in tournament.")

        if home_score > away_score:
            home_team.wins += 1
            away_team.losses += 1
        elif home_score < away_score:
            home_team.losses += 1
            away_team.wins += 1
        else:
            home_team.draws += 1
            away_team.draws += 1

    def get_standings(self) -> List[Team]:
        """Returns teams sorted by points (descending) and then by name (alphabetically)."""
        # La tupla (-team.points, team.name) le dice a Python: "Ordena por puntos de mayor a menor, y si empatan, por nombre de la A a la Z"
        return sorted(self.get_all_teams(), key=lambda team: (-team.points, team.name))


# ==========================================
# 2. PARSERS & IMPORTERS (Manejo de datos externos)
# ==========================================

class MatchParser:
    """Handles parsing strings and files into match data for the tournament."""

    @staticmethod
    def parse_match_string(result_str: str, tournament: Tournament) -> None:
        """Parses 'TeamA-TeamB ScoreA-ScoreB' and registers it."""
        try:
            teams_part, scores_part = result_str.strip().split()
            home_name, away_name = teams_part.split('-')
            home_score, away_score = map(int, scores_part.split('-'))
            
            tournament.register_match(home_name, away_name, home_score, away_score)
        except ValueError as e:
            raise ValueError(f"Invalid format: '{result_str}'. Expected 'TeamA-TeamB 1-0'. Details: {e}")

    @staticmethod
    def import_from_file(file_path: str | Path, tournament: Tournament, is_csv: bool = False) -> int:
        """Reads a file (TXT or CSV) and imports matches. Returns the number of matches imported."""
        path = Path(file_path) # pathlib es la forma moderna y segura de manejar rutas en Python
        if not path.is_file():
            raise FileNotFoundError(f"File not found: {path.absolute()}")

        matches_imported = 0
        with path.open('r', encoding='utf-8') as file:
            if is_csv:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) >= 4:
                        # Asumiendo CSV: Home, Away, ScoreHome, ScoreAway
                        tournament.register_match(row[0].strip(), row[1].strip(), int(row[2]), int(row[3]))
                        matches_imported += 1
            else:
                for line in file:
                    clean_line = line.strip()
                    if clean_line:
                        MatchParser.parse_match_string(clean_line, tournament)
                        matches_imported += 1
                        
        return matches_imported


# ==========================================
# 3. USER INTERFACE (Capa de presentación)
# ==========================================

class TournamentCLI:
    """Command Line Interface to interact with the Tournament."""
    
    def __init__(self, tournament: Tournament):
        self.tournament = tournament

    def print_menu(self):
        print("\n" + "="*30)
        print(f"🏆 {self.tournament.name.upper()} MANAGER")
        print("="*30)
        print("1. Register match result (Manual)")
        print("2. Import results from TXT")
        print("3. Show standings")
        print("4. Team statistics")
        print("5. Exit")
        print("="*30)

    def run(self):
        while True:
            self.print_menu()
            choice = input("Select an option: ").strip()

            try:
                match choice:
                    case "1":
                        result = input("Enter result (e.g., Celta-Betis 2-1): ")
                        MatchParser.parse_match_string(result, self.tournament)
                        print("✅ Match registered successfully.")
                    
                    case "2":
                        filepath = input("Enter TXT file path: ")
                        count = MatchParser.import_from_file(filepath, self.tournament)
                        print(f"✅ Imported {count} matches successfully.")
                    
                    case "3":
                        print("\n📊 CURRENT STANDINGS")
                        for i, team in enumerate(self.tournament.get_standings(), 1):
                            print(f"{i:2d}. {team}")
                    
                    case "4":
                        name = input("Enter team name: ")
                        team = self.tournament.get_team(name)
                        if team:
                            print(f"\n📈 Stats for {team.name}:")
                            print(f"Matches played: {team.matches_played}")
                            print(f"Win Rate: {(team.wins / team.matches_played * 100) if team.matches_played else 0:.1f}%")
                        else:
                            print("❌ Team not found.")
                    
                    case "5":
                        print("Exiting gracefully... Bye! 👋")
                        break
                    
                    case _:
                        print("❌ Invalid option. Please select 1-5.")
            
            # Un catch global para que la aplicación nunca "explote" de golpe
            except Exception as e:
                print(f"⚠️ Error: {e}")


# ==========================================
# 4. ENTRY POINT (Arranque de la aplicación)
# ==========================================
if __name__ == "__main__":
    # 1. Configurar el torneo
    my_tournament = Tournament("Campionato Castelao", max_teams=6)
    
    # 2. Añadir equipos (manejando posibles errores de capacidad)
    initial_teams = ["Celta", "Sevilla", "Español", "Girona", "Villareal", "Betis"]
    for team_name in initial_teams:
        my_tournament.add_team(team_name)

    # 3. Arrancar la interfaz y pasarle el torneo (Dependency Injection)
    app = TournamentCLI(my_tournament)
    app.run()