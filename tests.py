import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

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
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    def test_add_new_book_add_same_book_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        # тест для проверки того, что книга добавилась только один раз
        assert len(collector.get_books_genre()) == 1

    # тесты для проверки длины названия книги
    @pytest.mark.parametrize("book_name", [
        'Валидное название книги','x' * 40])
    def test_add_new_book_valid_name_length(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()
    @pytest.mark.parametrize("book_name", ['','x' * 45])
    def test_add_new_book_invalid_name_length(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    # тест корректности установки жанра книги, которая есть в словаре
    def test_set_book_genre_for_existing_book(self, collector):
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Ужасы')
        assert collector.get_book_genre('Book1') == 'Ужасы'
    # тест установки жанра книги, которой нет в словаре
    def test_set_book_genre_for_non_existing_book(self, collector):
        collector.set_book_genre('NonExistingBook', 'Ужасы')
        assert collector.get_book_genre('NonExistingBook') is None

    # тест для получения жанра книги по её названию
    def test_get_book_genre(self,collector):
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1','Ужасы')
        assert collector.get_book_genre('Book1') == 'Ужасы'

    # тест получения жанра книги без установленного жанра
    def test_get_book_genre_no_genre_set(self, collector):
        collector.add_new_book('Book1')
        assert collector.get_book_genre('Book1') == ''

    # тест передачи не верного жанра, которого нет в коллекции
    def test_get_books_with_specific_genre_invalid_genre(self, collector):
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Фантастика')
        books = collector.get_books_with_specific_genre('Роман')
        assert books == []

    # тест для получения полного словаря книг и жанров
    def test_get_books_genre(self, collector):
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Фантастика')
        collector.add_new_book('Book2')
        collector.set_book_genre('Book2', 'Ужасы')
        expected = {'Book1': 'Фантастика', 'Book2': 'Ужасы'}
        assert collector.get_books_genre() == expected

    # тест получения списка книг предназначенных для детей
    def test_get_books_for_children_positive(self, collector):
        collector.add_new_book('Book1')
        collector.set_book_genre('Book1', 'Фантастика')
        collector.add_new_book('Book3')
        collector.set_book_genre('Book3', 'Мультфильмы')
        books_for_children = collector.get_books_for_children()
        assert 'Book1' in books_for_children
        assert 'Book3' in books_for_children

    # тест того, что неподходящие для детей книги не попадают в итоговый список
    def test_get_books_for_children_negative(self, collector):
        collector.add_new_book('Book2')
        collector.set_book_genre('Book2', 'Ужасы')
        books_for_children = collector.get_books_for_children()
        assert 'Book2' not in books_for_children

    # тест добавления книги в избранное
    def test_add_book_in_favorites(self, collector):
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        assert 'Book1' in collector.get_list_of_favorites_books()

    # тест удаления книги из избранного
    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book('Book1')
        collector.add_book_in_favorites('Book1')
        collector.delete_book_from_favorites('Book1')
        assert 'Book1' not in collector.get_list_of_favorites_books()

    # тест отображения корректного списка избранных книг
    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book('Book1')
        collector.add_new_book('Book2')
        collector.add_book_in_favorites('Book1')
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ['Book1']
