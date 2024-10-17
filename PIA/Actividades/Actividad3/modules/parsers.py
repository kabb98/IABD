import json
import yaml
from pathlib import Path

class JSONParser:
    
    @staticmethod
    def read_file(path: Path):
        with open(path, 'r') as f:
            return json.load(f)
    
    @staticmethod
    def write_file(out_path: Path, data: dict):
        out_data = json.dumps(data, indent=4)
        with open(out_path, 'w') as f:
            json.dump(out_data, f)

class YAMLParser:
    
    def read_file(self, path: str):
        with open(path, 'r') as f:
            return yaml.safe_load(f)
    
    def write_file(self, out_path: str, data: dict):
        with open(out_path, 'w') as f:
            yaml.dump(data, f)