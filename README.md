# qa_python
В проекте я реализовала тесты:
1) test_add_new_book_add_same_book_twice - проверка повторной попытки добавления одной и той же книги
2) test_add_new_book_valid_name_length - проверка длины названия книги с использованием параметризации (валидное значение)
3) test_add_new_book_invalid_name_length - проверка длины названия книги с использованием параметризации (не валидное значение)
4) test_set_book_genre_for_existing_book - установка жанра книги, которая существует в коллекции
5) test_set_book_genre_for_non_existing_book - установка жанра книги, которой нет в коллекции
6) test_get_book_genre - получение жанра книги по её названию
7) test_get_book_genre_no_genre_set - получение жанра книги без установленного жанра
8) test_get_books_with_specific_genre_valid_genre - проверка получения списка книг, соответствующих определенному жанру
9) test_get_books_with_specific_genre_invalid_genre - проверка поведения, когда запрашивается жанр, которого нет в библиотеке
10) test_get_books_genre - получение полного словаря книг и жанров
11) test_get_books_for_children_positive - проверка выделения книг, подходящих для детей
12) test_get_books_for_children_negative - проверка выделения книг, не подходящих для детей
13) test_add_book_in_favorites - добавление книги в избранное
14) test_delete_book_from_favorites - удаление книги из избранного
15) test_get_list_of_favorites_books - отображение корректного списка избранных книг
