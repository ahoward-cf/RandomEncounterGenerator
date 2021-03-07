import pandas as pd
from pathlib import Path


class table:
    """Container for the encounter table and associated functions"""

    def __init__(self, filename):
        """Loads an existing encounter table"""
        self.filename = filename
        if Path(self.filename).is_file():
            self.table = self.f_load_table()
        else:
            self.table = self.f_create_new_table()

    def f_load_table(self):
        """loads an existing encounter table from a file"""
        table = pd.read_csv(self.filename)
        return(table)

    def f_create_new_table(self):
        """creates a new, blank, encounter table"""
        table = pd.DataFrame(
            columns=['Encounter Name', 'CR', 'Environment', 'Rarity', 'Notes'])
        self.f_save_table()
        return(table)

    def f_save_table(self):
        """saves an encounter table to a file"""
        self.table.to_csv(self.filename, index=False)
