import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
    #Write your code here and return a python list after reshaping by using numpy's tolist() method
    r,c=new_shape
    if len(a)*len(a[0])!=r*c:
        return []
    return  np.array(a).reshape(new_shape).tolist()