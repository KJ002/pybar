import yaml
from pathlib import Path

def main():

    with open(str(Path.home()) + '/.config/pybar/config') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    print(config)

if __name__ == '__main__':
    main()
