## Recursion

Предназначение рекурсии - разбивать/уменьшать
поступившие данные до тех пор, пока не будет
выполнено условие выхода.

Рекурсивная функция всегда представлена комбинацией
основного случая (base case) у рекурсивного вызова

В питоне рекурсия ограничена глубиной стека
(по умолчанию - 1000) и не оптимизирована.
Это значит, что то, как именно написана рекурсивная
функция влияет только на ее визуальное восприятие, но 
никак не улучшает эффективность ее исполнения
(в некоторых других языках рекурсия оптимизирована,
а значит можно написать код таким образом, чтобы
ускороить исполнение рекурсии)
В питоне рекурсию можно писать не задумываясь. 
Скорость ее исполнения всегда будет одинакова.

### Частые ошибки

- Нет условия выхода (base case)
- Нет return
- Нет уменьшения данных


## Дополнительно

Рекурсия и циклы взаимозаменяемы!

Любую задачу, которую вы решаете рекурсией можно
решить и циклами, и наоборот!

Есть некие ЯП в которых циклов нет вообще!
Там используется оптимизированная рекурсия с
глубоким стеком!

### Когда конкретно применять рекурсию?

Сложно дать рекомендацию. Это приходит с опытом.
Обычно, рекурсия хороша там, где данные не однородны,
и имеют некую вложенность. Пример: JSON

Когда вы используете сложное костыльное решение на
циклах, то стоит задуматься о том, чтобы использовать
рекурсию...и наоборот...если вы делаете рекурсивное 
решение и оно очень сложное, то подумайте о том,
чтобы использовать циклы...

### Где в стандартной библиотеке используется рекурсия?

repr, str, встроенная библиотека json!

То есть если вы работаете со входящими json, и вам
придет по сети какой-то json с большой вложенностью
(более 1000), то у вас упадет RecursionError,
более того, вы даже не увидите ничего в логах, т.к.
логи используют repr!

