#import hddm
#from hddm.simulators import *
#import hddm.simulators.boundary_functions as bf
from .simulators import boundary_functions as bf
import numpy as np

model_config = {
    "test": {
        "params": ["v", "a", "z", "t"],
        "params_trans": [0, 0, 1, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3], [3.0, 2.5, 0.9, 2.0]],
        "param_bounds_cnn": [
            [-2.5, 0.5, 0.25, 1e-3],
            [2.5, 2.2, 0.75, 1.95],
        ],  # [-2.5, 0.5, 0.25, 0.05], [2.5, 2.2, 0.75, 1.95]]
        "boundary": bf.constant,
        "n_params": 4,
        "default_params": [0.0, 1.0, 0.5, 1e-3],
        "hddm_include": ["z"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15},
    },
    "ddm": {
        "params": ["v", "a", "z", "t"],
        "params_trans": [0, 0, 1, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3], [3.0, 2.5, 0.9, 2.0]],
        "param_bounds_cnn": [
            [-2.5, 0.5, 0.25, 1e-3],
            [2.5, 2.2, 0.75, 1.95],
        ],  # [-2.5, 0.5, 0.25, 0.05], [2.5, 2.2, 0.75, 1.95]]
        "boundary": bf.constant,
        "n_params": 4,
        "default_params": [0.0, 1.0, 0.5, 1e-3],
        "hddm_include": ["z"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15},
    },
    "ddm_vanilla": {
        "params": ["v", "a", "z", "t"],
        "params_trans": [0, 0, 1, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0],
        "param_bounds": [[5.0, 0.1, 0.05, 0], [5.0, 5.0, 0.95, 3.0]],
        "boundary": bf.constant,
        "n_params": 4,
        "default_params": [0.0, 2.0, 0.5, 0],
        "hddm_include": ["z"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15},
    },
    "angle": {
        "params": ["v", "a", "z", "t", "theta"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.2, 1e-3, -0.1], [3.0, 2.0, 0.8, 2.0, 1.45]],
        "param_bounds_cnn": [
            [-2.5, 0.2, 0.1, 0.0, 0.0],
            [2.5, 2.0, 0.9, 2.0, (np.pi / 2 - 0.2)],
        ],  # [(-2.5, 2.5), (0.2, 2.0), (0.1, 0.9), (0.0, 2.0), (0, (np.pi / 2 - .2))]
        "boundary": bf.angle,
        "n_params": 5,
        "default_params": [0.0, 1.0, 0.5, 1e-3, 0.0],
        "hddm_include": ["z", "theta"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "theta": 0.1, "theta_std": 0.2},
    },
    "weibull": {
        "params": ["v", "a", "z", "t", "alpha", "beta"],
        "params_trans": [0, 0, 1, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 2.0, 2.0],
        "param_bounds": [
            [-2.5, 0.3, 0.2, 1e-3, 0.31, 0.31],
            [2.5, 2.5, 0.8, 2.0, 4.99, 6.99],
        ],
        "param_bounds_cnn": [
            [-2.5, 0.2, 0.1, 0.0, 0.5, 0.5],
            [2.5, 2.0, 0.9, 2.0, 5.0, 7.0],
        ],  # [(-2.5, 2.5), (0.2, 2.0), (0.1, 0.9), (0.0, 2.0), (0.5, 5.0), (0.5, 7.0)]
        "boundary": bf.weibull_cdf,
        "n_params": 6,
        "default_params": [0.0, 1.0, 0.5, 1e-3, 3.0, 3.0],
        "hddm_include": ["z", "alpha", "beta"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "alpha": 1.0, "alpha_std": 0.5,
                         "beta": 1.0, "beta_std": 0.5},
    },
    "levy": {
        "params": ["v", "a", "z", "alpha", "t"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1.0, 1e-3], [3.0, 2.0, 0.9, 2.0, 2]],
        "param_bounds_cnn": [
            [-2.5, 0.2, 0.1, 1.0, 0.0],
            [2.5, 2.0, 0.9, 2.0, 2.0],
        ],  # [(-2.5, 2.5), (0.2, 2), (0.1, 0.9), (1.0, 2.0), (0.0, 2.0)]
        "boundary": bf.constant,
        "n_params": 5,
        "default_params": [0.0, 1.0, 0.5, 1.5, 1e-3],
        "hddm_include": ["z", "alpha"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "alpha": 1.0, "alpha_std": 0.5},
    },
    "full_ddm": {
        "params": ["v", "a", "z", "t", "sz", "sv", "st"],
        "params_trans": [0, 0, 1, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 0.1, 0.5, 0.1],
        "param_bounds": [
            [-3.0, 0.3, 0.3, 0.25, 1e-3, 1e-3, 1e-3],
            [3.0, 2.5, 0.7, 2.25, 0.2, 2.0, 0.25],
        ],
        "param_bounds_cnn": [
            [-2.5, 0.2, 0.1, 0.25, 0.0, 0.0, 0.0],
            [2.5, 2.0, 0.9, 2.5, 0.4, 1.0, 0.5],
        ],  #  [(-2.5, 2.5), (0.2, 2.0), (0.1, 0.9), (0.25, 2.5), (0, 0.4), (0, 1), (0.0, 0.5)]
        "boundary": bf.constant,
        "n_params": 7,
        "default_params": [0.0, 1.0, 0.5, 0.25, 1e-3, 1e-3, 1e-3],
        "hddm_include": ["z", "st", "sv", "sz"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "sz": 1.1, # AF-TODO: Might be worth downregulating and adding _std widths
                         "st": 0.1,
                         "sv": 0.5,},
    },
    "full_ddm_vanilla": {
        "params": ["v", "a", "z", "t", "sz", "sv", "st"],
        "params_trans": [0, 0, 1, 0, 0, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 0.1, 0.5, 0.1],
        "param_bounds": [
            [-5.0, 0.1, 0.3, 0.25, 0, 0, 0],
            [5.0, 5.0, 0.7, 2.25, 0.25, 4.0, 0.25],
        ],
        "boundary": bf.constant,
        "n_params": 7,
        "default_params": [0.0, 1.0, 0.5, 0.25, 0, 0, 0],
        "hddm_include": ["z", "st", "sv", "sz"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "sz": 1.1, # AF-TODO: Might be worth downregulating and adding _std widths
                         "st": 0.1,
                         "sv": 0.5,},
    },
    "ornstein": {
        "params": ["v", "a", "z", "g", "t"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, None],
        "param_bounds": [[-2.0, 0.3, 0.2, -1.0, 1e-3], [2.0, 2.0, 0.8, 1.0, 2]],
        "param_bounds_cnn": [
            [-2.5, 0.2, 0.1, -1.0, 0.0],
            [2.5, 2.0, 0.9, 1.0, 2.0],
        ],  # [(-2.5, 2.5), (0.2, 2.0), (0.1, 0.9), (-1.0, 1.0), (0.0, 2.0)]
        "boundary": bf.constant,
        "n_params": 5,
        "default_params": [0.0, 1.0, 0.5, 0.0, 1e-3],
        "hddm_include": ["z", "g"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "g": 0.5, # AF-TODO: Might be worth adding std ?
                         "g_trans": 0.2},
    },
    "ddm_sdv": {
        "params": ["v", "a", "z", "t", "sv"],
        "params_trans": [0, 0, 1, 0, 0],
        "params_std_upper": [1.5, 1.0, None, 1.0, 1.0],
        "param_bounds": [[-3.0, 0.3, 0.1, 1e-3, 1e-3], [3.0, 2.5, 0.9, 2.0, 2.5]],
        "param_bounds_cnn": [
            [-3.0, 0.3, 0.1, 0.0, 0.0],
            [3.0, 2.5, 0.9, 2.0, 2.5],
        ],  # [(-3, 3), (0.3, 2.5), (0.1, 0.9), (0.0, 2.0), (0.0, 2.5)]
        "boundary": bf.constant,
        "n_params": 5,
        "default_params": [0.0, 1.0, 0.5, 1e-3, 1e-3],
        "hddm_include": ["z", "sv"],
        "n_choices": 2,
        "choices": [-1, 1],
        "slice_widths": {"v": 1.5, "v_std": 1,  
                         "a": 1, "a_std": 1, 
                         "z": 0.1, "z_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         "sv": 0.5, # AF-TODO: Might be worth adding std ?
                         },
    },
    "ddm_par2": {
        "params": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "params_trans": [0, 0, 0, 0, 1, 1, 1, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, None, None, 1.0],
        "param_bounds": [
            [-2.0, -2.0, -2.0, 0.3, 0.2, 0.2, 0.2, 0.0],
            [2.0, 2.0, 2.0, 2.0, 0.8, 0.8, 0.8, 2.0],
        ],
        "param_bounds_cnn": [
            [-2.5, -2.5, -2.5, 0.2, 0.1, 0.1, 0.1, 0.0],
            [2.5, 2.5, 2.5, 2.0, 0.9, 0.9, 0.9, 2.0],
        ],
        "boundary": bf.constant,
        "n_params": 8,
        "default_params": [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 1.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "n_choices": 4,
        "choices": [0, 1, 2, 3],
        "slice_widths": {"vh": 1.5, "vh_std": 0.5,
                         "vl1": 1.5, "vl1_std": 0.5,
                         "vl2": 1.5, "vl2_std": 0.5,  
                         "a": 1, "a_std": 1, 
                         "zh": 0.1, "zh_trans": 0.2,
                         "zl1": 0.1, "zl1_trans": 0.2,
                         "zl2": 0.1, "zl2_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         },
    },
    "ddm_seq2": {
        "params": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "params_trans": [0, 0, 0, 0, 1, 1, 1, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, None, None, 1.0],
        "param_bounds": [
            [-2.0, -2.0, -2.0, 0.3, 0.2, 0.2, 0.2, 0.0],
            [2.0, 2.0, 2.0, 2.0, 0.8, 0.8, 0.8, 2.0],
        ],
        "param_bounds_cnn": [
            [-2.5, -2.5, -2.5, 0.2, 0.1, 0.1, 0.1, 0.0],
            [2.5, 2.5, 2.5, 2.0, 0.9, 0.9, 0.9, 2.0],
        ],
        "boundary": bf.constant,
        "n_params": 8,
        "default_params": [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 1.0],
        "hddm_include": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "t"],
        "n_choices": 4,
        "choices": [0, 1, 2, 3],
        "slice_widths": {"vh": 1.5, "vh_std": 0.5,
                         "vl1": 1.5, "vl1_std": 0.5,
                         "vl2": 1.5, "vl2_std": 0.5,  
                         "a": 1, "a_std": 1, 
                         "zh": 0.1, "zh_trans": 0.2,
                         "zl1": 0.1, "zl1_trans": 0.2,
                         "zl2": 0.1, "zl2_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         },
    },
    "ddm_mic2": {
        "params": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t"],
        "params_trans": [0, 0, 0, 0, 1, 1, 1, 1, 0],
        "params_std_upper": [1.5, 1.5, 1.5, 1.0, None, None, None, None, 1.0],
        "param_bounds": [
            [-2.0, -2.0, -2.0, 0.3, 0.2, 0.2, 0.2, 0.0, 0.0],
            [2.0, 2.0, 2.0, 2.0, 0.8, 0.8, 0.8, 1.0, 2.0],
        ],
        "param_bounds_cnn": [
            [-2.5, -2.5, -2.5, 0.2, 0.1, 0.1, 0.1, 0.0, 0.0],
            [2.5, 2.5, 2.5, 2.0, 0.9, 0.9, 0.9, 1.0, 2.0],
        ],
        "boundary": bf.constant,
        "n_params": 9,
        "default_params": [0.0, 0.0, 0.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5],
        "hddm_include": ["vh", "vl1", "vl2", "a", "zh", "zl1", "zl2", "d", "t"],
        "n_choices": 4,
        "choices": [0, 1, 2, 3],
        "slice_widths": {"vh": 1.5, "vh_std": 0.5,
                         "vl1": 1.5, "vl1_std": 0.5,
                         "vl2": 1.5, "vl2_std": 0.5,  
                         "a": 1, "a_std": 1, 
                         "zh": 0.1, "zh_trans": 0.2,
                         "zl1": 0.1, "zl1_trans": 0.2,
                         "zl2": 0.1, "zl2_trans": 0.2,
                         "d": 0.1, "d_trans": 0.2, 
                         "t": 0.01, "t_std": 0.15,
                         },
    },
}

model_config["weibull_cdf"] = model_config["weibull"].copy()
model_config["full_ddm2"] = model_config["full_ddm"].copy()
