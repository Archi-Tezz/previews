# -*- coding: utf-8 -*-
"""Собирает корневой index.html со списком всех превью-папок."""
import os, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
USER = "Archi-Tezz"
REPO = "previews"

skip = {".git", "__pycache__"}
projects = sorted(
    d for d in os.listdir(ROOT)
    if os.path.isdir(os.path.join(ROOT, d))
    and not d.startswith((".", "_"))
    and d not in skip
    and os.path.exists(os.path.join(ROOT, d, "index.html"))
)

cards = "\n".join(
    f'      <a class="card" href="{p}/"><span class="name">{p}</span>'
    f'<span class="go">Открыть →</span></a>' for p in projects
) or '      <p class="empty">Пока пусто — добавьте папку с index.html.</p>'

html = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ARCHI — демо-стенд</title>
<style>
  :root{{ --bg:#14171b; --card:#1b1f25; --line:#2b313a; --txt:#f2f4f7; --mut:#8b94a1; --acc:#3ddc97; }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:var(--bg);color:var(--txt);font:16px/1.6 "Segoe UI",system-ui,sans-serif}}
  .wrap{{max-width:900px;margin:0 auto;padding:72px 24px}}
  .mark{{display:flex;align-items:center;gap:14px;margin-bottom:10px}}
  .bar{{width:4px;height:36px;background:var(--acc);border-radius:2px}}
  h1{{font-size:28px;letter-spacing:.16em;font-weight:700}}
  .sub{{color:var(--mut);font-size:15px;letter-spacing:.08em;margin-bottom:48px;padding-left:18px}}
  .list{{display:grid;gap:12px}}
  .card{{display:flex;justify-content:space-between;align-items:center;
         background:var(--card);border:1px solid var(--line);border-radius:10px;
         padding:20px 24px;text-decoration:none;color:var(--txt);transition:.15s}}
  .card:hover{{border-color:var(--acc);transform:translateY(-1px)}}
  .name{{font-weight:600}}
  .go{{color:var(--mut);font-size:14px}}
  .empty{{color:var(--mut)}}
  footer{{color:var(--mut);font-size:13px;margin-top:56px;border-top:1px solid var(--line);padding-top:22px}}
</style>
</head>
<body>
  <div class="wrap">
    <div class="mark"><div class="bar"></div><h1>ARCHI</h1></div>
    <div class="sub">ДЕМО-СТЕНД · РАБОТЫ НА ПРОСМОТРЕ</div>
    <div class="list">
{cards}
    </div>
    <footer>Обновлено {datetime.date.today().strftime('%d.%m.%Y')}</footer>
  </div>
</body>
</html>
"""

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print(f"index.html собран, проектов: {len(projects)}")
for p in projects:
    print(f"  https://{USER.lower()}.github.io/{REPO}/{p}/")
