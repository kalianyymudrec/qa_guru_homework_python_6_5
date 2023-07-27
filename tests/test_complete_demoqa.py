from selene import browser, have
import os

def test_complete_demoqa():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Danila')
    browser.element('#lastName').type('Panov')
    browser.element('#userEmail').type('danila@mail.ru')
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1357924680')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().type('August').click()
    browser.element('[class="react-datepicker__year-select"]').click().type('2002').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--008"]').click()
    browser.element('#subjectsInput').type('ofc')
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath('pictures/image.png'))
    browser.element('#currentAddress').type('komsomolskiy 4')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Noida').press_enter()
    browser.element('#submit').click()


    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.modal-body').should(have.text('Danila Panov'))
    browser.element('.modal-body').should(have.text('danila@mail.com'))
    browser.element('.modal-body').should(have.text('Male'))
    browser.element('.modal-body').should(have.text('1357924680'))
    browser.element('.modal-body').should(have.text('18 August,2002'))
    browser.element('.modal-body').should(have.text('ofc'))
    browser.element('.modal-body').should(have.text('Sports'))
    browser.element('.modal-body').should(have.text('image.png'))
    browser.element('.modal-body').should(have.text('komsomolskiy 4'))
    browser.element('.modal-body').should(have.text('NCR Noida'))
