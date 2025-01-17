import argparse
import scraper
import formatter
from tabulate import tabulate


def main():
    parser = argparse.ArgumentParser(description="Slash")
    parser.add_argument('--search', type=str, help='Product search query')
    parser.add_argument('--num', type=int, help="Maximum number of records", default=3)
    parser.add_argument('--sort', type=str, nargs='+', help="Sort according to re (relevance: default), pr (price) or ra (rating)", default="re")
    parser.add_argument('--link', action='store_true', help="Show links in the table")
    parser.add_argument('--des', action='store_true', help="Sort in descending (non-increasing) order")
    args = parser.parse_args()
    
    products1 = scraper.searchAmazon(args.search)
    products2 = scraper.searchWalmart(args.search)

    for sortBy in args.sort:
        products1 = formatter.sortList(products1, sortBy, args.des)[:args.num]
        products2 = formatter.sortList(products2, sortBy, args.des)[:args.num]
        results = products1 + products2
        results = formatter.sortList(results, sortBy, args.des)


    print()
    print()
    print(tabulate(results, headers="keys", tablefmt="github"))
    print()
    print()

if __name__ == '__main__':
    main()