import os

from selene import browser, have


def test_fill_form():
    # Открываем страницу
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")


    # Вводим имя и фамилию
    browser.element('#firstName').type('Таисия')
    browser.element('#lastName').type('Повали')

    # Добавляем email
    browser.element('#userEmail').type('user@mail.ru')

    # Выбираем пол
    browser.element('[for="gender-radio-2"]').click()

    # Вводим номер телефона
    browser.element('#userNumber').type('9991234567')

    # Выбираем дату рождения
    browser.element('#dateOfBirthInput').click()

    # Выбираем год
    browser.element('.react-datepicker__year-select').click()
    browser.element('.react-datepicker__year-select') \
        .all('option') \
        .element_by(have.text('1990')) \
        .click()

    # Выбираем месяц
    browser.element('.react-datepicker__month-select').click()
    browser.element('.react-datepicker__month-select') \
        .all('option') \
        .element_by(have.text('March')) \
        .click()

    # Выбираем день
    browser.element('.react-datepicker__day--010').click()

    # Вводим subject
    browser.element('#subjectsInput').type('Commerce')
    browser.element('.subjects-auto-complete__menu').element('div').click()

    # Отмечаем хобби
    browser.element('[for="hobbies-checkbox-3"]').click()  # Music

    # Загружаем файл аватара
    browser.element('#uploadPicture').set_value(os.path.abspath('cat.jpg'))  # Путь к файлу

    # Проверяем адрес проживания
    browser.element('#currentAddress').type('Москва, ул. Ленина, д. 1')

    # Выбираем штат
    browser.element('#react-select-3-input').type('Haryana')
    browser.element('[id^="react-select-3-option-"]').click()

    # Выбираем город
    browser.element('#react-select-4-input').type('Karnal')
    browser.element('[id^="react-select-4-option-"]').click()

    # Отправляем форму
    browser.element('#submit').click()

    # Проверяем успешную отправку
    browser.element('.modal-content').should(have.text('Thanks for submitting the form'))

    # Проверяем заполненные поля в модальном окне
    browser.element('.table-responsive').should(have.text('Таисия Повали'))
    browser.element('.table-responsive').should(have.text('user@mail.ru'))
    browser.element('.table-responsive').should(have.text('Female'))
    browser.element('.table-responsive').should(have.text('9991234567'))
    browser.element('.table-responsive').should(have.text('10 March,1990'))
    browser.element('.table-responsive').should(have.text('Commerce'))
    browser.element('.table-responsive').should(have.text('Music'))
    browser.element('.table-responsive').should(have.text('cat.jpg'))
    browser.element('.table-responsive').should(have.text('Москва, ул. Ленина, д. 1'))
    browser.element('.table-responsive').should(have.text('Haryana Karnal'))

