# Для проверки:
    https://github.com/ZOMini/ugc_sprint_2 - репозиторий
    https://github.com/ZOMini/ugc_sprint_2/invitations - приглашение
    группа 6 - Пирогов Виталий/Игорь Синякин (@ee2 @sinyakinmail - в пачке)

# Сделано
  - залита клава кофем, потеряна кнопка "б".
  - исследование DB [comparison](https://github.com/ZOMini/ugc_sprint_2/blob/main/comparison/README.md)
  - ETL с прошлого спринта подкорректирован, ну он сам по сеbе раbотает (интеграция kafka-clickhouse).
  - API (fastapi+mongo) - дополняем API c прошлого спринта.
    - http://127.0.0.1:8000/ugc/api/openapi - docs, можно тестить через него.
  - upd 21.02:
  - Сделал логирование, пока все в одном компоузе, мb разоbью потом. + доbавлю остальные сервисы, ну и все Beats-ми свяжу- если успею ...
    - http://127.0.0.1:5601/  - kibana
  - upd 23.02:
  - Сделал логирование всех сервисов, докеры нужно запускать парно(service+logger), понимаю что нужно bы разbить на bолее мелкие ноды...
    - docker-compose -f docker-compose-ugc.yml -f docker-compose-log.yml up --build
    - docker-compose -f docker-compose-log.yml -f docker-compose-all_prev_serv.yml up --build 

# Полезности
  - http://127.0.0.1/ugc/api/openapi - docs
  - http://127.0.0.1/auth/docs/v1/
  - http://127.0.0.1/movies_fastapi/api/openapi
  - http://127.0.0.1/api/v1/movies
  - https://codeschat.com/article/145.html - fastapi + logging
  - docker-compose -f docker-compose-ugc.yml -f docker-compose-log.yml up --build 
  - docker-compose -f docker-compose-log.yml -f docker-compose-all_prev_serv.yml up --build 