
# ==========================================================
# PROJECT: Human PBMC Single-Cell RNA-seq Analysis
# MODULE 02: Quality Control
# STEP 1: Identify mitochondrial genes
# ==========================================================

import scanpy as sc

# Load the original PBMC count matrix.
adata = sc.datasets.pbmc3k()

# Identify mitochondrial genes using the MT- prefix.
# Store the result as a Boolean column in gene metadata.
adata.var["mt"] = adata.var_names.str.startswith("MT-")

# Count how many genes are marked as mitochondrial.
n_mt_genes = adata.var["mt"].sum()

print("Number of mitochondrial genes:", n_mt_genes)

# Display the identified mitochondrial gene names.
print("\nMitochondrial genes:")
print(adata.var_names[adata.var["mt"]].tolist())
