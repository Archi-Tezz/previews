# -*- coding: utf-8 -*-
"""Собирает корневой index.html: выполненные работы + демо-страницы."""
import os, datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
USER, REPO = "Archi-Tezz", "previews"

# Выполненные работы — живые сайты по внешним ссылкам.
# Добавлять сюда: ("Название", "https://адрес", "короткое пояснение")
WORKS = [
    ("Farmila Stats", "https://45-138-73-155.sslip.io", "Веб-сервис статистики · свой сервер, домен, SSL"),
]

skip = {".git", "__pycache__"}
demos = sorted(
    d for d in os.listdir(ROOT)
    if os.path.isdir(os.path.join(ROOT, d))
    and not d.startswith((".", "_"))
    and d not in skip
    and os.path.exists(os.path.join(ROOT, d, "index.html"))
)

def card(href, name, note, external=False):
    tag = '<span class="tag">вживую</span>' if external else ""
    rel = ' target="_blank" rel="noopener"' if external else ""
    return (f'      <a class="card" href="{href}"{rel}>\n'
            f'        <span class="left"><span class="name">{name}{tag}</span>'
            f'<span class="note">{note}</span></span>\n'
            f'        <span class="go">Открыть →</span>\n      </a>')

works_html = "\n".join(card(u, n, note, True) for n, u, note in WORKS)
demos_html = "\n".join(card(f"{d}/", d, "демонстрационная страница") for d in demos) \
             or '      <p class="empty">Пока пусто.</p>'

def section(title, body):
    return f'    <div class="head">{title}</div>\n    <div class="list">\n{body}\n    </div>'

blocks = []
if WORKS:
    blocks.append(section("ВЫПОЛНЕННЫЕ РАБОТЫ", works_html))
blocks.append(section("ДЕМОНСТРАЦИОННЫЕ СТРАНИЦЫ", demos_html))

html = f"""<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ARCHI — работы</title>
<style>
  :root{{ --bg:#14171b; --card:#1b1f25; --line:#2b313a; --txt:#f2f4f7; --mut:#8b94a1; --acc:#3ddc97; }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:var(--bg);color:var(--txt);font:16px/1.6 "Segoe UI",system-ui,sans-serif}}
  .wrap{{max-width:900px;margin:0 auto;padding:72px 24px}}
  .mark{{display:flex;align-items:center;gap:14px;margin-bottom:10px}}
  .bar{{width:4px;height:36px;background:var(--acc);border-radius:2px}}
  h1{{font-size:28px;letter-spacing:.16em;font-weight:700}}
  .sub{{color:var(--mut);font-size:15px;letter-spacing:.08em;margin-bottom:52px;padding-left:18px}}
  .head{{color:var(--mut);font-size:12px;letter-spacing:.18em;margin:0 0 14px;font-weight:600}}
  .list{{display:grid;gap:12px;margin-bottom:44px}}
  .card{{display:flex;justify-content:space-between;align-items:center;gap:16px;
         background:var(--card);border:1px solid var(--line);border-radius:10px;
         padding:18px 24px;text-decoration:none;color:var(--txt);transition:.15s}}
  .card:hover{{border-color:var(--acc);transform:translateY(-1px)}}
  .left{{display:flex;flex-direction:column;gap:3px;min-width:0}}
  .name{{font-weight:600;display:flex;align-items:center;gap:10px}}
  .tag{{font-size:11px;font-weight:600;letter-spacing:.08em;color:var(--acc);
        border:1px solid rgba(61,220,151,.35);border-radius:4px;padding:2px 7px}}
  .note{{color:var(--mut);font-size:14px}}
  .go{{color:var(--mut);font-size:14px;white-space:nowrap}}
  .empty{{color:var(--mut)}}
  footer{{color:var(--mut);font-size:13px;border-top:1px solid var(--line);padding-top:22px}}
  @media(max-width:560px){{ .wrap{{padding:48px 18px}} .go{{display:none}} }}
</style>
</head>
<body>
  <div class="wrap">
    <div class="mark"><div class="bar"></div><h1>ARCHI</h1></div>
    <div class="sub">РАЗРАБОТКА САЙТОВ · ВЁРСТКА · PHP / MYSQL</div>
{chr(10).join(blocks)}
    <footer>Обновлено {datetime.date.today().strftime('%d.%m.%Y')}</footer>
  </div>
</body>
</html>
"""

with open(os.path.join(ROOT, "index.html"), "w", encoding="utf-8") as f:
    f.write(html)

print(f"работ: {len(WORKS)}, демо: {len(demos)}")
