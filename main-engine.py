import time

class Point:
    def __init__(self,x,y): self.x,self.y=x,y
    def __repr__(self): return f"P({self.x},{self.y})"

def Z(id_val, pt):
    print(f"Executing Z: ID={id_val} at {pt}")
    return pt

# --- BEGIN ---
