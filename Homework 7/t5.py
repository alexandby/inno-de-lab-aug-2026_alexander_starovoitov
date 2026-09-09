# Поток данных телеметрии от серверов кластера
system_telemetry = [
("srv_01", 12.5, 64, "online"),
("srv_02", 85.0, 92, "online"),
("srv_03", 0.0, 0, "offline"),
("srv_04", 45.2, 78, "online"),
("srv_05", 95.1, 99, "online")
]
# Реализация конвейера агрегации метрик

#1
node_name = [node_name for node_name, _, _, _ in system_telemetry]
cpu_load = [cpu_load for _, cpu_load, _, _ in system_telemetry]
ram_usage = [ram_usage for _, _, ram_usage, _ in system_telemetry]
status = [status for _, _, _, status in system_telemetry]

#2
active_nodes = [
    (node_name, cpu_load, ram_usage, status) for node_name, cpu_load, ram_usage, status in system_telemetry
    if status == 'online'
]

#3
status_active = [node_name for node_name, _, _, status in system_telemetry if status == 'online']

#4
metrics = {
    'active_nodes_count': len(active_nodes),
    'average_cpu': sum(cpu_load)/len(active_nodes),
    'max_ram':max(ram_usage)
}

print(f'Активные узлы в сети: {status_active}')
print('Итоговый отчет телеметрии:')
print(f'metrics: { metrics }')
