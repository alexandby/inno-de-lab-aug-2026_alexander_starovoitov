# Список транзакций, полученных от платежного шлюза
raw_transactions = ["SUCCESS:100", "FAILED:50", "SUCCESS:-10", "SUCCESS:0", "SUCCESS:250", "ERROR:200"]
# Реализация фильтрации в одну строку с помощью List Comprehension

raw_transactions = [int(rt.split(':')[-1]) for rt in raw_transactions if
                    rt.startswith('SUCCESS') and int(rt.split(':')[-1]) > 0]

print(f'Очищенные транзакции: {raw_transactions}')
