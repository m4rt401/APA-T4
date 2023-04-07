class Aleat:
    '''
    Clase que implementa un generador de números del rango 0<=Xn<=m usando el método LGC.
    
    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    '''

    def __init__(self, m=2**31 - 1, a=1103515245, c=12345, x0=1212121):
        '''
        Creamos el método __init__ para obtener un conjunto de variables que sean configurables, y que
        tengan por defecto un valor.
        '''
        self.m = m
        self.a = a
        self.c = c
        self.x = x0

    def __next__(self):
        '''
        Con este método realizamos la generación y devuelve el número aleatorio siguiente.
        '''
        self.x = (self.a * self.x + self.c) % self.m
        return self.x

    def __call__(self, num):
        '''
        Reinicia la secuencia con el argumento indicado entre paréntesis.
        '''
        self.x = num

def aleat(m=2**31 - 1, a=1103515245, c=12345, x0=1212121):
    '''
    Esta función hace lo mismo que la clase anterior. Hacemos primero una asignación de 
    valores. Continuamos generando un bucle en el que realizamos hacemos que por cada iteración
    se actualize el valor de x y luego nos devuelve su valor usando el método yield.
    Cada vez que num tenga un valor nuevo nos hará el retorno y nos mostrara los numeros.

    >>> rand = Aleat(m=32, a=9, c=13, x0=11)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    16
    29
    18
    15

    >>> rand(29)
    >>> for _ in range(4):
    ...     print(next(rand))
    ...
    18
    15
    20
    1
    '''
    x = x0
    while True:
        x = (a * x + c) % m
        num = yield x
        if num is not None:
            x = num

if __name__ == "__main__":
    import doctest
    doctest.testmod()