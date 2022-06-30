## A Machine Learning Acceleration for Nonlinear PDE Solvers

### Directories:

- **featureselection**: Numerical experiments for the feature selection.
- **modelselection**: Numerical experiments for the model selection.

### Numerical experiments

Inside **featureselection** and **modelselection** there are four folders:

- **2D_2layered**: simulations of the two-dimensional layered reservoir used for training.
- **2D_4quadrants**: simulations of the two-dimensional heterogeneous reservoir with permeability varying in four quadrants.
- **3D_channels**: simulations of the realistic three-dimensional channelized reservoir.
- **3D_faulted**:  simulations of the realistic three-dimensional faulted reservoir.

From inside this folders execute *non_linear_iterations_ximproved.ipynb*: 

Inside the notebook
```
Cell->Run All 
```

or using the command line:
```
$ jupyter nbconvert --to notebook --execute <notebookname>.ipynb
```


