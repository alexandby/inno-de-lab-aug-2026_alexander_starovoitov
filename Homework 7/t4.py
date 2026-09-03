# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

#1
requested_roles = set(requested_roles)

#2
inter_roles = set.intersection(requested_roles, required_admin_roles)

#3
diff_roles = set.difference(required_admin_roles, requested_roles)

#4
print(
f'''
Уникальные запрошенные роли: { requested_roles }
Общие административные роли: { inter_roles }
Недостающие административные роли: { diff_roles }
Наличие роли security_officer в запросе: { 'security_officer' in requested_roles }
'''
)