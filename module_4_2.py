def test_function():
    def inner_function():
        print("Я в области видимости функции test_function")
    inner_function() # - не возвращает значение
#inner_function() - выдает ошибку, т.к. эта функция существует в функции test_function
test_function() # - работает