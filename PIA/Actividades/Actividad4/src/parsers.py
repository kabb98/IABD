from pathlib import Path
import yaml

class Parser:

    def __init__(self) -> None:
        Path('../output').mkdir(parents=True, exist_ok=True)
    
    @staticmethod
    def parse(path: Path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)
