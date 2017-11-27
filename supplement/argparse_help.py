import argparse


def main():
    parser = argparse.ArgumentParser(description='Process argument for parameter dictionary.')
    parser.add_argument('-g', '--gpu', help='cuda visible devices')
    parser.add_argument('-t', '--test', action='store_true')
    parser.add_argument('-s', '--sample', help='sample selection')
    # experiment
    parser.add_argument('-R', '--rotation', action='store_true')
    parser.add_argument('-d', '--dice', choices=['value', 'softmax'], help='dice type')
    parser.add_argument('-r', '--regularization', action='store_true')
    parser.add_argument('-n', '--network', choices=['unet', 'dilated'], help='network option')
    parser.add_argument('--epoch', help='training epochs')
    parser.add_argument('--save_interval', help='save interval')
    parser.add_argument('--test_interval', help='test interval')
    parser.add_argument('--memory', help='memory usage for unlimited usage')
    _ = parser.parse_args()


if __name__ == '__main__':
    main()