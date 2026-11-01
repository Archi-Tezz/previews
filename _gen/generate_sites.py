# -*- coding: utf-8 -*-
"""Собирает демо-сайты из общего шаблона: разные ниши, цвета и темы."""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TPL = """<!doctype html>
<html lang="ru">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{brand} — {tagline}</title>
<style>
  :root{{ --bg:{bg}; --surf:{surf}; --line:{line}; --txt:{txt}; --mut:{mut}; --acc:{acc}; --on-acc:{on_acc}; }}
  *{{box-sizing:border-box;margin:0;padding:0}}
  body{{background:var(--bg);color:var(--txt);font:16px/1.65 {font};-webkit-font-smoothing:antialiased}}
  .wrap{{max-width:1080px;margin:0 auto;padding:0 28px}}
  header{{border-bottom:1px solid var(--line);position:sticky;top:0;background:var(--bg);z-index:5}}
  nav{{display:flex;align-items:center;justify-content:space-between;padding:20px 0}}
  .logo{{font-weight:800;letter-spacing:.2em;font-size:15px}}
  .links a{{color:var(--mut);text-decoration:none;margin-left:30px;font-size:15px}}
  .links a:hover{{color:var(--txt)}}
  .phone{{color:var(--acc);font-weight:600;margin-left:30px;text-decoration:none}}
  .hero{{padding:104px 0 88px;max-width:660px}}
  .eyebrow{{color:var(--acc);font-size:13px;letter-spacing:.2em;font-weight:700;margin-bottom:18px}}
  h1{{font-size:52px;line-height:1.1;letter-spacing:-.025em;margin-bottom:20px}}
  .lead{{color:var(--mut);font-size:19px;margin-bottom:36px}}
  .btn{{display:inline-block;background:var(--acc);color:var(--on-acc);font-weight:700;
        padding:16px 34px;border-radius:10px;text-decoration:none;font-size:16px}}
  .btn:hover{{filter:brightness(1.07)}}
  .ghost{{background:none;color:var(--txt);border:1px solid var(--line);margin-left:12px}}
  h2{{font-size:32px;letter-spacing:-.02em;margin-bottom:10px}}
  .sec-sub{{color:var(--mut);margin-bottom:38px}}
  section{{padding-bottom:92px}}
  .grid{{display:grid;grid-template-columns:repeat(3,1fr);gap:20px}}
  .card{{background:var(--surf);border:1px solid var(--line);border-radius:14px;padding:30px}}
  .card .ic{{width:40px;height:40px;border-radius:10px;background:var(--acc);opacity:.18;margin-bottom:18px}}
  .card h3{{font-size:18px;margin-bottom:8px}}
  .card p{{color:var(--mut);font-size:15px}}
  .price{{display:flex;justify-content:space-between;align-items:baseline;gap:20px;
          padding:20px 0;border-bottom:1px dashed var(--line)}}
  .price .n{{font-weight:600}}
  .price .d{{color:var(--mut);font-size:14px;flex:1}}
  .price .v{{font-weight:700;color:var(--acc);white-space:nowrap}}
  .band{{background:var(--surf);border:1px solid var(--line);border-radius:18px;
         padding:46px;display:flex;justify-content:space-between;align-items:center;gap:28px;flex-wrap:wrap}}
  .band h2{{margin-bottom:6px}}
  .band p{{color:var(--mut)}}
  form{{display:flex;gap:10px;flex-wrap:wrap}}
  input{{background:var(--bg);border:1px solid var(--line);color:var(--txt);
         padding:15px 18px;border-radius:10px;font:inherit;min-width:210px}}
  input:focus{{outline:none;border-color:var(--acc)}}
  button{{background:var(--acc);color:var(--on-acc);border:0;padding:15px 28px;
          border-radius:10px;font:inherit;font-weight:700;cursor:pointer}}
  footer{{border-top:1px solid var(--line);padding:30px 0;color:var(--mut);font-size:14px}}
  .fw{{display:flex;justify-content:space-between;gap:16px;flex-wrap:wrap;width:100%}}
  @media(max-width:860px){{ .grid{{grid-template-columns:1fr}} h1{{font-size:36px}}
    .links{{display:none}} .hero{{padding:64px 0 56px}} .band{{padding:30px}} }}
</style>
</head>
<body>
<header><div class="wrap"><nav>
  <span class="logo">{brand}</span>
  <span class="links">{nav}<a class="phone" href="tel:+70000000000">{phone}</a></span>
</nav></div></header>

<div class="wrap">
  <section class="hero">
    <div class="eyebrow">{eyebrow}</div>
    <h1>{h1}</h1>
    <p class="lead">{lead}</p>
    <a class="btn" href="#form">{cta}</a><a class="btn ghost" href="#price">Цены</a>
  </section>

  <section>
    <h2>{f_title}</h2>
    <p class="sec-sub">{f_sub}</p>
    <div class="grid">{cards}</div>
  </section>

  <section id="price">
    <h2>Цены</h2>
    <p class="sec-sub">Честный прайс без звёздочек и скрытых доплат</p>
    {prices}
  </section>

  <section id="form">
    <div class="band">
      <div><h2>{cta_title}</h2><p>{cta_sub}</p></div>
      <form id="lead">
        <input type="tel" placeholder="Ваш телефон" required>
        <button type="submit">{cta}</button>
      </form>
    </div>
  </section>
</div>

<footer><div class="wrap fw">
  <span>{brand} · {addr}</span><span>Демонстрационная страница · вёрстка ARCHI</span>
</div></footer>

<script>
document.getElementById("lead").addEventListener("submit", function (e) {{
  e.preventDefault();
  this.innerHTML = "<p>Заявка отправлена. Перезвоним в течение 15 минут.</p>";
}});
</script>
</body>
</html>
"""

