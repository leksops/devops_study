network_statuses = ["🟢 10.0.0.1", "🔴 10.0.0.2", "🟢 10.0.0.3", "🔴 10.0.0.4"]
broken_servers = []

for status in network_statuses :
    if "🔴" in status:
        broken_servers.append(status)

count = len(broken_servers)
print(f"внимание! обнаружено {count} упавших верверов: {broken_servers}")