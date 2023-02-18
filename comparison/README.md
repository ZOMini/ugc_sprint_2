## Результаты

Операция                          | Clickhouse  | MongoDB     |
----------------------------------|-------------| ----------- |
INSERT SINGLE VIEWS 1k            | 5.49s       | 1.25s       |
INSERT SINGLE REVIEWS 1k          | 5.67s       | 1.07s       |
INSERT SINGLE BOOKMARKS 1k        | 5.46s       | 1.06s       |
INSERT BULK VIEWS 1m              | 8.25s       | 20.79s      |
INSERT BULK REVIWS 1m             | 9.88s       | 23.75s      |
INSERT BULK BOOKMARKS 1m          | 9.28s       | 22.26s      |
SELECT SINGLE VIEWS 1k            | 9.34s       | 5.10s       |
SELECT SINGLE REVIEWS 1k          | 6.94s       | 5.75s       |
SELECT SINGLE VIEWS 1k + index    | 5.58s       | 1.15s       |
SELECT SINGLE REVIEWS 1k + index  | 5.76s       | 1.18s       |

* Чтение с индексом по value в Clickhouse тестил руками.
Так как скорость чтения нам важнее, bерем mongo, да и пораbотать с ней хочется.
API bудем дораbатывать предыдущий, не хочется плодить и так уже море docker-ов,
хотя с точки зрения масштаbирования, гиbче bыло bы разделять,
тем bолее API - явно узкое место.
Еще подумал - можно же, УСЛОВНО, отдать 3-и API ноды под кафку, 1 или 2 под mongo.
Кроче дораbатываем прошлый API.