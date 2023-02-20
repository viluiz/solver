import sys, os
import numpy as np
import joblib
import pandas as pd 
import xgboost as xgb

if __name__ == '__main__':

    # Check the number of inputs
    if len(sys.argv) == 2:
        
        # Process input    
        input_ = int(sys.argv[1])
        
        # Read the dataset for training
        df = pd.concat([pd.read_csv("AI_backtracking_parameters.csv").iloc[:,:-1],
                        pd.read_csv("non_linear_iterations.csv").iloc[:,:-1]]
                       ,axis=1)
        df = df[input_:]
        df.columns = df.columns.str.strip()
        df = df.dropna()
        df = df[df.outer_nonlinear_iteration != 1]
        df = df[df.outer_nonlinear_iteration != 2]
        X_train = df[['aspect_ratio',
                    'courant_number',
                    'shockfront_courant_number',
                    'shockfront_number_ratio',
                    #'min_total_mobility',
                    #'max_total_mobility',
                    'average_total_mobility',
                    #'min_Darcy_velocity',
                    #'max_Darcy_velocity',
                    'average_Darcy_velocity',
                    #'min_shockfront_mobratio',
                    #'max_shockfront_mobratio',
                    'average_shockfront_mobratio',
                    'average_longitudinal_capillary',
                    'average_transverse_capillary',
                    #'max_longitudinal_capillary',
                    #'max_transverse_capillary',
                    #'min_longitudinal_capillary',
                    #'min_transverse_capillary',
                    'average_buoyancy_number',
                    'average_longitudinal_buoyancy',
                    'average_transverse_buoyancy',
                    #'max_buoyancy_number',
                    #'max_longitudinal_buoyancy',
                    #'max_transverse_buoyancy',
                    #'min_buoyancy_number',
                    #'min_longitudinal_buoyancy',
                    #'min_transverse_buoyancy',
                    'average_overrelaxation',
                    #'max_overrelaxation',
                    #'min_overrelaxation',
                    #'average_invPeclet',
                    #'max_invPeclet',
                    #'min_invPeclet',
                    'res',
                    'resold',
                    'res_resold',
                     #'backtrack_par_factor',
                     #'outer_nonlinear_iteration',
                    'Inner_non_linear_iterations']].values 
        y_train = df["backtrack_par_factor"].values
        
        # Load models
        stdnorm = joblib.load("stdnorm_pipeline.pkl")
        XGRFmodel_loaded = joblib.load("XGBRFmodel_orig_lessfeatures.pkl") 
        
        # Retrain the model 
        # (optimized the learning rate -> range = [0.01, 1.0])
        # (optimized the max depth -> range = [3, 30])
        rf_xgb = XGRFmodel_loaded["RFreg"].get_booster() 
        XGRFmodel_loaded["RFreg"].set_params(n_estimators = 1, 
                                          learning_rate=0.01, 
                                          max_depth = 3,
                                          subsample=1.0, 
                                          colsample_bynode=1.0,
                                          random_state=42, 
                                          objective='reg:squarederror')
        XGRFmodel_loaded["RFreg"].fit(X_train, y_train, xgb_model=rf_xgb)
        joblib.dump(XGRFmodel_loaded, "XGBRFmodel_orig_lessfeatures.pkl")
        
    else:
        print(sys.argv)

