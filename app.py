"""
Задание 1:
В папке files/ лежит файл с каталогом продукции (стекло лобовое, заднее, боковое и различные аксессуары: клей, молдинги)
Нужно считать информацию из этого каталога и записать в файл json. Нужные листы в каталоге
["Автостекло. Аксессуары. Клей", "Российский автопром"]
Автостекло. Аксессуары. Клей - это каталог "Иномарки"
Российский автопром - это каталог "Отечественные"
Нужные столбцы ["Вид стекла", "Еврокод", "Код AGC", "Старый Код AGC", "Наименование", "ОПТ"]
Обратить внимание - Если у позиции цена фиксированная, то в столбце ОПТ будет *, поэтому такие случаи нужно учесть и в
цену ставить Фиксированную цену.
Структура объекта в json-файле:
    {
        "art": Код AGC,
        "eurocode": Еврокод,
        "oldcode": Старый Код AGC,
        "name": Наименование,
        "catalog": Иномарки или отечественные (смотря из какой вкладки каталога позиция)
        "category": Вид стекла,
        "price": Цена ОПТ или Фиксированная
    }

Задание 2:
Опираясь на полученную информацию сформировать катлог для клиента. Для клиента нужны только товары из категорий
["ветровое", "заднее", "боковое"]
Цены для клиента рассчитываются по следующему принципу:
ветровое - (цена price из каталога + 1000) + 5%
заднее - (цена price из каталога + 800) + 7%
боковое - цена price из каталога + 10%
В итоге должны получить excel-файл с расшиернием .xlsx
-----------------------------------------------------------------------
| catalog | category | art | eurocode | oldcode | name | client_price |
-----------------------------------------------------------------------
"""