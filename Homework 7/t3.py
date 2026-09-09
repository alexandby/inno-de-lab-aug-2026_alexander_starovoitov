# Конфигурационный словарь, полученный от сервиса инициализации
db_config = {
"connection": {
"host": "production-db.internal",
"port": 5432,
"user": "postgres"
}
}

#1
print(f'{ db_config.get('connection', {}).get('host', {}) }')
print(f'{ db_config.get('connection', {}).get('port', {}) }')

#2
print(f'SSL Mode: {db_config.get('ssl_settings', {}).get('ssl_mode', 'verify-full')}')

#3
db_config['connection']['admin'] = db_config['connection'].pop('user')

#4
db_config.get('connection').update(max_connections = 100)

print('Параметры соединения:')
for key, value in db_config['connection'].items():
    print(f'* {key}: {value}')