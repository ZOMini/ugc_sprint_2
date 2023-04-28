[![ugc+ workflows](https://github.com/ZOMini/ugc_sprint_2/actions/workflows/python.yml/badge.svg)](https://github.com/ZOMini/ugc_sprint_2/actions/workflows/python.yml)
# User Generated Content(UGC) + Elastic Logstash Kibana(ELK)

## Описание
  - UGC api сервис - позволяет пользователю(фронту) производить определенные действия с DB и ивент брокером(Kafka + Click House).
  - Взаимодействие Kafka и Click House основано на прямой интеграции, без ETL.
  - Все микросервисы, в том числе ранее написанные, логируют в ELK.

## Стек
  - Django, DRF, FastAPI, Elastic, Postgres, SQLlite, SQLAlchemy, Redis, Authlib(OAuth 2.0), JSON Web Tokens(JWT), Jaeger(Trace)
  - Kafka, Click House, Elastic Logstash Kibana(ELK) + filebeat

## Запуск
  - заполняем .env (см. .env.template)
  - docker-compose -f docker-compose-ugc.yml -f docker-compose-log.yml up --build
  - docker-compose -f docker-compose-log.yml -f docker-compose-all_prev_serv.yml up --build

## Сделано
  - залита клава кофем, потеряна кнопка "б".
  - исследование DB [comparison](https://github.com/ZOMini/ugc_sprint_2/blob/main/comparison/README.md)
  - ETL с прошлого спринта подкорректирован, ну он сам по себе работает (интеграция kafka-clickhouse).
  - API (fastapi+mongo) - дополняем API c прошлого спринта.
    - http://127.0.0.1:8000/ugc/api/openapi - docs, можно тестить через него.
  - upd 21.02:
  - Сделал логирование, пока все в одном компоузе, мб разобью потом. + доbавлю остальные сервисы, ну и все Beats-ми свяжу- если успею ...
    - http://127.0.0.1:5601/  - kibana
  - upd 23.02:
  - Сделал логирование всех сервисов, докеры нужно запускать парно(service+logger), понимаю что нужно бы разbить на более мелкие ноды...

## Полезности
  - http://127.0.0.1/ugc/api/openapi - docs
  - http://127.0.0.1/auth/docs/v1/
  - http://127.0.0.1/movies_fastapi/api/openapi
  - http://127.0.0.1/api/v1/movies
  - https://codeschat.com/article/145.html - fastapi + logging
  - docker-compose -f docker-compose-ugc.yml -f docker-compose-log.yml up --build 
  - docker-compose -f docker-compose-log.yml -f docker-compose-all_prev_serv.yml up --build 

## Для проверки:
    https://github.com/ZOMini/ugc_sprint_2 - репозиторий
    https://github.com/ZOMini/ugc_sprint_2/invitations - приглашение
    группа 6 - Пирогов Виталий/Игорь Синякин (@ee2 @sinyakinmail - в пачке)