servers_list = ["10.0.0.1", "10.0.0.2"]
servers_list.append("10.0.0.3")

total = len(servers_list)
print(f"Всего обнаружено: {total} серверов. \n")

for server in servers_list:
    print(f"🔥 Сервер {server} взят под мониторинг")

