## Результаты

Операция                   | Clickhouse  | MongoDB     |
---------------------------|-------------| ----------- |
INSERT SINGLE VIEWS 1k     | 5.49s       | 1.25s       |
INSERT SINGLE REVIEWS 1k   | 5.67s       | 1.07s       |
INSERT SINGLE BOOKMARKS 1k | 5.46s       | 1.06s       |
INSERT BULK VIEWS 1m       | 8.25s       | 20.79s      |
INSERT BULK REVIWS 1m      | 9.88s       | 23.75s      |
INSERT BULK BOOKMARKS 1m   | 9.28s       | 22.26s      |
SELECT SINGLE VIEWS 1k     | 9.34s       | 5.10s       |

Так как скорость чтения нам важнее, bерем mongo, да и пораbотать с ней хочется.