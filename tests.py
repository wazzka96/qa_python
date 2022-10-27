from main import BooksCollector


# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    # проверка, что книга была добавлена с рейтингом 1
    def test_add_new_book_set_rating_1(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Любовь и бутерброды')
        assert collector.get_book_rating('Любовь и бутерброды') == 1

    # проверка, что рейтинг нельзя установить больше 10
    def test_set_book_rating_more_then_10(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Любовь и бутерброды')

        # выставляем рейтинг больше 10
        collector.set_book_rating('Любовь и бутерброды', 11)
        assert collector.get_book_rating('Любовь и бутерброды') == 1

    # проверка, что книге, которой нет в books_rating не выставляется рейтинг и, следовательно, словарь пустой
    def test_set_book_rating_non_existent_book_negative_result(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # выставляем валидный рейтинг
        collector.set_book_rating('Любовь и бутерброды', 9)
        assert collector.books_rating == {}

    # проверка, что выводятся книги с указанным рейтингом
    def test_get_books_with_specific_rating_positive_result(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книги
        collector.add_new_book('Любовь и бутерброды')
        collector.add_new_book('Этичный взлом Пентагона для сомневающихся')

        # выставляем валидный рейтинг
        collector.set_book_rating('Любовь и бутерброды', 6)
        collector.set_book_rating('Этичный взлом Пентагона для сомневающихся', 10)
        assert 'Этичный взлом Пентагона для сомневающихся' in collector.get_books_with_specific_rating(10) and len(collector.get_books_with_specific_rating(10)) == 1

    # проверка, что при вызове get_book_rating выводится значение integer
    def test_get_book_rating_is_integer(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Любовь и бутерброды')

        assert type(collector.get_book_rating('Любовь и бутерброды')) == int

    # проверка, что при вызове add_book_in_favorites, если указать несуществующую книгу, то она не добавится в избранное
    def test_add_book_in_favorites_non_existent_book_negative_result(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Подделка произведений искусства. Советы и подсказки')

        # добавляем несуществующую книгу в избранное
        collector.add_book_in_favorites('Любовь и бутерброды')

        assert collector.favorites == []

    # проверка, что при вызове add_book_in_favorites, если добавить уже добвленную в избранное книгу, то она не продублируется
    def test_add_book_in_favorites_double_add(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Подделка произведений искусства. Советы и подсказки')

        # добавляем книгу в избранное
        collector.add_book_in_favorites('Подделка произведений искусства. Советы и подсказки')
        collector.add_book_in_favorites('Подделка произведений искусства. Советы и подсказки')

        assert 'Подделка произведений искусства. Советы и подсказки' in collector.favorites and len(collector.favorites) == 1

    # проверка, что при вызове delete_book_from_favorites книга удаляется из избранного
    def test_delete_book_from_favorites_positive_result(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем книгу
        collector.add_new_book('Как я бросила вашего папу')

        # добавляем книгу в избранное
        collector.add_book_in_favorites('Как я бросила вашего папу')

        # удаляем книгу из избранного
        collector.delete_book_from_favorites('Как я бросила вашего папу')

        assert 'Как я бросила вашего папу' not in collector.favorites

    # проверка, что при вызове get_list_of_favorites_books выводится список
    def test_get_list_of_favorites_books_is_list(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        assert type(collector.get_list_of_favorites_books()) == list