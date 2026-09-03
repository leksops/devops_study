print("=== ЗАПУСК МОНИТОРИНГА СЕТИ ===")

# 1. Список серверов для проверки
servers = ["10.0.0.1", "10.0.0.2", "10.0.0.3", "10.0.0.4"]

# 2. Имитируем, что сервер 10.0.0.3 упал (для наглядности)
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
    <h1>📊 Статус infraestructura (Мой мониторинг)</h1>
"""

# 3. Циклом обходим сервера и динамически дописываем кусочки HTML-кода
for ip in servers:
    if ip == "10.0.0.3":
        msg = f'<div class="server down">🔴 Сервер {ip} — Упал</div>\n'
        html_content += msg
    else:
        msg = f'<div class="server up">🟢 Сервер {ip} — Стабилен</div>\n'
        html_content += msg

html_content += """
</body>
</html>
"""

# 4. Записываем весь получившийся текст в файл index.html для Nginx
with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ Отчет успешно сгенерирован в файл index.html!")
