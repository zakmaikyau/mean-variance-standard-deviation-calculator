import numpy as np

def calculate(list):
  
  if len(list) < 9:
    
    raise ValueError("List must contain nine numbers.")
  
  else:

    calculations = dict.fromkeys(['mean', 'variance', 'standard deviation'])

    mat = np.array(list).reshape(3,3)
    calculations['mean'] = [mat.mean(0).tolist(), mat.mean(1).tolist(), mat.mean().tolist()]

    calculations['standard deviation'] = [mat.std(0).tolist(), mat.std(1).tolist(), mat.std().tolist()]
    
    calculations['variance'] = [mat.var(0).tolist(), mat.var(1).tolist(), mat.var().tolist()]

  return calculations
