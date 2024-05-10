import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class PCA:
    def __init__(self):
        pass
    def transform(self, database, features=None):
        # Calculating cov from database
        covar = database.cov()

        # Obtaining eigenvalues and vectors for PCA transform
        eigenvalues, eigenvectors = np.linalg.eig(covar)

        # Sorting in search for best values
        idx = eigenvalues.argsort()[::-1]
        eigenvalues = eigenvalues[idx]
        eigenvectors = eigenvectors[idx]

        # Checking explainibility of values
        explained_var = np.cumsum(eigenvalues) / np.sum(eigenvalues)

        # Getting number of values through explained_variance
        n_components = np.argmax(explained_var >= 0.50) + 1
        
        pca_vectors = eigenvectors[:,:n_components]
        pca_component = pd.DataFrame(pca_vectors, index=features, columns=['PCA1', 'PCA2'])

        # Plotting explainibility of data through PCA with heatmap
        plt.figure()
        sns.heatmap(pca_component)

        # Getting new database through dot product with pca_components
        covar_pca = pd.DataFrame(np.dot(database, pca_component))

        covar_pca.rename({'PC1': 'PCA1', 'PC2': 'PCA2'}, axis=1, inplace=True)

        return covar_pca