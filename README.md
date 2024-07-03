# Sprint_7

Проект автоматизации тестирования API сервиса Яндекс.Самокат

1. Основа для написания автотестов — selenium 4.21.0
2. Команда для запуска тестов— pytest
3. Команда для получения allure отчета:
- pytest tests.py --alluredir=allure_results
- allure serve allure_results
4. В проекте реализованы проверки:
- Проверка создания курьера 
- Проверка авторизации курьера
- Проверка создания заказа
- Проверка получения списка заказов
