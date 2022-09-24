import numpy as np

a = [BAx, BAy, BAz]
b = [cAx, cAy, cAz]
a_mag = np.linalg.norm(a)
b_mag = np.linalg.norm(b)

theta = np.across(np.dot(a,b)/(a_mag * b_mag))
