# BooksCollector — юнит-тесты

Проект с тестами для класса `BooksCollector` (`main.py`). Тесты написаны на `pytest` и находятся в файле `tests.py`.

## Запуск

```
pip install pytest
pytest -v tests.py
```

## Реализованные тесты

### add_new_book
- `test_add_new_book_add_two_books` — можно добавить две книги.
- `test_add_new_book_valid_name_length_book_added` (параметризованный) — книга с названием из 1 и 40 символов добавляется.
- `test_add_new_book_invalid_name_length_book_not_added` (параметризованный) — книга с пустым названием и с названием из 41 символа не добавляется.
- `test_add_new_book_same_book_twice_added_once` — одну и ту же книгу нельзя добавить дважды.
- `test_add_new_book_new_book_has_no_genre` — у добавленной книги нет жанра.

### set_book_genre
- `test_set_book_genre_available_genre_genre_set` (параметризованный) — жанр из списка доступных устанавливается.
- `test_set_book_genre_unknown_genre_genre_not_set` — несуществующий жанр не устанавливается.
- `test_set_book_genre_book_not_in_collection_book_not_added` — для книги, которой нет в словаре, жанр не устанавливается.

### get_book_genre
- `test_get_book_genre_unknown_book_returns_none` — для неизвестной книги возвращается `None`.

### get_books_with_specific_genre
- `test_get_books_with_specific_genre_returns_only_books_of_that_genre` — возвращаются только книги нужного жанра.
- `test_get_books_with_specific_genre_no_matching_books_returns_empty_list` (параметризованный) — для жанра без книг и для неизвестного жанра возвращается пустой список.

### get_books_genre
- `test_get_books_genre_returns_books_with_genres` — возвращается словарь книг с жанрами.

### get_books_for_children
- `test_get_books_for_children_age_rated_genres_not_included` — книги с возрастным рейтингом не попадают в список для детей.
- `test_get_books_for_children_book_without_genre_not_included` — книга без жанра не попадает в список для детей.

### add_book_in_favorites
- `test_add_book_in_favorites_book_in_collection_book_added` — книга из словаря добавляется в избранное.
- `test_add_book_in_favorites_same_book_twice_added_once` — повторно добавить книгу в избранное нельзя.
- `test_add_book_in_favorites_book_not_in_collection_book_not_added` — книгу, которой нет в словаре, добавить в избранное нельзя.

### delete_book_from_favorites
- `test_delete_book_from_favorites_book_in_favorites_book_removed` — книга удаляется из избранного.
- `test_delete_book_from_favorites_book_not_in_favorites_favorites_unchanged` — удаление книги, которой нет в избранном, ничего не меняет.

### get_list_of_favorites_books
- `test_get_list_of_favorites_books_returns_books_in_order_of_adding` — возвращается список избранных книг в порядке добавления.
