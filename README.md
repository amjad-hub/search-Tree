# search-Tree

Бэкенд  предоставляет возможность работы с древовидной структурой, которую необходимо правильно уложить
в базу данных, для эффективной работы согласно требованиям.
Каждый элемент дерева должен иметь обязательное поле text, 
по которому осуществляется полнотекстовый поиск.
Основные требования:
● Авторизация через API, дальнейшее взаимодействие с API возможно только для 
авторизованных клиентов через токен (простая, но безопаснаяавторизация);
● Метод для вставки нового элемента;
● Метод для полнотекстового поиска, результат — список элементов с идентификаторами всех родителей;
● Метод для извлечения поддерева по id элемента, результат — список элементов с идентификаторами всех родителей;
● Конструировать запросы необходимо на SQLAlchemy избегая голого SQL;
● В качестве GUI для методов должен быть использован Swagger UI;
● Ответ на все методы должен быть в формате JSON.
