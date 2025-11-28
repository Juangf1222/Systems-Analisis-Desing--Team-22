
# 1. Data-Driven Simulation

This simulation uses a synthetic dataset of 20,000 customers with financial and behavioral features inspired by the Kaggle competition, including:

base income

average spending

credit utilization

volatility

monthly balance (converted into mean, variance, trend)

monthly spending (mean, variance, trend)

Procedure:

Synthetic dataset generation.

Stratified train-test split.

Training a Random Forest classifier.

Evaluation using:

ROC AUC

PR AUC

Accuracy

Confusion matrix

Extraction of feature importances.

Export of predictions and plots.

Generated files:

synthetic_customers.csv

ml_predictions.csv

feature_importances.csv

roc_curve.png

pr_curve.png

# 2. Event-Based Simulation (Cellular Automaton)

This simulation models the propagation of credit default as a spatial and dynamic process, using a 60×60 cellular automaton.

Each cell represents a customer:

0 = not in default

1 = in default

Transition Rules:

The probability that a cell transitions to default depends on:

Global economic stress parameter E

Fraction of neighboring cells in default

Random perturbation per time step

Generated files:

ca_summary.csv

ca_fraction.png

ca_final_map.png

# Requirements

To run the notebook you need:

Python 3.x
numpy
pandas
scikit-learn
matplotlib


Recommended environments:

Kaggle Notebook

Jupyter Notebook / JupyterLab

VSCode with Jupyter extension

# How to Run the Notebook

Open simulation_notebook.ipynb.

Ensure dependencies are installed.

Run all cells in order.

All outputs will be automatically saved to the simulation_outputs/ folder.

# Report

The file Workshop_4_Report.pdf includes:

Simulation methodology

Results of both simulations

Comparative analysis

Sensitivity and chaos discussion

Conclusions

# PDF Link

https://drive.google.com/file/d/1Hrt0SPgr5qPkRLlj36dpUjXa5KdzcyZ6/view?usp=sharing

# Authors

Juan Pablo Galindo Flórez - 20231020230

Stevens Camilo Llanos Acero - 20231020221
