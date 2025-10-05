##  Project Overview
**Author: Alan Royce Gabriel BS22B001**
---

### **Objective**

This project explores **data veracity challenges** in the **Yeast gene expression dataset**, a classical multi-label biological dataset.
Using **t-SNE** and **Isomap**, the project visualizes and analyzes complex data issues such as:

* **Noisy/Ambiguous Labels**
* **Outliers**
* **Hard-to-Learn Samples**

These visual insights highlight the limitations that classifiers face when learning from real-world biological data.

---

### **Dataset**

**Yeast Dataset**

* **Features (X):** 103 gene expression attributes.
* **Labels (Y):** 14 binary functional categories.
* Source: [MULAN Repository – Yeast Dataset](http://mulan.sourceforge.net/datasets-mlc.html)

A converted `yeast.csv` file is used in this notebook, obtained by transforming the original `.arff` file using Python’s `scipy.io.arff` module.

---


###  **Workflow**

#### **1️ Preprocessing**

* Load the converted CSV file.
* Clean label columns (`b'0' → 0`, `b'1' → 1`).
* Split data into features (`X`) and labels (`Y`).
* Standardize features using `StandardScaler`.
* Reduce 14 labels to 3 visualization categories (two most frequent single-labels + top multi-label combination + “Other”).

#### **2️ Dimensionality Reduction**

**t-SNE**

* Tested perplexities `[5, 10, 20, 30, 40, 50]`.
* Evaluated embeddings using:

  * **Silhouette Score**
  * **Calinski–Harabasz Index**
  * **Davies–Bouldin Index**
* Selected **perplexity = 30** as the optimal trade-off between local and global structure.

**Isomap**

* Reduced data to 2D using Isomap with 10 neighbors.
* Compared manifold shape and global structure with t-SNE.

#### **3️ Veracity Inspection**

To identify problematic data points in the t-SNE space:

* **Outliers**: Detected using **Local Outlier Factor (LOF)**.
* **Noisy/Ambiguous Labels**: Identified using neighbor label disagreement.
* **Hard-to-Learn Samples**: Quantified via **local label entropy** (diversity of neighbor labels).

Each category is plotted distinctly for visual interpretation.

---

###  **Results Summary**

| Perplexity | Silhouette | Calinski–Harabasz | Davies–Bouldin |
| ---------- | ---------- | ----------------- | -------------- |
| 5          | -0.054     | 4.99              | 94.30          |
| 10         | -0.032     | 11.70             | 49.22          |
| 20         | -0.028     | 14.51             | 7.59           |
| **30**     | **-0.035** | **15.74**         | **7.57**       |
| 40         | -0.045     | 9.63              | 21.93          |
| 50         | -0.059     | 6.56              | 14.57          |

**Interpretation:**

* t-SNE with **perplexity = 30** gives the most interpretable structure.
* Overlapping clusters and negative Silhouette confirm biological complexity and label overlap.
* Isomap preserves **global structure**, while t-SNE emphasizes **local similarity**.

---


###  **How to Run**

1. Clone the repository or open the `.ipynb` notebook in Jupyter/Colab.
2. Ensure the following dependencies are installed:

   ```bash
   pip install numpy pandas matplotlib seaborn scikit-learn scipy
   ```
3. Place your converted CSV file at:

   ```
   data/yeast.csv
   ```
4. Run all cells sequentially to reproduce the analysis.

---
## Repository Contents

* `bs22b001_A5.ipynb` — Jupyter Notebook with full code, experiments, and evaluations.