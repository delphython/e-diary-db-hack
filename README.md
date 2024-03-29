# Взламываем электронный дневник

Консольная утилита для взлома базы данных электронного дневника, которая исправляет плохие оценки (2 и 3) по всем предметам на пятерки, удаляет жалобы и добавляет похвалы от учителя для определенного ученика по определенному предмету.

## 1. Развернуть сайт дневника школы

Для развертывания сайта дневника школы воспользуйтесь [этой инструкцией](https://github.com/devmanorg/e-diary/tree/master#readme)

## 2. Скачать файл базы данных сайта дневника школы

Скачайте [архив базы данных](https://dvmn.org/filer/canonical/1562234129/166/), разархивируйте его и поместите в каталог проекта сайта дневника школы. Если файл базы данных уже есть - замените его.

## 3. Установить скрипт

Скачайте скрипт `script.py` из текущего репозитория и скопируйте его в каталог проекта сайта дневника школы рядом с файлом `manage.py`.

## 4. Запуск скрипта

Для запуска скрипта необходимо в консоли перейти в каталог, где лежит файл скрипта и запустить команду:
```sh
python script.py schoolkid_full_name subject_title
```
где `schoolkid_full_name` - ФИО ученика в кавычках, `subject - наименование предмета.
Пример:
```sh
python script.py "Иванов Иван Иванович" Математика
```
Для проверки работы скрипта необходимо перейти на сайт электронного дневника, найти ученика и проверить, исправлены ли оценки, исчезли ли жалобы и появилась ли похвала от учителя.

Скрипта может выдавать сообщения, если введены некорректно ФИО ученика или наименование предмета.
1. Если введено несуществующее ФИО ученика, то будет выдано сообщение: `В базе данных нет ученика с именем Тестов Тест Тестович!`
2. Если введено ФИО ученика, повторяющееся в базе данных, то будет выдано сообщение: `В базе данных несколько учеников в ФИО которых содержится Иван!`
3. Если введен несуществующий предмет, то будет выдано сообщение: `В базе данных нет предмета с названием Математик!`

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).

## Контакты

Виталий Клюкин – [@delphython](https://t.me/delphython) – [delphython@gmail.com](mailto:delphython@gmail.com)

[https://github.com/delphython](https://github.com/delphython/)
