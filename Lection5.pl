write("hello world").

% Правило для вычисления суммы элементов списка
сумма([], 0).
сумма([X | Tail], Sum) :- 
    сумма(Tail, TailSum),
    Sum is X + TailSum.

% Правило для вычисления произведения элементов списка
произведение([], 1).
произведение([X | Tail], Product) :-
    произведение(Tail, TailProduct),
    Product is X * TailProduct.
?- сумма([1, 2, 3, 4], Sum).
Sum = 10.

?- произведение([1, 2, 3, 4], Product).
Product = 24.