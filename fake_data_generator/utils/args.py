import argparse


def get_args():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        '--no_users',
        '--nu',
        type=int,
        default=100,
        help='Number of users to generate.',
    )
    parser.add_argument(
        '--no_products',
        '--np',
        type=int,
        default=1000,
        help='Number of products to generate.',
    )
    parser.add_argument(
        '--no_events',
        '--ne',
        type=int,
        default=1_000_000,
        help='Maximum number of events to generate.',
    )
    return parser.parse_args()
