# A Machine Learning Acceleration for Nonlinear PDE Solvers

This repository is the official implementation of: 

***A Machine Learning Acceleration for Nonlinear PDE Solvers*** ICML submitted paper.

## Directories:

- **datasets**: Train and test datasets.
- **feature_selection**: Grid search for different sets of features.
- **model_selection**: Grid search for different machine learning models.
- **numerical_experiments**: All numerical experiments.
- **xgboost_coupling**: XGBoost coupling.

## Requirements

To install requirements:

```setup
 $ conda env create -f environment.yml 
 $ conda activate py3ml
 $ python -m ipykernel install --user --name=python3
```

Finally, start Jupyter:

```start
 $ jupyter notebook
```

### Dataset

To download the dataset follow the instructions in the directory **dataset**.

