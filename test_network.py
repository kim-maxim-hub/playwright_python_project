import re

from time import sleep
from playwright.sync_api import Page, expect, Route


def test_auth_positive(page: Page):
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    expect(page.locator('.alert')).to_have_text('Вы успешно авторизованы.')

def test_auth_neggative(page: Page):
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User413')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    expect(page.locator('.alert')).to_have_text('Неверно указана электронная почта, логин или пароль.')

def test_request_route(page: Page):

    def change_request(route: Route):
        data = route.request.post_data
        if data:
            data = data.replace('User412', 'User413')
        route.continue_(post_data=data)

    page.route(re.compile('profile/authenticate'), change_request)
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    expect(page.locator('.alert')).to_have_text('Неверно указана электронная почта, логин или пароль.')
    
def test_response(page: Page):

    def change_response(route: Route):
        response = route.fetch()
        data = response.text()
        data = data.replace('User412', 'Person412')
        route.fulfill(response=response, body=data)
    
    page.route(re.compile('profile'), change_response)
    page.goto('https://gymlog.ru/profile/login/')
    page.locator('#email').fill('User412')
    page.locator('#password').fill('k9L-hL')
    page.get_by_role('button', name='Войти').click()
    page.get_by_role('link', name='Мой профиль').click()
    sleep(5)
