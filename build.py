#!/usr/bin/env python3
"""Builds public/index.html from src/index.src.html, data/data.json and assets/*.webp.

    python3 build.py              -> public/index.html
    python3 build.py --artifact   -> also dist/artifact.html (body-only version for claude.ai)
"""
import base64, os, re, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
P = lambda *a: os.path.join(ROOT, *a)


def b64(name):
    with open(P('assets', name + '.webp'), 'rb') as f:
        return base64.b64encode(f.read()).decode()


def put(s, tag, value, count=1):
    assert s.count(tag) == count, f'{tag}: expected {count}, found {s.count(tag)}'
    return s.replace(tag, value)


def build():
    s = open(P('src', 'index.src.html'), encoding='utf-8').read()
    s = put(s, '/*DATA*/null', open(P('data', 'data.json'), encoding='utf-8').read().strip())
    s = put(s, '/*IMG*/', b64('urchin'))
    s = put(s, '/*KELP*/', b64('kelp'), 2)
    s = put(s, '/*JON*/', b64('jon'))
    for k in ('p1', 'p2', 'p3'):
        s = put(s, '/*' + k.upper() + '*/', b64(k))
    s = s.replace("    set('count', null); // placeholder to keep id in map\n", '').replace('  shown.count = null;\n', '')
    os.makedirs(P('public'), exist_ok=True)
    open(P('public', 'index.html'), 'w', encoding='utf-8').write(s)
    print('public/index.html', len(s))
    return s


def artifact(s):
    title = re.search(r'<title>.*?</title>', s, re.S).group(0)
    links = ''.join(l for l in re.findall(r'<link[^>]*>\n?', s) if 'fonts.g' in l)
    style = re.search(r'<style>.*?</style>', s, re.S).group(0)
    body = re.search(r'<body>(.*)</body>', s, re.S).group(1)
    style = put(style, '  html { background: var(--paper); }', '  html { background: var(--paper); color-scheme: light; }')
    style = put(style, '  body { color: var(--ink);', '  body { background: var(--paper); color: var(--ink);')
    out = title + '\n' + links + style + '\n' + body.strip() + '\n'
    os.makedirs(P('dist'), exist_ok=True)
    open(P('dist', 'artifact.html'), 'w', encoding='utf-8').write(out)
    print('dist/artifact.html', len(out))


if __name__ == '__main__':
    html = build()
    if '--artifact' in sys.argv:
        artifact(html)
