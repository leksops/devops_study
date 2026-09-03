import urllib.request

print("=== ЗАПУСК ЖИВОГО МОНИТОРИНГА СЕТИ ===")

# 1. Список реальных адресов для проверки
sites_to_check = [
    "https://google.com",
    "https://github.com",
    "https://this-site-definitely-does-not-exist-123.com"
]

html_content = """
<html>
<head>
    <meta charset="UTF-8">
    <title>DevOps Dashboard</title>
    <style>
        body { font-family: Arial; margin: 40px; background: #f4f4f9; }
        .server { padding: 15px; margin: 10px 0;
                  border-radius: 5px; color: white; font-weight: bold; }
        .up { background: #2ecc71; }
        .down { background: #e74c3c; }
    </style>
</head>
<body>
    <h1>📊 Живой статус сайтов (Мониторинг)</h1>
"""

# 2. Циклом обходим сайты и делаем реальные сетевые запросы
for url in sites_to_check:
    try:
        # Пробуем постучаться на сайт
        response = urllib.request.urlopen(url, timeout=3)
        # Если сайт ответил, получаем его HTTP-код (200 означает "Всё ок")
        status_code = response.getcode()

        if status_code == 200:
            msg = (
                f'<div class="server up">'
                f'🟢 {url} — Доступен (Код 200)</div>\n'
            )
            html_content += msg
            print(f"🟢 {url} — успешно проверен.")
    except Exception:
        # Если сайт не ответил, возникнет ошибка
        msg = (
            f'<div class="server down">'
            f'🔴 {url} — НЕДОСТУПЕН (Ошибка)</div>\n'
        )
        html_content += msg
        print(f"🔴 {url} — упал или недоступен.")

html_content += """
</body>
</html>
"""

# 3. Записываем результат в файл для Nginx
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ Живой отчет успешно сгенерирован в index.html!")
