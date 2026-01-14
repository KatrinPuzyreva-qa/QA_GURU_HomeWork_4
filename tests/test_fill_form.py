from selene import browser, have


def test_fill_form():
    # Открываем страницу
    browser.open('https://demoqa.com/automation-practice-form')

    # Вводим имя и фамилию
    browser.element('#firstName').type('Таисия')
    browser.element('#lastName').type('Повали')

    # Добавляем email
    browser.element('#userEmail').type('user@mail.ru')

    # Выбираем пол
    browser.element('[for="gender-radio-1"]').click()

    # Вводим номер телефона
    browser.element('#userNumber').type('89991234567')

    # Выбираем дату рождения
    browser.element('#dateOfBirthInput').send_keys('1990-01-01')

    # 6. Вводим subject
    browser.element('#subjectsInput').type('Commerce')
    browser.element('.subjects-auto-complete__menu').element('div').click()

    # Отмечаем хобби
    browser.element('[for="hobbies-checkbox-3"]').click()  # Music

    # Загружаем файл аватара
    browser.element('#uploadPicture').set_value('avatarka.jpg')  # Путь к файлу

    # Проверяем адрес проживания
    browser.element('#currentAddress').type('Москва, ул. Ленина, д. 1')

    # Отправляем форму
    browser.element('#submit').click()

    # Проверяем успешную отправку
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))
