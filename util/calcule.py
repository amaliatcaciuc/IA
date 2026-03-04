"""
Modul pentru calcule matematice specifice IA.
Contine implementarea manuala a distantei Manhattan.
"""

def distanta_manhattan_manual(x: list, y: list) -> float:
    """
    Calculeaza suma diferentelor absolute dintre componentele a doi vectori.
    
    Args:
        x (list): Primul vector (X1, X2, ..., Xn).
        y (list): Al doilea vector (Y1, Y2, ..., Yn).
        
    Returns:
        float: Distanta Manhattan calculata manual.
    """
   
    return sum(abs(xi - yi) for xi, yi in zip(x, y))