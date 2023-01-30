import pytest


@pytest.fixture
def smtp_connection():
    import smtplib

    return smtplib.SMTP("smtp.gmail.com", 587, timeout=5)


def test_ehlo(smtp_connection):
    response, msg = smtp_connection.ehlo()
    assert response == 250
    assert 0  # в демонстрационных целях

# В данном случае pytest использует следующий алгоритм для вызова тестовой функции:
# 1) pytest находит функцию test_ehlo по ее префиксу test_. 
#    Ей передается аргумент с именем smtp_connection, 
#    поэтому pytest ищет и находит функцию с именем smtp_connection, помеченную как фикстура.
# 2) Фикстура smtp_connection() вызывается для создания объекта-функции.
# 3) Затем вызывается функция test_ehlo(<объект smtp_connection>), 
#    выполняется и падает на последней строчке.

