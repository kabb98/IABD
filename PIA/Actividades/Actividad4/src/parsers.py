from pathlib import Path
import yaml

class Parser:
    @staticmethod
    def parse(path: Path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)
