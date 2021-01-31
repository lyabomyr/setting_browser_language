from time import sleep
link ='http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_goods_has_add_to_basket_button(browser):
    browser.get(link)
    sleep(30) #sleep для проверки правильности инициализации браузера
    find_button=browser.find_element_by_css_selector('.btn-add-to-basket')
    add_to_basket = find_button
    assert add_to_basket, 'кнопка добавления товара отсутвует'