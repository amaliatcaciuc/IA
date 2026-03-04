import scipy.spatial.distance as dist
from util.calcule import distanta_manhattan_manual

def citeste_date(nume_fisier):
    """Citeste doi vectori dintr-un fisier text."""
    with open(nume_fisier, 'r') as f:
        linii = f.readlines()
       
        x = [float(i) for i in linii[0].split()]
        y = [float(i) for i in linii[1].split()]
    return x, y

if __name__ == "__main__":
    
    vec_x, vec_y = citeste_date("date_intrare.txt")
    
    
    rezultat_manual = distanta_manhattan_manual(vec_x, vec_y)
    

    rezultat_scipy = dist.cityblock(vec_x, vec_y)
    
    print(f"Vector X: {vec_x}")
    print(f"Vector Y: {vec_y}")
    print("-" * 30)
    print(f"Distanta Manhattan (Manual): {rezultat_manual}")
    print(f"Distanta Manhattan (SciPy):  {rezultat_scipy}")