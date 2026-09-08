#!/usr/bin/env python3
"""Check static HTML references before publishing; standard library only."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids = set()
        self.references = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if identifier := attrs.get('id'):
            if identifier in self.ids:
                self.errors.append(f'Duplicate ID: {identifier}')
            self.ids.add(identifier)
        for key in ('href', 'src'):
            if reference := attrs.get(key):
                self.references.append(reference)
        if tag == 'img' and not attrs.get('alt'):
            self.errors.append('Image without descriptive alt text')


def main():
    page = Page()
    page.feed((ROOT / 'index.html').read_text())
    for reference in page.references:
        url = urlsplit(reference)
        if url.scheme or url.netloc:
            continue
        if url.path and not (ROOT / unquote(url.path)).is_file():
            page.errors.append(f'Missing asset: {reference}')
        if not url.path and url.fragment and unquote(url.fragment) not in page.ids:
            page.errors.append(f'Missing anchor: {reference}')
    if page.errors:
        raise SystemExit('\n'.join(page.errors))
    print(f'Checked {len(page.references)} references and {len(page.ids)} unique IDs.')


if __name__ == '__main__':
    main()
