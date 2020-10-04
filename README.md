# TaskManager
-------------

# Пользователь может зарегистрироваться в сервисе задав пару логин-пароль
Задавая пару логин-пароль, переходя по url localhost/auth/users/,
отправляется POST запрос с логином и паролем, тем самым пользователь
регистрируется в сервисе. Регистрация реализована с помощью библиотке djoser

# В системе может существовать много пользователей
В проекте используется встроенная модель django User, которая позволяет
создавать много пользователей

# Пользователь может авторизоваться в сервисе предоставив пару логин-пароль
# и получив в ответе токен
Задавая пару логин-пароль, переходя по url localhost/auth/login/,
отправляется POST запрос с логином и паролем, который возвращет необходимый
токен с помощью djangorestframework_simplejwt

# Пользователь видит только свои задачи
Отправляя GET-запрос с токеном, переходя по url localhost/tasks/,
пользователю возвращается список задач по его токену

# Пользователь может создать себе задачу
Отправляя POST-запрос с json, в котором находятся данные о задаче, а именно:
название, описание, статус, планируемая дата завершения, данные сохраняются
в БД

# Пользователь может менять статус задачи на любой из данного набора
# Пользователь может менять планируемое время завершения, название и описание
Отправляя POST-запрос с json, в котором находятся данные о задаче, а именно:
новое название, новое описание, новый статус, новая планируемая дата завершения,
данные обновляются в БД

# Пользователь может получить список своих задач, с возможностью фильтрации
# по статусу и планируемому времени завершения
В ответ на GET-запрос с токеном пользователя, по url localhost/tasks/,
пользователю возвращаются задачи отсортированные по статусу и
планируемому времени завершения
