import csv


class ResultImporter:
    """
    Utility class dedicated solely to reading files and importing
    results into a given Tournament instance.
    """

    @staticmethod
    def from_txt(file_path: str, tournament) -> int:
        """
        Imports results from a TXT file.
        Expected format per line: 'Home-Away HomeScore-AwayScore'
        """
        matches_imported = 0
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    clean_line = line.strip() # Removes invisible characters like \n
                    if clean_line:            # Skips completely empty lines
                        tournament.register_match(clean_line)
                        matches_imported += 1
            print(f"Success: Imported {matches_imported} matches from TXT.")
            
        except FileNotFoundError:
            print(f"Error: The file '{file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            
        return matches_imported

    @staticmethod
    def from_csv(file_path: str, tournament) -> int:
        """
        Imports results from a CSV file.
        Expected format per row: HomeTeam,AwayTeam,HomeScore,AwayScore
        """
        matches_imported = 0
        try:
            with open(file_path, 'r', newline='', encoding='utf-8') as file:
                reader = csv.reader(file)
                next(reader, None) # Skip header if present

                for row in reader:
                    # Defensive programming: ensure the row has exactly 4 columns
                    if len(row) == 4:
                        home, away, score_h, score_a = row
                        
                        # We format it to match what tournament.register_match expects
                        formatted_result = f"{home.strip()}-{away.strip()} {score_h.strip()}-{score_a.strip()}"
                        tournament.register_match(formatted_result)
                        matches_imported += 1
                    else:
                        print(f"Warning: Skipping malformed row -> {row}")
                        
            print(f"Success: Imported {matches_imported} matches from CSV.")
            
        except FileNotFoundError:
            print(f"Error: The CSV file '{file_path}' was not found.")
        except Exception as e:
            print(f"An unexpected error occurred reading the CSV: {e}")
            
        return matches_imported