DARK  = dict(bg="#14171b", surf="#1b1f25", line="#2b313a", txt="#f2f4f7", mut="#8b94a1", on_acc="#0f1114")
LIGHT = dict(bg="#fbfaf7", surf="#ffffff", line="#e6e3dc", txt="#1f2420", mut="#6b7169", on_acc="#ffffff")
SANS  = '"Segoe UI",system-ui,sans-serif'

SITES = [
  dict(slug="barbershop", theme=DARK, acc="#e0a33e", font=SANS,
       brand="КЛИНОК", tagline="барбершоп", phone="+7 495 000-00-00",
       nav=["Услуги", "Мастера", "Цены"], eyebrow="БАРБЕРШОП НА ПОКРОВКЕ",
       h1="Стрижка, после которой не надо ничего поправлять",
       lead="Четыре мастера, запись за день, кофе и тишина. Без очередей и без разговоров, если не хочется.",
       cta="Записаться", addr="Москва, Покровка 14",
       f_title="Почему к нам возвращаются", f_sub="Три причины, из которых складывается всё остальное",
       cards=[("Мастер закреплён", "Ходите к своему и не объясняете всё заново каждый раз."),
              ("Работаем до 22:00", "Успеете после работы, а в выходные открыты с десяти утра."),
              ("Не затягиваем", "Стрижка занимает 45 минут. Опоздали — всё равно примем.")],
       prices=[("Мужская стрижка", "машинка и ножницы, укладка", "1800 ₽"),
               ("Стрижка бороды", "моделирование, горячее полотенце", "1200 ₽"),
               ("Отец и сын", "две стрижки подряд", "2600 ₽"),
               ("Бритьё опасной бритвой", "классика, 40 минут", "1500 ₽")],
       cta_title="Запишитесь на удобное время", cta_sub="Перезвоним за 15 минут и подберём мастера"),

  dict(slug="autoservice", theme=DARK, acc="#4a9eff", font=SANS,
       brand="ОСЬ", tagline="автосервис", phone="+7 495 000-00-00",
       nav=["Услуги", "Цены", "Контакты"], eyebrow="АВТОСЕРВИС ПОЛНОГО ЦИКЛА",
       h1="Чиним так, чтобы вы вернулись только на ТО",
       lead="Диагностика при вас, согласование каждой работы до начала, гарантия два года на работы и детали.",
       cta="Записаться на диагностику", addr="Москва, Электрозаводская 21",
       f_title="Как мы работаем", f_sub="Никаких «разобрали — потом посчитаем»",
       cards=[("Смета до работ", "Называем сумму заранее. Выросла — звоним и спрашиваем."),
              ("Гарантия 2 года", "На работы и на детали, которые ставим сами."),
              ("Видеоотчёт", "Снимаем процесс и показываем, что именно меняли.")],
       prices=[("Компьютерная диагностика", "считывание ошибок, расшифровка", "1500 ₽"),
               ("Замена масла и фильтров", "работа без стоимости расходников", "1200 ₽"),
               ("Замена тормозных колодок", "одна ось, с проверкой дисков", "2400 ₽"),
               ("Развал-схождение", "3D стенд, печать протокола", "3000 ₽")],
       cta_title="Запишитесь на диагностику", cta_sub="Свободные места есть на завтра"),

  dict(slug="yoga", theme=LIGHT, acc="#7a9a6a", font=SANS,
       brand="ВДОХ", tagline="студия йоги", phone="+7 495 000-00-00",
       nav=["Расписание", "Направления", "Цены"], eyebrow="СТУДИЯ ЙОГИ В ЦЕНТРЕ",
       h1="Место, где можно наконец выдохнуть",
       lead="Маленькие группы до восьми человек, мягкий свет и преподаватели, которые помнят ваше имя.",
       cta="Пробное занятие", addr="Москва, Чистопрудный бульвар 9",
       f_title="Чем у нас иначе", f_sub="Студия, а не фитнес-клуб с ковриками",
       cards=[("Группы до 8 человек", "Преподаватель успевает подойти к каждому за занятие."),
              ("Первое занятие бесплатно", "Приходите без абонемента и без обязательств."),
              ("Коврики и блоки наши", "Приносить с собой ничего не нужно, душ в студии.")],
       prices=[("Первое занятие", "знакомство со студией", "бесплатно"),
               ("Разовое занятие", "любое направление", "900 ₽"),
               ("Абонемент на 8 занятий", "действует два месяца", "6000 ₽"),
               ("Индивидуальное занятие", "персональная программа", "2500 ₽")],
       cta_title="Приходите на пробное", cta_sub="Запишем на ближайшее удобное время"),
]

for s in SITES:
    cards = "".join(
        '<div class="card"><div class="ic"></div><h3>{}</h3><p>{}</p></div>'.format(t, d)
        for t, d in s["cards"])
    prices = "".join(
        '<div class="price"><span class="n">{}</span><span class="d">{}</span>'
        '<span class="v">{}</span></div>'.format(n, d, v) for n, d, v in s["prices"])
    nav = "".join('<a href="#">{}</a>'.format(x) for x in s["nav"])

    html = TPL.format(brand=s["brand"], tagline=s["tagline"], phone=s["phone"], nav=nav,
                      eyebrow=s["eyebrow"], h1=s["h1"], lead=s["lead"], cta=s["cta"],
                      f_title=s["f_title"], f_sub=s["f_sub"], cards=cards, prices=prices,
                      cta_title=s["cta_title"], cta_sub=s["cta_sub"], addr=s["addr"],
                      acc=s["acc"], font=s["font"], **s["theme"])

    out = os.path.join(ROOT, s["slug"])
    os.makedirs(out, exist_ok=True)
    with open(os.path.join(out, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("готово:", s["slug"])
