
# ==========================================================
# Project: Human PBMC Single-Cell RNA-seq Analysis
# Module 01: Data Loading and Exploration
# ==========================================================

# Import Scanpy, a Python library for single-cell analysis.
import scanpy as sc


# Load the PBMC 3K dataset.
# Scanpy downloads it on first use and caches it locally.
# The dataset is returned as an AnnData object.
adata = sc.datasets.pbmc3k()


# Display general information about our dataset.
print("=== PBMC DATASET INFORMATION ===")

print(adata)

# Number of cells (observations)
print("Number of cells:", adata.n_obs)

# Number of genes/features (variables)
print("Number of genes:", adata.n_vars)

# Matrix dimensions: (cells, genes)
print("Matrix shape:", adata.shape)


# ==========================================================
# STEP 4: Inspect the gene-expression matrix
# ==========================================================

# Check the Python type of the expression matrix.
print("\nMatrix type:", type(adata.X))

# Examine the first 5 cells and first 5 genes.
# Convert this small selection into a readable array.
print("\nFirst 5 cells × first 5 genes:")
print(adata.X[:5, :5].toarray())


# ==========================================================
# STEP 5: Inspect CD3D expression across PBMCs
# ==========================================================

# Retrieve CD3D counts for the first 10 cells.
# Rows: first 10 cells
# Column: CD3D gene
cd3d_counts = adata[:10, "CD3D"].X.toarray()

print("\nCD3D counts in the first 10 cells:")
print(cd3d_counts.flatten())

