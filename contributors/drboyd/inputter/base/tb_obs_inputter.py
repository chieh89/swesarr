# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 16:33:25 2024

@author: drboyd1
"""

fn_input = 'tb_obs.txt'
sar_prior = [-17.5]

###############################################33
o_txt = [' Pit  #']
for each in sar_prior:
    o_txt.append('    ' + str(each))
    
# output text
with open(fn_input, 'w') as f:
    f.write("\n".join(o_txt))