from pathlib import Path
import yaml

class Parser:

    def __init__(self) -> None:
        Path('../output').mkdir(parents=True, exist_ok=True)

    def parse(self, path: Path):
        with open(path, 'r') as file:
            return yaml.safe_load(file)

parser = Parser()
print(parser.parse(Path('config.yml')))