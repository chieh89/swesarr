# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 18:11:52 2024

@author: drboyd1
"""

import glob, os, shutil, subprocess

def main_writer(fn_input='FILENAME.txt',   fn_RunParams='RunParams.txt',
                fn_obs='tb_obs.txt',       fn_hyper='hyperpar.txt',
                fn_accep='acceptance.txt', fn_tbout='post_tb.out',
                fn_thout='post_theta.out',
                run_params = {}, hyper_params = {}, obs_params = {}):

    # add junk line
    o_txt = [fn_RunParams, fn_obs, fn_hyper, fn_accep, fn_tbout, fn_thout]

    # output text
    with open(fn_input, 'w') as f:
        f.write("\n".join(o_txt))
        
    # run other things
    run_params_writer(fn_input=fn_RunParams, run_params=run_params)
    hyper_params_writer(fn_input=fn_hyper, hyper_params=hyper_params)
    obs_writer(fn_input=fn_obs, obs_params=obs_params)
    readme_writer()

def readme_writer(fn_input = 'README.md'):

    o_txt = [
        '# an apology',
        '',
        'this is the results dylan boyd attempting to run mike durand''s very cool metromemls function']
    
    # output text
    with open(fn_input, 'w') as f:
        f.write("\n".join(o_txt))
        
def run_params_writer(fn_input='RunParams.txt', run_params={}):
    # default inputs!
    # do not change the order for these values!
    Npits       = 1
    Niter       = 20000
    Nburn       = 2000
    NlyrMax     = 2
    Nfreq       = 1
    Nangle      = 1
    Np_passive  = 0
    Np_active   = 1
    Np_other    = 0
    NsnowVars   = 4
    NsoilVars   = 3
    ScatOpt     = 2 # 1 Emp. MEMLS, 2 MEMLS-IBA, 3 Roy-HUT  
    ModelOpt    = 1 # 1 MEMLS, 2 HUT, 3 DMRT-ML, 4 DMRT-QMS, 5 Bi-Continuous
    StdTb       = 2.0
    StdSigma    = 0.50
    StdOther    = None # [] should be list [] based on other Np_other
    Freq        = [9.75] # [Nfreq]
    Angle       = [45.0]  # [Nangle]
    Pol_Passive = None # [Np_passive] 1 Verti. 2 Horiz.
    Pol_Active  = [1] # [Np_active] # 1 VV, 2 HH, 3 VH, 4 HV
    Tsky        = 4.0172 # [Nfreq, 2]

    # Booleans (0 = False, 1 = True)
    UsePrior       = 1 # 0 False 1 True
    EstimateDz     = 1
    EstimateRho    = 1 
    EstimateD      = 1 
    EstimateTsnow  = 1
    EstimateSoil   = 1 
    EstimateP_M    = 0 
    EstimateP_Q    = 1
    EstimateP_SR   = 0
    InitialDz      = 0 # 0 (normal value, exp(mu+0.5cov)), -1 (smaller value, exp(mu-cov)), 1 (larger value, exp(mu+2cov))
    InitialRho     = 0
    InitialD       = 0
    InitialTsnow   = 0
    InitialSoil    = 0
    ConstrainRho   = 1
    ConstrainTsnow = 2 # 0 (No constraint), 1 (surface<bottom, warm snow at surface), 2 (surface>bottom, cold snow at surface)

    # min max (mm) values
    lay_thick_mm    = [0.0010, 10.0000]      # [m]
    snow_density_mm = [50.0000, 917.0000] # [kg/m3]
    grain_diam_mm   = [0.0010, 5.0000]      # [millimeter]
    snow_temp_mm    = [-30.0000, 0.0000]     # [degC]
    soil_moist_mm   = [0.0000, 1.0000]      # [-]
    soil_rmsh_mm    = [0.0000, 0.1000]       # [m]
    soil_temp_mm    = [-30.0000, 5.0000]     # [degC]
    P_M_mm          = [0.0000, 0.3000]             # 
    P_Q_mm          = [0.0800, 0.1200]             # 
    P_SR_mm         = [0.5000, 1.0000]            # ?

   # ordered list to iterate over
    run_params_val = [
        Npits, Niter, Nburn, NlyrMax, Nfreq, Nangle, Np_passive,
        Np_active, Np_other, NsnowVars, NsoilVars, ScatOpt, ModelOpt,
        StdTb, StdSigma, StdOther, Freq, Angle, Pol_Passive,
        Pol_Active,
        Tsky,
        UsePrior,
        EstimateDz,
        EstimateRho,
        EstimateD, 
        EstimateTsnow,
        EstimateSoil, 
        EstimateP_M,
        EstimateP_Q,
        EstimateP_SR,
        InitialDz,
        InitialRho,
        InitialD,
        InitialTsnow,
        InitialSoil,
        ConstrainRho,
        ConstrainTsnow,
        # min max (mm) values
        lay_thick_mm,
        snow_density_mm,
        grain_diam_mm,
        snow_temp_mm,
        soil_moist_mm,
        soil_rmsh_mm,
        soil_temp_mm,
        P_M_mm,
        P_Q_mm,
        P_SR_mm
        ]
    
    # dynamic updating of the ordered list using the attached indices.
    # this is a hackjob :(
    run_params_id = {
        'Npits' : 0, 
        'Niter' : 1, 
        'Nburn' : 2, 
        'NlyrMax' : 3, 
        'Nfreq' : 4, 
        'Nangle' : 5, 
        'Np_passive' : 6,
        'Np_active' : 7, 
        'Np_other' : 8, 
        'NsnowVars' : 9, 
        'NsoilVars' : 10, 
        'ScatOpt' : 11,
        'ModelOpt' : 12,
        'StdTb' : 13, 
        'StdSigma' : 14, 
        'StdOther' : 15, 
        'Freq' : 16, 
        'Angle' : 17, 
        'Pol_Passive' : 18,
        'Pol_Active' : 19,
        'Tsky' : 20,
        'UsePrior' : 21,
        'EstimateDz' : 22,
        'EstimateRho' : 23,
        'EstimateD' : 24, 
        'EstimateTsnow' : 25,
        'EstimateSoil' : 26, 
        'EstimateP_M' : 27,
        'EstimateP_Q' : 28,
        'EstimateP_SR' : 29,
        'InitialDz' : 30,
        'InitialRho' : 31,
        'InitialD' : 32,
        'InitialTsnow' : 33,
        'InitialSoil' : 34,
        'ConstrainRho' : 35,
        'ConstrainTsnow' : 36,
        # min max (mm) values
        'lay_thick_mm' : 37,
        'snow_density_mm' : 38,
        'grain_diam_mm' : 39,
        'snow_temp_mm' : 40,
        'soil_moist_mm' : 41,
        'soil_rmsh_mm' : 42,
        'soil_temp_mm' : 43,
        'P_M_mm' : 44,
        'P_Q_mm' : 45,            # 
        'P_SR_mm' : 46
        }

    run_params_hds = [
        'Number of pits to run (Npits)',
        'Number of iterations in the Markov Chain (Niter)',
        'Number of burn-in iterations in the Markov Chain (Nburn)',
        'Number of snow layers to predict (NlyrMax)',
        'Number of observation frequencies (Nfreq)',
        'Number of observation angles (Nangle)',
        'Number of polarizations of passive Tb (Np_passive)',
        'Number of polarizations of active backscattering coefficient (Np_active)',
        'Number of other observations (Np_other)',
        'Number of snow parameters per layer (NsnowVars)',
        'Number of soil parameters (NsoilVars)',
        'Scattering Coefficient Option (ScatOpt): 1 (Empirical MEMLS, Hallikainen-HUT), 2 (MEMLS-IBA, combined HUT), or 3 (Roy-HUT)',
        'Observation Model Option (ModelOpt): 1 (MEMLS), 2 (HUT), 3 (DMRT-ML), 4 (DMRT-QMS), 5 (Bi-Continuous)',
        'Error standard deviation of Tb observations (StdTb)',
        'Error standard deviation of backscattering coefficient observations (StdSigma)',
        'Error standard deviation of other observations (StdOther(Np_other))(Here StdOther(1)=Snow Depth in m)',
        'Observation frequencies (Freq(Nfreq))',
        'Observation angles in degree (Angle(Nangle))',
        'Polarizations for Passive Measurement(Pol_Passive(Np_passive)): 1 (vertical), 2 (horizontal)',
        'Polarizations for Active Measurement(Pol_Active(Np_active)): 1 (vv), 2 (hh), 3 (vh), 4 (hv)',
        'Tb boundary condition above snow surface at vertical and horizontal polarizations (K) (Tsky(Nfreq,2))',
        'Use prior information, 0 or 1. (UsePrior)',
        'Estimate dZ, -1, 0, 1  (EstimateDz)',
        'Estimate rho, -1, 0, 1  (EstimateRho)',
        'Estimate D, -1, 0, 1  (EstimateD)',
        'Estimate T, -1, 0, 1  (EstimateTsnow)',
        'Estimate S, -1, 0, 1  (EstimateSoil)',
        'Estimate P_M, -1,0,1 (EstimateP_M)',
        'Estimate P_Q, -1,0,1 (EstimateP_Q)',
        'Estimate P_SR, -1,0,1 (EstimateP_SR)',
        'Initial Value dZ, -1, 0, 1  (InitialDz): 0 (normal value, exp(mu+0.5cov)), -1 (smaller value, exp(mu-cov)), 1 (larger value, exp(mu+2cov))',
        'Initial Value rho, -1, 0, 1  (InitialRho)',
        'Initial Value D, -1, 0, 1  (InitialD)',
        'Initial Value T, -1, 0, 1  (InitialTsnow)',
        'Initial Value S, -1, 0, 1  (InitialSoil)',
        'Constrain rho (ConstrainRho): 0 (No constraint), 1 (surface<bottom, loose snow at surface), 2 (surface>bottom, dense snow at surface)',
        'Constrain 274-T (ConstrainTsnow): 0 (No constraint), 1 (surface<bottom, warm snow at surface), 2 (surface>bottom, cold snow at surface)',
        'Minimum & maximum limits for layer thickness [m]',
        'Minimum & maximum limits for density [kg/m3]',
        'Minimum & maximum limits for grain diameter [mm]',
        'Minimum & maximum limits for snow temperature [degC]',
        'Minimum & maximum limits for soil moisture [frac]',
        'Minimum & maximum limits for soil rms-height [m]',
        'Minimum & maximum limits for soil temperature [degC]',
        'Minimum & Maximum limits for model parameter, P_M',
        'Minimum & Maximum limits for model parameter, P_Q',
        'Minimum & Maximum limits for model parameter, P_SR'
        ]
    
    ### Insert values if desired!
    if run_params:
        for key in run_params.keys():
            i = run_params_id[key]
            run_params_val[i] = run_params[key]

    ################################################################
    # Styling functions for function input                         #
    ################################################################
    def style_float(val):
        # 4 decimal points, 9 = 8 characters + 1 for decimal
        v_txt = f'{val:9.4f}' 
        return v_txt

    def style_int(val):
        if val < 20:
            v_txt = f'{val : > 5}'
        else:
            v_txt = f'{val : > 12}'
        return v_txt

    def mystery_hd(hd):
        msg = 'unexpected data input for hd:\n{0}'.format(hd)
        raise Exception(msg)
    ################################################################
    o_txt = [] # output text file
    for hd, val in zip(run_params_hds, run_params_val):
        # always append header
        o_txt.append(hd)
        
        # determine type of input
        tp = type(val)
        
        # if none, skip line
        if val is None:
            continue
        elif tp == int:
            v_txt = style_int(val)
            o_txt.append(v_txt)
        elif tp == float:
            v_txt = style_float(val)
            o_txt.append(v_txt)
        elif tp == list:
            # loop over list!
            for each in val:
                ntp = type(each)
                if ntp == int: 
                    v_txt = style_int(each)
                elif ntp == float : 
                    v_txt = style_float(each)
                else:
                    mystery_hd(hd)
                o_txt.append(v_txt)
        else:
            mystery_hd(hd)
        
    # add junk line
    o_txt.append('')

    # output text
    with open(fn_input, 'w') as f:
        f.write("\n".join(o_txt))
        
def hyper_params_writer(fn_input = 'hyperpar.txt', hyper_params={}):
    # sections placed from 1-6 here
    None
    lay_thk_1    = [ 0.18972350, 0.00820469 ]
    grain_size_1 = [  0.18000000, 0.00810000 ]
    density_1    = [217.00000000, 3136.00000000]
    temp_274_1   = [ 10.85000000, 25.00000000 ]
    temp_279_1   = [ 15.85000000, 25.00000000 ]
    vwc_1        = [  0.08000000, 0.00160000]
    rmsh_1       = [  0.01000000, 0.00002500 ]
    P_M_1        = [   0.10000000, 0.00250000 ]
    P_Q_1        = [  0.10000000, 0.00010000 ]
    P_SR_1       = [  1.00000000, 0.06250000 ]
    None
    lay_thk_2    = [ 0.09486175,  1.00000000,  0.00410234,  0.04000000 ]
    grain_size_2 = [  0.18000000,  0.18000000,  0.00810000,  0.00810000 ]
    density_2    = [217.00000000, 217.00000000, 3136.00000000, 3136.00000000]
    temp_274_2   = [  10.85000000, 10.85000000, 25.00000000, 25.00000000 ]
    temp_279_2   = [ 15.85000000, 25.00000000 ]
    vwc_2        = [  0.08000000, 0.00160000]
    rmsh_2       = [  0.01000000, 0.00002500 ]
    P_M_2        = [   0.10000000, 0.00250000 ]
    P_Q_2        = [  0.10000000, 0.00010000]
    P_SR_2       = [  1.00000000, 0.06250000]
    None
    lay_thk_3    = [   0.06324117,  1.00000000,  1.00000000,  0.00273490,  0.04000000,  0.04000000 ]
    grain_size_3 = [    0.18000000,  0.18000000,  0.18000000,  0.00810000,  0.00810000,  0.00810000 ]
    density_3    = [217.00000000, 217.00000000, 217.00000000, 3136.00000000, 3136.00000000, 3136.00000000]
    temp_274_3   = [  10.85000000, 10.85000000, 10.85000000, 25.00000000, 25.00000000, 25.00000000]
    temp_279_3   = [ 15.85000000, 25.00000000 ]
    vwc_3        = [  0.08000000, 0.00160000]
    rmsh_3       = [  0.01000000, 0.00002500 ]
    P_M_3        = [   0.10000000, 0.00250000 ]
    P_Q_3        = [  0.10000000, 0.00010000]
    P_SR_3       = [  1.00000000, 0.06250000]
    None
    lay_thk_4    = [   0.04743088,  1.00000000,  1.00000000,  1.00000000,  0.00205117,  0.04000000,  0.04000000,  0.04000000]
    grain_size_4 = [  0.18000000,  0.18000000,  0.18000000,  0.18000000,  0.00810000,  0.00810000,  0.00810000,  0.00810000 ]
    density_4    = [217.00000000, 217.00000000, 217.00000000, 217.00000000, 3136.00000000, 3136.00000000, 3136.00000000, 3136.00000000]
    temp_274_4   = [  10.85000000, 10.85000000, 10.85000000, 10.85000000, 25.00000000, 25.00000000, 25.00000000, 25.00000000 ]
    temp_279_4   = [ 15.85000000, 25.00000000 ]
    vwc_4        = [  0.08000000, 0.00160000]
    rmsh_4       = [  0.01000000, 0.00002500 ]
    P_M_4        = [   0.10000000, 0.00250000 ]
    P_Q_4        = [  0.10000000, 0.00010000]
    P_SR_4       = [  1.00000000, 0.06250000]
    None
    lay_thk_5    = [ 0.03794470,  1.00000000,  1.00000000,  1.00000000,  1.00000000,  0.00164094,  0.04000000,  0.04000000,  0.04000000,  0.04000000 ]
    grain_size_5 = [  0.18000000,  0.18000000,  0.18000000,  0.18000000,  0.18000000,  0.00810000,  0.00810000,  0.00810000,  0.00810000,  0.00810000 ]
    density_5    = [217.00000000, 217.00000000, 217.00000000, 217.00000000, 217.00000000, 3136.00000000, 3136.00000000, 3136.00000000, 3136.00000000, 3136.00000000]
    temp_274_5   = [  10.85000000, 10.85000000, 10.85000000, 10.85000000, 10.85000000, 25.00000000, 25.00000000, 25.00000000, 25.00000000, 25.00000000 ]
    temp_279_5   = [ 15.85000000, 25.00000000 ]
    vwc_5        = [  0.08000000, 0.00160000]
    rmsh_5       = [  0.01000000, 0.00002500 ]
    P_M_5        = [   0.10000000, 0.00250000 ]
    P_Q_5        = [  0.10000000, 0.00010000]
    P_SR_5       = [  1.00000000, 0.06250000]
    None
    lay_thk_6    = [ 0.03162058,  1.00000000,  1.00000000,  1.00000000,  1.00000000,  1.00000000,  0.00136745,  0.04000000,  0.04000000,  0.04000000,  0.04000000,  0.04000000 ]
    grain_size_6 = [  0.18000000,  0.18000000,  0.18000000,  0.18000000,  0.18000000,  0.18000000,  0.00810000,  0.00810000,  0.00810000,  0.00810000,  0.00810000,  0.00810000 ]
    density_6    = [217.00000000, 217.00000000, 217.00000000, 217.00000000, 217.00000000, 217.00000000, 3136.00000000, 3136.00000000, 3136.00000000, 3136.00000000, 3136.00000000, 3136.00000000]
    temp_274_6   = [  10.85000000, 10.85000000, 10.85000000, 10.85000000, 10.85000000, 10.85000000, 25.00000000, 25.00000000, 25.00000000, 25.00000000, 25.00000000, 25.00000000 ]
    temp_279_6   = [ 15.85000000, 25.00000000 ]
    vwc_6        = [  0.08000000, 0.00160000]
    rmsh_6       = [  0.01000000, 0.00002500 ]
    P_M_6        = [   0.10000000, 0.00250000 ]
    P_Q_6        = [  0.10000000, 0.00010000]
    P_SR_6       = [  1.00000000, 0.06250000]

    hyper_parms_vals = [
        None,
        lay_thk_1,
        grain_size_1,
        density_1,
        temp_274_1,   
        temp_279_1,   
        vwc_1,        
        rmsh_1,       
        P_M_1,       
        P_Q_1,       
        P_SR_1,       
        None,
        lay_thk_2,    
        grain_size_2, 
        density_2,    
        temp_274_2,   
        temp_279_2,   
        vwc_2,
        rmsh_2,
        P_M_2,
        P_Q_2,
        P_SR_2,
        None,
        lay_thk_3,
        grain_size_3,
        density_3,
        temp_274_3,
        temp_279_3,
        vwc_3,
        rmsh_3,
        P_M_3,
        P_Q_3,
        P_SR_3,
        None,
        lay_thk_4,
        grain_size_4,
        density_4,
        temp_274_4,
        temp_279_4,
        vwc_4,
        rmsh_4,
        P_M_4,
        P_Q_4,
        P_SR_4,
        None,
        lay_thk_5,
        grain_size_5,
        density_5,
        temp_274_5,
        temp_279_5,
        vwc_5,
        rmsh_5,
        P_M_5,
        P_Q_5,
        P_SR_5,       
        None,
        lay_thk_6,    
        grain_size_6, 
        density_6,    
        temp_274_6,   
        temp_279_6,   
        vwc_6,        
        rmsh_6,       
        P_M_6,        
        P_Q_6,        
        P_SR_6]       

    hyper_parms_ids = {
        'None' : 0,
        'lay_thk_1' : 1,
        'grain_size_1' : 2,
        'density_1' : 3,
        'temp_274_1' : 4,   
        'temp_279_1' : 5,   
        'vwc_1' : 6,        
        'rmsh_1' : 7,       
        'P_M_1' : 8,       
        'P_Q_1' : 9,       
        'P_SR_1' : 10,       
        'None' : 11,
        'lay_thk_2' : 12,    
        'grain_size_2' : 13, 
        'density_2' : 14,    
        'temp_274_2' : 15,   
        'temp_279_2' : 16,   
        'vwc_2' : 17,
        'rmsh_2' : 18,
        'P_M_2' : 19,
        'P_Q_2' : 20,
        'P_SR_2' : 21,
        'None' : 22,
        'lay_thk_3' :23,
        'grain_size_3' : 24,
        'density_3' : 25,
        'temp_274_3' : 26,
        'temp_279_3' : 27,
        'vwc_3' : 28,
        'rmsh_3' : 29,
        'P_M_3' : 30,
        'P_Q_3' : 31,
        'P_SR_3' : 32,
        'None' : 33,
        'lay_thk_4' : 34,
        'grain_size_4' : 35,
        'density_4' : 36,
        'temp_274_4' : 37,
        'temp_279_4' : 38,
        'vwc_4' : 39,
        'rmsh_4' : 40,
        'P_M_4' : 41,
        'P_Q_4' : 42,
        'P_SR_4' : 43,
        'None' : 44,
        'lay_thk_5' : 45,
        'grain_size_5' : 46,
        'density_5' : 47,
        'temp_274_5' : 48,
        'temp_279_5' : 49,
        'vwc_5' : 50,
        'rmsh_5' : 51,
        'P_M_5' : 52,
        'P_Q_5' : 53,
        'P_SR_5' : 54,       
        'None' : 55,
        'lay_thk_6' : 56,    
        'grain_size_6' : 57, 
        'density_6' : 58,    
        'temp_274_6' : 59,   
        'temp_279_6' : 60,   
        'vwc_6' : 61,        
        'rmsh_6' : 62,       
        'P_M_6' : 63,        
        'P_Q_6' : 64,        
        'P_SR_6' : 65
        }

    hyper_parms_hds = [
        1,
        'Layer thickness (log-normal),m ',
        'Grain size (log-normal),mm ',
        'Density (log-normal),kg/m^3 ',
        '274.-Temperature (log-normal),K ',
        'Soil Temperature, 279-Tempereature (log-normal),K ',
        'Soil volumetric water content,FRAC ',
        'Soil surface rougness,m ',
        'Model Parameter with normal distribution, P_M ',
        'Model Parameter with uniform distribution, P_Q ',
        'Model Parameter with uniform distribution, P_SR ',
        2,
        'Layer thickness (log-normal),m ',
        'Grain size (log-normal),mm ',
        'Density (log-normal),kg/m^3 ',
        '274.-Temperature (log-normal),K ',
        'Soil Temperature, 279-Tempereature (log-normal),K ',
        'Soil volumetric water content,FRAC ',
        'Soil surface rougness,m ',
        'Model Parameter with normal distribution, P_M ',
        'Model Parameter with uniform distribution, P_Q ',
        'Model Parameter with uniform distribution, P_SR ',
        3,
        'Layer thickness (log-normal),m ',
        'Grain size (log-normal),mm ',
        'Density (log-normal),kg/m^3 ',
        '274.-Temperature (log-normal),K ',
        'Soil Temperature, 279-Tempereature (log-normal),K ',
        'Soil volumetric water content,FRAC ',
        'Soil surface rougness,m ',
        'Model Parameter with normal distribution, P_M ',
        'Model Parameter with uniform distribution, P_Q ',
        'Model Parameter with uniform distribution, P_SR ',
        4,
        'Layer thickness (log-normal),m ',
        'Grain size (log-normal),mm ',
        'Density (log-normal),kg/m^3 ',
        '274.-Temperature (log-normal),K ',
        'Soil Temperature, 279-Tempereature (log-normal),K ',
        'Soil volumetric water content,FRAC ',
        'Soil surface rougness,m ',
        'Model Parameter with normal distribution, P_M ',
        'Model Parameter with uniform distribution, P_Q ',
        'Model Parameter with uniform distribution, P_SR ',
        5,
        'Layer thickness (log-normal),m ',
        'Grain size (log-normal),mm ',
        'Density (log-normal),kg/m^3 ',
        '274.-Temperature (log-normal),K ',
        'Soil Temperature, 279-Tempereature (log-normal),K ',
        'Soil volumetric water content,FRAC ',
        'Soil surface rougness,m ',
        'Model Parameter with normal distribution, P_M ',
        'Model Parameter with uniform distribution, P_Q ',
        'Model Parameter with uniform distribution, P_SR ',
        6,
        'Layer thickness (log-normal),m ',
        'Grain size (log-normal),mm ',
        'Density (log-normal),kg/m^3 ',
        '274.-Temperature (log-normal),K ',
        'Soil Temperature, 279-Tempereature (log-normal),K ',
        'Soil volumetric water content,FRAC ',
        'Soil surface rougness,m ',
        'Model Parameter with normal distribution, P_M ',
        'Model Parameter with uniform distribution, P_Q ',
        'Model Parameter with uniform distribution, P_SR '
        ]
    
    ### Insert values if desired!
    if hyper_params:
        for key in hyper_params.keys():
            i = hyper_parms_ids[key]
            hyper_parms_vals[i] = hyper_params[key]

    o_txt = [] # output text file
    for hd, val in zip(hyper_parms_hds, hyper_parms_vals):
        if val is None and type(hd) == int:
            o_txt.append(f'{hd : > 2}')
        else:
            o_txt.append( hd )
            for each in val:
                o_txt.append( f'{each:12.8f}' )
                
    # add junk line
    o_txt.append('')

    # output text
    with open(fn_input, 'w') as f:
        f.write("\n".join(o_txt))

def obs_writer(fn_input='tb_obs.txt', obs_params={}):
    
    sar_obs = [-17.5]
    
    # this is so lazy. i'm so sorry
    if obs_params:
        for key in obs_params.keys():
            sar_obs = obs_params[key]
    
    ###############################################33
    o_txt = [' Pit  #']
    for each in sar_obs:
        o_txt.append('    ' + str(each))
        
    # output text
    with open(fn_input, 'w') as f:
        f.write("\n".join(o_txt))    

def main():
    # test function for MetroMEMLS interface
    obs_params = {'sar_obs' : [ -15 ]}
    main_writer(obs_params=obs_params)
    
def main_obs_looper(sar_obs, sim_dir='./', sim_name='sim', metro_memls_loc = './MetroMEMLS'):
    # create inputs for running MetroMEMLS by looping over a set of SAR obs
    # e.g., prepare 3 simulations in the folders
    # ./sim0, ./sim1, ./sim2

    
    # file name base
    fnb = sim_dir + sim_name
    sim_names = [fnb + str(a) for a in range(len(sar_obs))]
    
    # create directories
    for sim in sim_names:
        if not os.path.isdir(sim):
            os.makedirs(sim)
            
    # create directories and execute scripts!
    cmd = 'chmod +x MetroMEMLS'
    for sim, obs in zip(sim_names, sar_obs):
        shutil.copy(metro_memls_loc, sim)
        os.chdir(sim)
        obs_params = {'sar_obs' : [obs]}
        main_writer(obs_params=obs_params)
        result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
        os.chdir('..')

    
    
if __name__ == "__main__":
    main_obs_looper([-17.5, -15, -12.5])