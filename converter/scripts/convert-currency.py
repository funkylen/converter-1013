import argparse
from converter.convertercur import run


def main():
    parser = argparse.ArgumentParser(description='Перевод единиц измерения')

    parser.add_argument('--out_of', required=True, type=int)
    parser.add_argument('--to', required=True, type=int)
    parser.add_argument('--value', required=True, type=float)

    args = parser.parse_args()

    print(run(args.out_of, args.to, args.value))


if __name__ == '__main__':
    main()
