
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
