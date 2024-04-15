# Lambdas
# LISP: LISt Processing
# car(l: list) -> primer elemento
# cdr(l: list) -> resto de la lista

car = lambda l: l[0] if l else None
cdr = lambda l: l[1:] if l else []

# map, filter y reduce
# map(f, l) -> l  Aplica f a cada elemento de l
map = lambda f, l: [] if not l else \
    [f(car(l))] + map(f, cdr(l))

# filter(f, l) -> l  Devuelve los elementos de l que cumplen f
filter = lambda f, l: [] if not l else \
    [car(l)] + filter(f, cdr(l)) if f(car(l)) \
    else filter(f, cdr(l))

# reduce(f, l) -> x  Aplica f a los elementos de l
reduce = lambda f, l, res_default=0: res_default if not l else \
    car(l) if not cdr(l) else \
    f(car(l), reduce(f, cdr(l), res_default))

fibo = lambda n : [] if n < 0 \
    else [0] if n == 0 \
    else [0, 1] if n == 1 \
    else fibo(n-1) + [fibo(n-1)[-1] + fibo(n-1)[-2]]

fibo_memo = lambda n : [] if n < 0 \
    else [0] if n == 0 \
    else [0, 1] if n == 1 \
    else (fibo_ant := fibo(n-1)) + [fibo_ant[-1] + fibo_ant[-2]]

if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5]
    print(car(lista))
    print(cdr(lista))

    f = lambda x: x * 3
    print(map(f, lista))
    g = lambda x: x % 2 == 0
    print(filter(g, lista))
    h = lambda x, y: x + y
    print(reduce(h, lista))

    # En la vida real
    print(f"{[x * 3 for x in lista]}")
    print(f"{[x for x in lista if x % 2 == 0]}")

    import functools
    print(functools.reduce(h, lista))

    # map y filter están en la librería estándar, reduce hay que importarla de functools
    from datetime import datetime
    t1 = datetime.now()
    print(fibo(15))
    t2 = datetime.now()
    print(t2 - t1)

    t1 = datetime.now()
    print(fibo_memo(15))
    t2 = datetime.now()
    print(t2 - t1)

