## Пиши код в негативном ключе

После обучающих курсов начинающий программист
привыкает писать код в позитивном ключе
(опираясь на ту мысль, что все будет хорошо)

Позитивное мышление часто подводит.

Лучше размышлять с позиции того,
что может пойти не так

"Если вы не ищете проблемы в своем коде,
то они найдут вас"

Рутинная работа программиста - 
это работа с исключениями

## Как писать функцию?
- Внутри ф-ии по условиям бросать исключения
- При вызове ф-ии использовать блок try-except-finally

## Пиши свои классы исключений

- Пусть название класса будет длинным, но понятным
- Наследуйся от Exception (забудь про BaseException)
- Пиши подробное описание к классу
(опиши в каких случаях данное искллючение выбрасывается) 