import argparse
import sys

from . import airbank, cnb, storage
from .compare import convert, spread_pct


def load():
    c = cnb.fetch()
    try:
        a = airbank.fetch()
    except airbank.NotConfigured as e:
        print(f"! {e} Zobrazuji jen ČNB.\n", file=sys.stderr)
        a = {}
    return c, a


def cmd_list(args):
    c, a = load()
    codes = [args.code.upper()] if args.code else sorted(c)
    day = next(iter(c.values())).day
    print(f"Kurzy ČNB k {day:%d.%m.%Y}\n")
    print(f"{'Měna':<5}{'ČNB':>10}{'AB nákup':>11}{'AB prodej':>11}{'spread':>9}")
    for code in codes:
        if code not in c:
            sys.exit(f"Neznámá měna: {code}")
        r, ab = c[code], a.get(code)
        if ab:
            sp = spread_pct(ab.sell, r.mid)
            print(f"{code:<5}{r.mid:>10.3f}{ab.buy:>11.3f}{ab.sell:>11.3f}{sp:>8.2f}%")
        else:
            print(f"{code:<5}{r.mid:>10.3f}{'-':>11}{'-':>11}{'-':>9}")
    storage.save(c)
    if a:
        storage.save(a)


def cmd_convert(args):
    c, a = load()
    code = args.code.upper()
    rate = a.get(code) or c[code]
    czk = convert(args.amount, rate, to_czk=True)
    print(f"{args.amount:g} {code} = {czk:,.2f} CZK ({rate.source})")


def main():
    p = argparse.ArgumentParser(prog="kurzy")
    sub = p.add_subparsers(dest="cmd")
    l = sub.add_parser("list", help="tabulka kurzů")
    l.add_argument("code", nargs="?")
    pr = sub.add_parser("prevod", help="přepočet do CZK")
    pr.add_argument("amount", type=float)
    pr.add_argument("code")
    args = p.parse_args()
    {"prevod": cmd_convert}.get(args.cmd, cmd_list)(
        args if args.cmd else p.parse_args(["list"]))


if __name__ == "__main__":
    main()
