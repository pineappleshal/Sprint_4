import pytest

from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['А', 'А' * 40])
    def test_add_new_book_valid_name_length_book_added(self, collector, name):
        collector.add_new_book(name)

        assert name in collector.get_books_genre()

    @pytest.mark.parametrize('name', ['', 'А' * 41])
    def test_add_new_book_invalid_name_length_book_not_added(self, collector, name):
        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_add_new_book_same_book_twice_added_once(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Оно')

        assert len(collector.get_books_genre()) == 1

    def test_add_new_book_new_book_has_no_genre(self, collector):
        collector.add_new_book('Оно')

        assert collector.get_book_genre('Оно') == ''

    @pytest.mark.parametrize('genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_available_genre_genre_set(self, collector, genre):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', genre)

        assert collector.get_book_genre('Оно') == genre

    def test_set_book_genre_unknown_genre_genre_not_set(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Роман')

        assert collector.get_book_genre('Оно') == ''

    def test_set_book_genre_book_not_in_collection_book_not_added(self, collector):
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_book_genre('Оно') is None

    def test_get_book_genre_unknown_book_returns_none(self, collector):
        assert collector.get_book_genre('Неизвестная книга') is None

    def test_get_books_with_specific_genre_returns_only_books_of_that_genre(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Дюна')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Оно']

    @pytest.mark.parametrize('genre', ['Роман', 'Комедии'])
    def test_get_books_with_specific_genre_no_matching_books_returns_empty_list(self, collector, genre):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre_returns_books_with_genres(self, collector):
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_genre() == {'Оно': 'Ужасы'}

    def test_get_books_for_children_age_rated_genres_not_included(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Маша и Медведь')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Шерлок Холмс', 'Детективы')
        collector.set_book_genre('Маша и Медведь', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Маша и Медведь']

    def test_get_books_for_children_book_without_genre_not_included(self, collector):
        collector.add_new_book('Оно')

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_book_in_collection_book_added(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_add_book_in_favorites_same_book_twice_added_once(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_add_book_in_favorites_book_not_in_collection_book_not_added(self, collector):
        collector.add_book_in_favorites('Оно')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_in_favorites_book_removed(self, collector):
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_not_in_favorites_favorites_unchanged(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Дюна')

        assert collector.get_list_of_favorites_books() == ['Оно']

    def test_get_list_of_favorites_books_returns_books_in_order_of_adding(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')
        collector.add_book_in_favorites('Оно')

        assert collector.get_list_of_favorites_books() == ['Дюна', 'Оно']
