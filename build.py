#!/usr/bin/env python3
"""Build index.html (public GitHub Pages site) from app/vestiaire-rm2.html (the Claude artifact source)."""
from pathlib import Path

root = Path(__file__).parent
body = (root / "app" / "vestiaire-rm2.html").read_text(encoding="utf-8")
config = (root / "firebase-config.json").read_text(encoding="utf-8").strip() if (root / "firebase-config.json").exists() else "null"
body = body.replace("const FIREBASE_CONFIG = null;", f"const FIREBASE_CONFIG = {config};", 1)

page = f"""<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#111a2c">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}[hidden]{{display:none!important}}</style>
</head>
<body>
{body}
</body>
</html>
"""
(root / "index.html").write_text(page, encoding="utf-8")
print("index.html built", "with Firebase" if config != "null" else "WITHOUT Firebase config (read-only)")
