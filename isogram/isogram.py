def is_isogram(string):
    """
    Esta función determina si la la frase ingresada es un isograma
    
    Param
    Frase String
    
    Return 
    Cuenta de letras repetidas (Int)
    """
    string = string.lower().replace(' ', '').replace('-', '')

    return len(string) == len(set(string))