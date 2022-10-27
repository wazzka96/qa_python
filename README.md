# qa_python
### Добавленные тесты в tests.py:
1. test_add_new_book_add_two_books - проверка, что можно добавить 2 книги
2. test_add_new_book_set_rating_1 - проверка, что книга была добавлена с рейтингом 1
3. test_set_book_rating_more_then_10 - проверка, что рейтинг нельзя установить больше 10
4. test_set_book_rating_non_existent_book_negative_result - проверка, что книге, которой нет в books_rating не выставляется рейтинг и, следовательно, словарь пустой
5. test_get_books_with_specific_rating_positive_result - проверка, что выводятся книги с указанным рейтингом
6. test_get_book_rating_is_integer - проверка, что при вызове get_book_rating выводится значение integer
7. test_add_book_in_favorites_non_existent_book_negative_result - проверка, что при вызове add_book_in_favorites, если указать несуществующую книгу, то она не добавится в избранное
8. test_add_book_in_favorites_double_add - проверка, что при вызове add_book_in_favorites, если добавить уже добвленную в избранное книгу, то она не продублируется
9. test_delete_book_from_favorites_positive_result - проверка, что при вызове delete_book_from_favorites книга удаляется из избранного
10. test_get_list_of_favorites_books_is_list - проверка, что при вызове get_list_of_favorites_books выводится список