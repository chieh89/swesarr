# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:00:44 2024

@author: drboyd1
"""

# filename
fn_input = 'RunParams.txt'

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
    P_Q_mm,            # 
    P_SR_mm
    
    ]

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


