from src import score_averages
import json

def main(targets):
    if 'data' in targets:
        with open('config/config.json') as fp:
            params = json.load(fp)
        score_averages(**params)

if __name__ == '__main__':
    targets = sys.argv[1:]
    main(targets)