def abbreviate(words):
    """
    Esta función convierte una frase en un acrónimo
    Toma una frase como Portable Network Graphics en PNG
    
    Param 
    words
    
    Return
    String (Acrónimo)
    """
    return "".join(words.upper()[i] if (i - 1 < 0 or (not words[i-1].isalpha() and words[i-1] != "'")) and words[i].isalpha() else "" for i in range(len(words) - 1, -1, -1))[::-1]