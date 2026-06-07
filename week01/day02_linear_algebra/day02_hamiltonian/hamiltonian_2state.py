import numpy as np

H_1 = np.array([[1,0.2],[2,2]])
H_2 = np.array([[1, 0.8],
              [0.8, 2]])
eigenvalues_1 ,eigenvectors_1 = np.linalg.eigh(H_1)
eigenvalues_2 ,eigenvectors_2 = np.linalg.eigh(H_2)

print("H_1 :",H_1)
print(" \nH_1 Eigenvalues:", eigenvalues_1)

print("\n H_1 Eigenvectors:", eigenvectors_1)

print("\nH_2 :",H_2)

print(" \n H_2 Eigenvalues:", eigenvalues_2)

print("\n H_2 Eigenvectors:", eigenvectors_2)

