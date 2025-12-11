
---

##  Overview

SmartRisk integrates **supervised learning** and **event-based simulation** to examine credit default behavior at both micro and macro scales.  
The framework evaluates:

- Predictive ability of a Random Forest model using financial behavior features.
- Emergent systemic behavior captured through a Cellular Automaton.
- Effects of class imbalance, weak signals, and stress propagation.
- Differences between prediction-driven and simulation-driven perspectives.

The project demonstrates how modern risk analysis benefits from combining ML prediction with dynamic simulation methods.

---

##  Components

### 1. Synthetic Data Generation
The `data_generation.py` script creates a realistic synthetic dataset:

- 20,000 customers  
- 12 months of financial activity  
- Features: balance variance, spending patterns, volatility, credit utilization  
- Logistic noise-based default probability assignment  

Output: `synthetic_dataset.csv`

---

### 2. Machine Learning Model
Implemented in `model_training.py` and `model_training.ipynb`.

- Algorithm: Random Forest (200 trees, depth 10)
- Standardized features
- Evaluation metrics:
  - ROC AUC = **0.500**
  - PR AUC = **0.032**
  - Accuracy = 0.93 (inflated by class imbalance)

Figures generated:

- `roc_curve.png`
- `pr_curve.png`

---

### 3. Cellular Automaton Simulation
Implemented in `ca_simulation.py`.

- 60×60 grid of customers  
- Local neighborhood influence  
- Global stress and stochastic noise  
- 60 time steps  
- Emergent systemic contagion behavior  

Output: `ca_summary.csv` + plot `ca_fraction.png`

---

### 4. Experiments Summary
The notebooks folder compiles:

- ML performance analysis  
- Feature importance  
- Failed attempts to improve the model  
- CA sensitivity tests  
- Comparisons between prediction and propagation behaviors  

---

## Final Report (PDF)



---

## Final Paper (PDF)

https://udistritaleduco-my.sharepoint.com/:b:/g/personal/jpgalindof_udistrital_edu_co/IQBc5kpV5GdoS4PC5pwCO5xjAUK3PwpEMdNHh888a86Sfq0?e=RtgDde

---

## Final Slides (Canva)

https://www.canva.com/design/DAG2wVwmC9U/0VyfARLmctVjVNXxrplugw/edit?utm_content=DAG2wVwmC9U&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

---

## Final Poster (Canva)

https://www.canva.com/design/DAG2vpVNLbM/eArllaQTZsxfXFN3olpLIA/edit?utm_content=DAG2vpVNLbM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

---

## Authors

Juan Pablo Galindo Flórez - 20231020230

Stevens Camilo Llanos Acero - 20231020221
