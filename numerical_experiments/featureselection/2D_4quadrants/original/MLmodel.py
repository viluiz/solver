import sys, os
import numpy as np
import joblib

# Input Features: 
#
#0 aspect_ratio
#1 courant_number
#2 shockfront_courant_number
#3 shockfront_number_ratio
#4 min_total_mobility
#5 max_total_mobility
#6 average_total_mobility
#7 min_Darcy_velocity
#8 max_Darcy_velocity
#9 average_Darcy_velocity
#10 min_shockfront_mobratio
#11 max_shockfront_mobratio
#12 average_shockfront_mobratio
#13 average_longitudinal_capillary
#14 average_transverse_capillary
#15 max_longitudinal_capillary
#16 max_transverse_capillary
#17 min_longitudinal_capillary
#18 min_transverse_capillary
#19 average_buoyancy_number
#20 average_longitudinal_buoyancy
#21 average_transverse_buoyancy
#22 max_buoyancy_number
#23 max_longitudinal_buoyancy
#24 max_transverse_buoyancy
#25 min_buoyancy_number
#26 min_longitudinal_buoyancy
#27 min_transverse_buoyancy
#28 average_overrelaxation
#29 max_overrelaxation
#30 min_overrelaxation
#31 average_invPeclet
#32 max_invPeclet
#33 min_invPeclet
#34 res
#35 resold
#36 res_resold
#37 outer_nonlinear_iteration
#38 Inner_non_linear_iterations
if __name__ == '__main__':

    # Check the number of inputs
    if len(sys.argv) == 40:
         
        inputs = np.array( sys.argv[1:], dtype='float' )
        inputs[-1] = 1
        inputs = np.delete(inputs,[31, 32, 33, 37])
        
        RFmodel_loaded = joblib.load("RFmodel_orig_gs.pkl") 
        btpf = RFmodel_loaded.predict(inputs[None])
        print(btpf[0])
        
    else:
        print(sys.argv)

