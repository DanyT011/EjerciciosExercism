def distance(strand_a, strand_b):
    """
    Calcular la distancia de martillo entre dos cadenas de ADN.
    Se comparan dos cadenas de ADN y se encuentran las diferencias 
    
    Param
    Cadena de ADN 1 (String) y Cadena de ADN 2 (String)
    
    Return
    Difernecia entre las dos cadenas (Int)
    """
    if len(strand_a) != len(strand_b):
        raise ValueError('not of equal length')
    errors = [a!=b for a,b in zip(strand_a, strand_b)]
    return sum(errors)