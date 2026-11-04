# -*- coding: utf-8 -*-
"""Erzeugt die statischen HTML-Seiten von Clavis IT Service.

Aufruf (im Projektordner):  python -B _generator/build.py
Die HTML-Dateien landen im Projektordner (eine Ebene über diesem Ordner).
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

from core import page, write_icons  # noqa: E402
from pages1 import PAGES1  # noqa: E402
from pages2 import PAGES2  # noqa: E402
from legal import PAGES3  # noqa: E402

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(HERE)

write_icons(os.path.join(OUT, "assets", "img", "icons.svg"))
for fn, title, desc, body, active, head in PAGES1 + PAGES2 + PAGES3:
    with open(os.path.join(OUT, fn), "w", encoding="utf-8", newline="\n") as f:
        f.write(page(fn, title, desc, body, active=active, extra_head=head))
    print("geschrieben:", fn)
