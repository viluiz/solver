# A Machine Learning Acceleration for Nonlinear PDE Solvers - applied to multiphase porous media flow

This repository is the official implementation of: 

[Machine learning acceleration for nonlinear solvers applied to multiphase porous media flow](https://www.sciencedirect.com/science/article/pii/S0045782521003200). 

and

Adaptive Learning Acceleration for Nonlinear PDE Solvers (Submitted)

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
 $ python -m ipykernel install --user --name=python3 (opitional)
```

Finally, start Jupyter:

```start
 $ jupyter notebook
```

### Dataset

To download the dataset follow the instructions in the directory **dataset**.

