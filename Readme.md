Реализуйте классы MinStat, MaxStat, AverageStat, которые будут находить минимум, максимум и среднее арифметическое последовательности целых чисел.
Экземпляры классов инициализируются без аргументов. Метод add_number должен добавлять в статистику число, которое будет учтено при вычислении финального результата методом result. Для экземпляров MinStat и MaxStat result должен возвращать целое число, для AverageStat — число типа float (это число будет сравниваться с правильным ответом до седьмой значащей цифры).

Если в последовательности отсутствуют числа и статистические величины вычислить невозможно, метод result должен возвращать None.

Реализуйте класс Table, который хранит целые числа в двумерной таблице. При инициализации Table(rows, cols) экземпляру передаются число строк и столбцов в таблице. Строки и столбцы нумеруются с нуля.
table.get_value(row, col) — прочитать значение из ячейки в строке row, столбце col. Если ячейка с индексами row и col не лежит внутри таблицы, нужно вернуть None.

table.set_value(row, col, value) — записать число в ячейку строки row, столбца col. Гарантируется, что в тестах будет в запись только в ячейки внутри таблицы.

table.n_rows() — вернуть число строк в таблице

table.n_cols() — вернуть число столбцов в таблице

table.delete_row(row) — удалить строку с номером row

table.delete_col(col) — удалить колонку с номером col

table.add_row(row) — добавить в таблицу новую строку с индексом row.
Номера строк >= row, должны увеличиться на единицу. Новая строка состоит из нулей.

table.add_col(col) — добавить в таблицу новую колонку с индексом col.
Номера колонок >= col, должны увеличиться на единицу. Новая колонка состоит из нулей.