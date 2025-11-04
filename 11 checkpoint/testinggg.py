# ...existing code...
#!/usr/bin/env python3
import sys
import argparse

try:
    from emoji import emojize
except ImportError:
    print("Missing dependency: run `pip install emoji`", file=sys.stderr)
    sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Emojize text (convert :alias: to emoji).")
    parser.add_argument('text', nargs='*', help='Text to emojize. If omitted, reads stdin.')
    parser.add_argument('-l', '--language', default='alias', help='emoji language (default: alias)')
    args = parser.parse_args()

    if args.text:
        text = ' '.join(args.text)
    else:
        text = sys.stdin.read()
        if not text:
            parser.print_help()
            sys.exit(0)

    print(emojize(text, language=args.language))

if __name__ == '__main__':
    main()