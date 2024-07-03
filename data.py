from faker import Faker
from random import randint
import datetime

class Data:

    Faker.seed(randint(1, 999))
    faker = Faker()

    main_page_url = 'https://qa-scooter.praktikum-services.ru'
    login = faker.user_name()
    password = faker.password()
    firstName = faker.first_name()
    lastName = faker.last_name()
    address = faker.address()
    metroStation = randint(1, 257)
    phone = faker.phone_number()
    rentTime = randint(1,4)
    deliveryDate = datetime.date.today()+datetime.timedelta(days=1)
    comment = faker.text(max_nb_chars=50)
    color_data = (
        ['BLACK'], ['GREY'], ['BLACK', 'GREY'], []
    )
    api_create_courier = "/api/v1/courier"
    api_login_courier = "/api/v1/courier/login"
    api_order = "/api/v1/orders"

    text_login_400 = "Недостаточно данных для входа"
    text_login_404 = "Учетная запись не найдена"
    text_create_201 = '{"ok":true}'
    text_create_409 = "Этот логин уже используется"
    text_create_400 = "Недостаточно данных для создания учетной записи"