-- Запрос 1: Топ-3 самых прибыльных типов продуктов за текущий год.
-- На какой вопрос отвечает: Какие категории услуг (абонементы, доп. услуги, персональные тренировки) приносят клубу наибольший доход?
SELECT 
    p.product_type,
    SUM(f.amount) AS total_revenue,
    SUM(f.quantity) AS total_sold
FROM fact_sales f
JOIN dim_products p ON f.product_key = p.product_key
JOIN dim_date d ON f.date_key = d.date_key
WHERE d.year = 2026
GROUP BY p.product_type
ORDER BY total_revenue DESC
LIMIT 3;


-- Запрос 2: Эффективность работы персонала по продажам.
-- На какой вопрос отвечает: Кто из сотрудников генерирует наибольшую выручку и насколько агрессивно они используют скидки для закрытия сделок?
SELECT 
    s.full_name AS employee_name,
    s.position,
    SUM(f.amount) AS revenue_generated,
    SUM(f.discount_amount) AS total_discounts_given
FROM fact_sales f
JOIN dim_staff s ON f.staff_key = s.staff_key
GROUP BY s.full_name, s.position
ORDER BY revenue_generated DESC;


-- Запрос 3: Объем выручки по демографическим сегментам клиентов.
-- На какой вопрос отвечает: Какая группа клиентов (по возрасту и полу) наиболее финансово ценна для фитнес-клуба?
SELECT 
    c.age_group,
    c.gender,
    SUM(f.amount) AS revenue,
    COUNT(DISTINCT f.client_key) AS unique_buyers
FROM fact_sales f
JOIN dim_clients c ON f.client_key = c.client_key
GROUP BY c.age_group, c.gender
ORDER BY revenue DESC;


-- Запрос 4: Помесячная динамика выручки и среднего чека.
-- На какой вопрос отвечает: Как распределяется выручка клуба по месяцам года, наблюдаются ли сезонные спады и как меняется средний чек покупки?
SELECT 
    d.year,
    d.month,
    SUM(f.amount) AS monthly_revenue,
    AVG(f.amount) AS average_cheque
FROM fact_sales f
JOIN dim_date d ON f.date_key = d.date_key
GROUP BY d.year, d.month
ORDER BY d.year DESC, d.month DESC;