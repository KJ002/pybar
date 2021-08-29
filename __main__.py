import yaml

def main():
    with open('$HOME/.config/pybar/config') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)

    print(config)

if __name__ == '__main__':
    main()
