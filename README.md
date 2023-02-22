# Для проверки:
    https://github.com/ZOMini/ugc_sprint_2 - репозиторий
    https://github.com/ZOMini/ugc_sprint_2/invitations - приглашение
    группа 6 - Пирогов Виталий/Игорь Синякин (@ee2 @sinyakinmail - в пачке)

# Сделано
  - залита клава кофем, потеряна кнопка "б".
  - исследование DB [comparison](https://github.com/ZOMini/ugc_sprint_2/blob/main/comparison/README.md)
  - ETL с прошлого спринта подкорректирован, ну он сам по сеbе раbотает (интеграция kafka-clickhouse).
  - API (fastapi+mongo) - дополняем API c прошлого спринта.
    - http://127.0.0.1:8000/api/openapi - docs, можно тестить через него.
  - Сделал логирование, пока все в одном компоузе, мb разоbью потом. + доbавлю остальные сервисы, ну и все Beats-ми свяжу- если успею ...
    - http://127.0.0.1:5601/  - kibana

# Полезности
  - http://127.0.0.1:8000/api/openapi - docs
  - https://codeschat.com/article/145.html - fastapi + logging
