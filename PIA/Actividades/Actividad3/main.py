
from modules.parsers import JSONParser, YAMLParser
from pathlib import Path

def main():
    jsonParser = JSONParser.read_file(Path('data.json'))
    print(jsonParser)

if __name__ == '__main__':
    main()
