# -*- coding: utf-8 -*-
"""
Created on Mon Mar 25 23:00:21 2019

@author: Dragana
"""

"""
The plots which are not commented out were used.
"""

import os
import numpy as np
import urllib.request
import seaborn as sns
from scipy.stats import norm
import matplotlib.pyplot as plt

"""
------- Distribution plots per single subject, per interval

os.chdir("C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/ScaledTime14/")
x=[]
cur_int='5.8'
cur_subj='14'
for i in range(1,4): # 1, 2, 3, 4, 5, 6
#for j in ['1.45','2.9','5.8']:
    name = 'ScaledTime_Play_subj_'+cur_subj+'_bl_' + str(i) + '_int_' + cur_int + '.txt'
    int_length=np.genfromtxt(name, dtype='str')
    for j in range(1,16):
        int_single = int_length[j,15]
        int_single = float(int_single)
        
        x.append(int_single)

plt.title("2.9 second interval productions for subject 02")
plt.ylabel("Density", fontsize=12) 
plt.xlabel("Produced intervals", fontsize=12) 
#plt.plot([2.9,2.9],[0,0.831], label='2.9 seconds', color='darkblue')
sns.distplot(x, rug=True, hist=False, label='Density', color='teal')
"""


"""
------- Distribution plots per single subject of all intervals

os.chdir("D:/ScaledTime/Matlab data/ScaledTime14")
#os.chdir("C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/ScaledTime1_Sebastien/")
x1=[]
x2=[]
x3=[]
cur_subj='14'
for i in range(1,5): # 1, 2, 3, 4
    for j in ['1.45','2.9','5.8']:
        name = 'ScaledTime_Play_subj_'+cur_subj+'_bl_' + str(i) + '_int_' + j + '.txt'
        int_length=np.genfromtxt(name, dtype='str')
        for k in range(1,16):
            int_single = int_length[k,17]
            int_single = float(int_single)
            if int_single < 30:
                if j == '1.45':
                    x1.append(int_single)
                if j == '2.9':
                    x2.append(int_single)
                if j == '5.8':
                    x3.append(int_single)

# A function to truncate the number of decimal places
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

x1_mean = sum(x1)/len(x1)
x1_sd = truncate(np.std(x1),3)
x2_mean = sum(x2)/len(x2)
x2_sd = truncate(np.std(x2),3)
x3_mean = sum(x3)/len(x3)
x3_sd = truncate(np.std(x3),3)

with sns.color_palette("Blues_r"):
    plt.title("All interval productions of pax at140305 of all blocks")
    plt.ylabel("Density", fontsize=12) 
    plt.xlabel("Produced intervals", fontsize=12)         
    sns.distplot(x1, rug=True, hist=False, label='1.45 seconds, SD='+str(x1_sd))
    sns.distplot(x2, rug=True, hist=False, label='2.9 seconds, SD='+str(x2_sd))
    sns.distplot(x3, rug=True, hist=False, label='5.8 seconds, SD='+str(x3_sd))
"""
#%%
"""
------- Distribution plots - all subjects, all intervals
"""
x1=[]
x2=[]
x3=[]
#pax = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
#       '11', '12', '13', '14', '15', '16', '17', '18']
pax = ['1','2','1369','7','8']
for i in range(1,7): # 1, 2, 3, 4, 5, 6
    for k in pax:
        data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
#        data_path = 'D:/ScaledTime/Matlab data/'
        data_path_subj = os.path.join(data_path, 'ScaledTime'+k)
        os.chdir(data_path_subj)
        for j in ['1.45','2.9','5.8']:
            name = 'ScaledTime_Play_subj_'+ k +'_bl_' + str(i) + '_int_' + j + '.txt'
            if os.path.isfile(name) and os.path.exists(name):
                int_length=np.genfromtxt(name, dtype='str')
                for n in range(1,16):
                    int_single = int_length[n,15] # 17
                    int_single = float(int_single)
                    if j == '1.45':
                        x1.append(int_single)
                    if j == '2.9':
                        x2.append(int_single)
                    if j == '5.8':
                        x3.append(int_single)
                    
# A function to truncate the number of decimal places
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier     
               
# Calculate the means and the standard deviations 
x1_arr = np.array(x1)
x2_arr = np.array(x2)
x3_arr = np.array(x3)
#
x1_mean = np.mean(x1_arr, axis=0)
x2_mean = np.mean(x2_arr, axis=0)
x3_mean = np.mean(x3_arr, axis=0)
#
x1_sd = truncate(np.std(x1_arr, axis=0), 3)
x2_sd = truncate(np.std(x2_arr, axis=0), 3)
x3_sd = truncate(np.std(x3_arr, axis=0), 3)

# Keeps all values between mean +/- 3sd
# x1
x1_final = [x for x in x1 if (x > x1_mean - 3*x1_sd)]
x1_final = [x for x in x1_final if (x < x1_mean + 3*x1_sd)]
# x2
x2_final = [x for x in x2 if (x > x2_mean - 3*x2_sd)]
x2_final = [x for x in x2_final if (x < x2_mean + 3*x2_sd)]
# x3
x3_final = [x for x in x3 if (x > x3_mean - 3*x3_sd)]
x3_final = [x for x in x3_final if (x < x3_mean + 3*x3_sd)] # changed this to 2, it was too long

# Calculate the SDs and Means of the data without the outliers
x1_fin_arr = np.array(x1_final)
x2_fin_arr = np.array(x2_final)
x3_fin_arr = np.array(x3_final)
#
x1_fin_mean = np.mean(x1_fin_arr, axis=0)
x2_fin_mean = np.mean(x2_fin_arr, axis=0)
x3_fin_mean = np.mean(x3_fin_arr, axis=0)
#
x1_fin_sd = truncate(np.std(x1_fin_arr, axis=0), 3)
x2_fin_sd = truncate(np.std(x2_fin_arr, axis=0), 3)
x3_fin_sd = truncate(np.std(x3_fin_arr, axis=0), 3)

#%% Plot

# Check this out https://python-graph-gallery.com/24-histogram-with-a-boxplot-on-top-seaborn/

with sns.color_palette("RdBu_r", n_colors=3): # "Blues_r"
    plt.title("Density distributions of all interval productions", fontsize=14)
    plt.ylabel("Density", fontsize=14) 
    plt.xlabel("Produced intervals (s)", fontsize=14)         
    gl = sns.distplot(x1_final, rug=False, hist=False, color="steelblue", kde_kws={"shade": True}, 
                 label = '1.45 seconds, ' + str(len(x1_final)) + ' intervals, SD=' + str(x1_fin_sd))
    sns.distplot(x2_final, rug=False, hist=False, color="thistle", kde_kws={"shade": True},
                 label = '2.9 seconds, ' + str(len(x2_final)) + ' intervals, SD=' + str(x2_fin_sd))
    sns.distplot(x3_final, rug=False, hist=False, color="indianred", kde_kws={"shade": True},
                 label = '5.8 seconds, ' + str(len(x3_final)) + ' intervals, SD=' + str(x3_fin_sd))
    plt.yticks([], [])
    plt.xticks([1.45, 2.9, 5.8])
    plt.xlim(right=10)
    plt.grid(b=None)
    
#    plt.tick_params(
#        axis='y',          # changes apply to the x-axis
#        which='both',      # both major and minor ticks are affected
#        bottom=False,      # ticks along the bottom edge are off
#        top=False,         # ticks along the top edge are off
#        labelbottom=False) # labels along the bottom edge are off
    
x1_med = np.median(x1_final)
x2_med = np.median(x2_final)
x3_med = np.median(x3_final)

lwm = 1.25
lwt = 1.
m_color = 'dimgrey'
plt.axvline(x1_med, ymax=0.93, linestyle='-.', linewidth=lwm, color=m_color) # ymax=0.91
#            label = '1.45 sec median')
#plt.text(1.7,0.2,'median',rotation=90)
plt.axvline(1.45, ymax=0.77, linestyle='-', linewidth=lwt, color='navy') # ymax=0.95
#
plt.axvline(x2_med, ymax=0.73, linestyle='-.', linewidth=lwm, color=m_color) # ymax=0.63 
#            label = '2.9 sec median')
#plt.text(3.1,0.2,'median',rotation=90)
plt.axvline(2.9, ymax=0.73, linestyle='-', linewidth=lwt, color='indigo') # ymax=0.65
#
plt.axvline(x3_med, ymax=0.44, linestyle='-.', linewidth=lwm, color=m_color, # ymax=0.285
            label = 'Medians')
#plt.text(6.1,0.2,'median',rotation=90)
plt.axvline(5.8, ymax=0.44, linestyle='-', linewidth=lwt, color='maroon') # ymax=0.28

#plt.plot([], [], ' ', label="-.-. Medians")

## Annotate with text + Arrow
#plt.annotate('This point is interesting!', xy=(25, 50), xytext=(0, 80),
#             arrowprops=dict(facecolor='black', shrink=0.05))
sns.despine()
plt.legend()
plt.grid(b=None)



# How to plot the mean and give the values of mean and std
# https://stackoverflow.com/questions/44960170/plotting-mean-lines-for-different-hue-data-on-a-seaborn-facetgrid-plot
#def vertical_mean_line(x, **kwargs):
#    ls = {"0":"-","1":"--"}
#    plt.axvline(x.mean(), linestyle =ls[kwargs.get("label","0")], 
#                color = kwargs.get("color", "g"))
#    txkw = dict(size=12, color = kwargs.get("color", "g"), rotation=90)
#    tx = "mean: {:.2f}, std: {:.2f}".format(x.mean(),x.std())
#    plt.text(x.mean()+1, 0.052, tx, **txkw)
#    
#gl.map(vertical_mean_line(x1_final, label="bla", color="steelblue")) 

#%%       
"""

# A function to truncate the number of decimal places
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

x1_mean = sum(x1)/len(x1)
x1_sd = truncate(np.std(x1),3)
x2_mean = sum(x2)/len(x2)
x2_sd = truncate(np.std(x2),3)
x3_mean = sum(x3)/len(x3)
x3_sd = truncate(np.std(x3),3)


x1_remove = []
x2_remove = []
x3_remove = []
for (i, j, k) in zip(range(len(x1)), range(len(x2)), range(len(x3))):
    if (x1[i] < (x1_mean-3*x1_sd)) or (x1[i] > (x1_mean+(3*x1_sd))):
        x1_remove.append(i)
#        x1.pop(i)
    if (x2[i] < (x2_mean-3*x2_sd)) or (x2[i] > (x2_mean+(3*x2_sd))):
        x2_remove.append(j)
#        x2.pop(j)
    if (x3[i] < (x3_mean-3*x3_sd)) or (x3[i] > (x3_mean+(3*x3_sd))):
        x3_remove.append(k)
#        x3.pop(k)
        
for (i, j, k) in zip(range(len(x1_remove)), range(len(x2_remove)), range(len(x3_remove))):
    x1.pop(x1_remove[i])
    x2.pop(x1_remove[j])
    x3.pop(x1_remove[k])

""" 



"""
------- Distribution plots of all blocks per interval per single subject

os.chdir("C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/ScaledTime8/")
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
interval = '1.45'
subject = '8'
for i in range(1,7): # 1, 2, 3, 4, 5, 6
        name = 'ScaledTime_Play_subj_'+subject+'_bl_' + str(i) + '_int_'+interval+'.txt'
        int_length=np.genfromtxt(name, dtype='str')
        for k in range(1,16):
            int_single = int_length[k,15]
            int_single = float(int_single)
            if i == 1:
                x1.append(int_single)
            if i == 2:
                x2.append(int_single)
            if i == 3:
                x3.append(int_single)
            if i == 4:
                x4.append(int_single)
            if i == 5:
                x5.append(int_single)
            if i == 6:
                x6.append(int_single)
                
plt.title("1.45 second interval productions for subject 04 across all blocks")
plt.ylabel("Density", fontsize=12) 
plt.xlabel("Produced intervals of 1.45 seconds", fontsize=12)         
sns.distplot(x1, rug=True, hist=False, color='r', label='Block 1')
sns.distplot(x2, rug=True, hist=False, color='orange', label='Block 2')
sns.distplot(x3, rug=True, hist=False, color='y', label='Block 3')
sns.distplot(x4, rug=True, hist=False, color='g', label='Block 4')
sns.distplot(x5, rug=True, hist=False, color='blue', label='Block 5')
sns.distplot(x6, rug=True, hist=False, color='violet', label='Block 6')
"""


"""
------- Distribution plots of all blocks of all subjects per interval

x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
cur_int='5.8'
outliers_lim=9
for i in range(1,7): # 1, 2, 3, 4, 5, 6
        for l in ['1', '2', '7', '8', '1369']:
            data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
            data_path_subj = os.path.join(data_path, 'ScaledTime'+l)
            os.chdir(data_path_subj)
            name = 'ScaledTime_Play_subj_' + l + '_bl_' + str(i) + '_int_' + cur_int + '.txt'
            if os.path.isfile(name) and os.path.exists(name):
                int_length=np.genfromtxt(name, dtype='str')
                for k in range(1,16):
                    int_single = int_length[k,15]
                    int_single = float(int_single)
                    if int_single < outliers_lim:
                        if i == 1:
                            x1.append(int_single)
                        elif i == 2:
                            x2.append(int_single)
                        elif i == 3:
                            x3.append(int_single)
                        elif i == 4:
                            x4.append(int_single)
                        elif i == 5:
                            x5.append(int_single)
                        elif i == 6:
                            x6.append(int_single)
                    else:
                        pass

# A function to truncate the number of decimal places
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier

x1_mean = sum(x1)/len(x1)
x1_sd = truncate(np.std(x1),3)
x2_mean = sum(x2)/len(x2)
x2_sd = truncate(np.std(x2),3)
x3_mean = sum(x3)/len(x3)
x3_sd = truncate(np.std(x3),3)
x4_mean = sum(x4)/len(x4)
x4_sd = truncate(np.std(x4),3)
x5_mean = sum(x5)/len(x5)
x5_sd = truncate(np.std(x5),3)
x6_mean = sum(x6)/len(x6)
x6_sd = truncate(np.std(x6),3)

#with sns.color_palette("RdBu_r", 6):
with sns.diverging_palette(145, 10, s=85, l=25, n=6):
    plt.title(cur_int+" second interval productions across blocks")
    plt.ylabel("Density", fontsize=12) 
    plt.xlabel("Produced intervals (s)", fontsize=12) 
#    plt.xlim(0,30) 
    sns.distplot(x1, rug=True, hist=False, label='Block 1, SD='+str(x1_sd))
    sns.distplot(x2, rug=True, hist=False, label='Block 2, SD='+str(x2_sd))
    sns.distplot(x3, rug=True, hist=False, label='Block 3, SD='+str(x3_sd))
    sns.distplot(x4, rug=True, hist=False, label='Block 4, SD='+str(x4_sd))
    sns.distplot(x5, rug=True, hist=False, label='Block 5, SD='+str(x5_sd))
    sns.distplot(x6, rug=True, hist=False, label='Block 6, SD='+str(x6_sd))
"""


"""
------- Standardize the distribution plots per pax ??????

os.chdir("C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/ScaledTime1_Sebastien/")


from sklearn.preprocessing import StandardScaler

x=[]
for i in range(1,7): # 1, 2, 3, 4, 5, 6
#for j in ['1.45','2.9','5.8']:
    name = 'ScaledTime_Play_subj_1_bl_'+str(i)+'_int_5.8.txt'
    int_length=np.genfromtxt(name, dtype='str')
    for j in range(1,16):
        int_single = int_length[j,15]
        int_single = float(int_single)
        x.append(int_single)

scaler = StandardScaler().fit(x)
sns.distplot(scaler, rug=True, hist=False)
"""


"""
------- Correlation of produced duration with target duration
"""

#    x[:,(i-1)]=int_length[1:,15]
    
#bl01_int1=np.genfromtxt("ScaledTime_Play_subj_1369_bl_1_int_1.45.txt", dtype='str')
#x=bl01_int1[1:,15]
#x = list(map(float, x))
#sns.distplot(x)


#f=open("ScaledTime_Play_subj_1369_bl_1_int_1.45.txt", "r")



"""
---- [Fixed] Plot scatter - y axis is CV (precision) per block of one subject, x axis are the 3 intervals
"""
x1=[]
x2=[]
x3=[]
cv1_all_blocks=[]
cv2_all_blocks=[]
cv3_all_blocks=[]
for i in range(1,7): # 1, 2, 3, 4, 5, 6
#    for k in ['1','2','1369','7','8']:
    for k in ['1', '2', '1002', '2001']:
        data_path = 'D:/ScaledTime/Matlab data/'
#        data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
        data_path_subj = os.path.join(data_path, 'ScaledTime'+k)
        os.chdir(data_path_subj)
        for j in ['1.45','2.9','5.8']:
            name = 'ScaledTime_Play_subj_'+ k +'_bl_' + str(i) + '_int_' + j + '.txt'
            if os.path.isfile(name) and os.path.exists(name):
                int_length=np.genfromtxt(name, dtype='str')
                for n in range(1,16):
                    int_single = int_length[n,17]
                    int_single = float(int_single)
                    if int_single < 9:
                        if j == '1.45':
                            x1.append(int_single)
                        if j == '2.9':
                            x2.append(int_single)
                        if j == '5.8':
                            x3.append(int_single)
                    else:
                        pass
#    x1_norm = []
#    for q in range(len(x1)):
#        x1_norm.append(x1[q]/1.45)
    x1_mean = sum(x1)/len(x1)
    x1_sd = np.std(x1)
    cv1 = x1_sd / x1_mean
    cv1_all_blocks.append(cv1)
    #------
#    x2_norm = []
#    for w in range(len(x2)):
#        x2_norm.append(x2[w]/2.9)
    x2_mean = sum(x2)/len(x2)
    x2_sd = np.std(x2)
    cv2 = x2_sd / x2_mean
    cv2_all_blocks.append(cv2)
    #------
#    x3_norm = []
#    for e in range(len(x1)):
#        x3_norm.append(x3[e]/2.9)
    x3_mean = sum(x3)/len(x3)
    x3_sd = np.std(x3)
    cv3 = x3_sd / x3_mean
    cv3_all_blocks.append(cv3)

with sns.color_palette("GnBu_d"):
    groups = ("Block 01", "Block 02", "Block 03", "Block 04", "Block 05", "Block 06")
    for i, groups in zip(cv1_all_blocks, groups):
        plt.scatter(1,i, linewidths=3, label=groups)
    for j in cv2_all_blocks:
        plt.scatter(2,j, linewidths=3)
    for k in cv3_all_blocks:
        plt.scatter(3,k, linewidths=3)
    plt.xlim(0,4)
    x = np.array([ 1, 2, 3])
    my_xticks = ['1.45', '2.9', '5.8']
    plt.xticks(x, my_xticks)
    plt.ylabel("Coefficient of Variation (CV)", fontsize=12) 
    plt.xlabel("Produced intervals (s)", fontsize=12) 
    plt.title("CV per produced interval, all blocks, all participants")
    plt.legend(loc='upper right')
    plt.show()



"""
---- Plot scatter - y axis is ER (accuracy) per block of one subject, x axis are the 3 intervals
"""
x1=[]
x2=[]
x3=[]
er1_all_blocks=[]
er2_all_blocks=[]
er3_all_blocks=[]
for i in range(1,7): # 1, 2, 3, 4, 5, 6
    for k in ['1','2','1369','7','8']:
        data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
        data_path_subj = os.path.join(data_path, 'ScaledTime'+k)
        os.chdir(data_path_subj)
        for j in ['1.45','2.9','5.8']:
            name = 'ScaledTime_Play_subj_'+ k +'_bl_' + str(i) + '_int_' + j + '.txt'
            if os.path.isfile(name) and os.path.exists(name):
                int_length=np.genfromtxt(name, dtype='str')
                for n in range(1,16):
                    int_single = int_length[n,15]
                    int_single = float(int_single)
                    if int_single < 9:
                        if j == '1.45':
                            x1.append(int_single)
                        if j == '2.9':
                            x2.append(int_single)
                        if j == '5.8':
                            x3.append(int_single)
                    else:
                        pass
#    x1_norm = []
#    for q in range(len(x1)):
#        x1_norm.append(x1[q]/1.45)
    x1_mean = sum(x1)/len(x1)
    x1_target = 1.45
    er1 = x1_mean / x1_target
    er1_all_blocks.append(er1)
    #------
#    x2_norm = []
#    for w in range(len(x2)):
#        x2_norm.append(x2[w]/2.9)
    x2_mean = sum(x2)/len(x2)
    x2_target = 2.9
    er2 = x2_mean / x2_target
    er2_all_blocks.append(er2)
    #------
#    x3_norm = []
#    for e in range(len(x1)):
#        x3_norm.append(x3[e]/2.9)
    x3_mean = sum(x3)/len(x3)
    x3_target = 5.8
    er3 = x3_mean / x3_target
    er3_all_blocks.append(er3)

with sns.color_palette("GnBu_d"):
    groups = ("Block 01", "Block 02", "Block 03", "Block 04", "Block 05", "Block 06")
    for i, groups in zip(er1_all_blocks, groups):
        plt.scatter(1,i, linewidths=3, label=groups)
    for j in er2_all_blocks:
        plt.scatter(2,j, linewidths=3)
    for k in er3_all_blocks:
        plt.scatter(3,k, linewidths=3)
    plt.xlim(0,4)
    x = np.array([ 1, 2, 3])
    my_xticks = ['1.45', '2.9', '5.8']
    plt.xticks(x, my_xticks)
    plt.ylabel("Error Rate (ER)", fontsize=12) 
    plt.xlabel("Produced intervals (s)", fontsize=12) 
    plt.title("ER per produced interval, all blocks, all participants")
    plt.legend(loc='upper right')
    plt.show()


"""
---- [NOT Fixed] Plot scatter - y axis is CV per block of one subject, x axis are the 3 intervals
"""
#import numpy as np
#x1=[]
#x2=[]
#x3=[]
#cv1_all_blocks=[]
#cv2_all_blocks=[]
#cv3_all_blocks=[]
#for i in range(1,7): # 1, 2, 3, 4, 5, 6
##    for k in ['1', '7', '8', '1369']:
#    for k in ['8']:
#        data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
#        data_path_subj = os.path.join(data_path, 'ScaledTime'+k)
#        os.chdir(data_path_subj)
#        for j in ['1.45','2.9','5.8']:
#            name = 'ScaledTime_Play_subj_'+ k +'_bl_' + str(i) + '_int_' + j + '.txt'
#            if os.path.isfile(name) and os.path.exists(name):
#                int_length=np.genfromtxt(name, dtype='str')
#                for n in range(1,16):
#                    int_single = int_length[n,15]
#                    int_single = float(int_single)
#                    if int_single < 9:
#                        if j == '1.45':
#                            x1.append(int_single)
#                        if j == '2.9':
#                            x2.append(int_single)
#                        if j == '5.8':
#                            x3.append(int_single)
#                    else:
#                        pass
#
#    x1_mean = sum(x1)/len(x1)
#    x1_sd = np.std(x1)
#    cv1 = x1_sd / x1_mean
#    cv1_all_blocks.append(cv1)
#    #------
#    x2_mean = sum(x2)/len(x2)
#    x2_sd = np.std(x2)
#    cv2 = x2_sd / x2_mean
#    cv2_all_blocks.append(cv2)
#    #------
#    x3_mean = sum(x3)/len(x3)
#    x3_sd = np.std(x3)
#    cv3 = x3_sd / x3_mean
#    cv3_all_blocks.append(cv3)
#
#with sns.color_palette("GnBu_d"):
#    for i in cv1_all_blocks:
#        plt.scatter(1,i, linewidths=2)
#    for j in cv2_all_blocks:
#        plt.scatter(2,j, linewidths=2)
#    for k in cv3_all_blocks:
#        plt.scatter(3,k, linewidths=2)
#    plt.xlim(0,4)
#    x = np.array([ 1, 2, 3])
#    my_xticks = ['1.45', '2.9', '5.8']
#    plt.xticks(x, my_xticks)
#    plt.title("CV per produced interval, all blocks, all subjects")
#    plt.ylabel("Coefficient of Variation (CV)", fontsize=12) 
#    plt.xlabel("Produced intervals (s)", fontsize=12) 
#    plt.show()
#
#



"""
---- Objective - subjective duration
"""
x1=[]
x2=[]
x3=[]
pax = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
for i in range(1,7): # 1, 2, 3, 4, 5, 6
#    for k in ['1', '7', '8', '1369']:
    for k in pax:
        data_path = 'D:/scaledTime/Matlab data/'
        data_path_subj = os.path.join(data_path, 'ScaledTime'+k)
        os.chdir(data_path_subj)
        for j in ['1.45','2.9','5.8']:
            name = 'ScaledTime_Play_subj_'+ k +'_bl_' + str(i) + '_int_' + j + '.txt'
            if os.path.isfile(name) and os.path.exists(name):
                int_length=np.genfromtxt(name, dtype='str')
                for n in range(1,16):
                    int_single = int_length[n,17]
                    int_single = float(int_single)
                    if j == '1.45':
                        x1.append(int_single)
                    if j == '2.9':
                        x2.append(int_single)
                    if j == '5.8':
                        x3.append(int_single)

# A function to truncate the number of decimal places
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier     
               
# Calculate the means and the standard deviations 
x1_arr = np.array(x1)
x2_arr = np.array(x2)
x3_arr = np.array(x3)
#
x1_mean = np.mean(x1_arr, axis=0)
x2_mean = np.mean(x2_arr, axis=0)
x3_mean = np.mean(x3_arr, axis=0)
#
x1_sd = truncate(np.std(x1_arr, axis=0), 3)
x2_sd = truncate(np.std(x2_arr, axis=0), 3)
x3_sd = truncate(np.std(x3_arr, axis=0), 3)

# Keeps all values between mean +/- 3sd
# x1
x1_final = [x for x in x1 if (x > x1_mean - 3*x1_sd)]
x1_final = [x for x in x1_final if (x < x1_mean + 3*x1_sd)]
# x2
x2_final = [x for x in x2 if (x > x2_mean - 3*x2_sd)]
x2_final = [x for x in x2_final if (x < x2_mean + 3*x2_sd)]
# x3
x3_final = [x for x in x3 if (x > x3_mean - 3*x3_sd)]
x3_final = [x for x in x3_final if (x < x3_mean + 2*x3_sd)] # also changed this to 2

# Calculate the SDs and Means of the data without the outliers
x1_fin_arr = np.array(x1_final)
x2_fin_arr = np.array(x2_final)
x3_fin_arr = np.array(x3_final)
#
x1_fin_mean = np.mean(x1_fin_arr, axis=0)
x2_fin_mean = np.mean(x2_fin_arr, axis=0)
x3_fin_mean = np.mean(x3_fin_arr, axis=0)
#
x1_fin_sd = truncate(np.std(x1_fin_arr, axis=0), 3)
x2_fin_sd = truncate(np.std(x2_fin_arr, axis=0), 3)
x3_fin_sd = truncate(np.std(x3_fin_arr, axis=0), 3)

# Plot
with sns.color_palette("GnBu_d"):
    for i in x1_final:
        plt.scatter(1.45,i, linewidths=1)
    x1_mean = x1_fin_mean
    for j in x2_final:
        plt.scatter(2.9,j, linewidths=1)
    x2_mean = x2_fin_mean
    for k in x3_final:
        plt.scatter(5.8,k, linewidths=1)
    x3_mean = x3_fin_mean

    x = np.array([ 1.45, 2.9, 5.8])
    my_xticks = ['1.45', '2.9', '5.8']
    plt.xticks(x, my_xticks)
    plt.title("All subjects, all blocks")
    plt.ylabel("Subjective duration (s)", fontsize=12) 
    plt.xlabel("Objective duration (s)", fontsize=12)
    plt.plot(np.arange(0,7,0.1),np.arange(0,7,0.1), color='silver', marker=',', label='Target durations')
    plt.plot(x,[x1_mean,x2_mean,x3_mean], color='maroon', marker='o', label='Subjective durations mean')
    plt.legend(loc='lower right')
    plt.show()



#%%
"""
------- Sequential effects
"""
x1=[]
x2=[]
x3=[]
x4=[]
x5=[]
x6=[]
x_short=[]
x_long=[]
cur_int='5.8'
outliers_lim=12
for i in range(1,7): # 1, 2, 3, 4, 5, 6
        for l in ['1', '2', '7', '8', '1369']:
            data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
            data_path_subj = os.path.join(data_path, 'ScaledTime'+l)
            os.chdir(data_path_subj)
            name = 'ScaledTime_Play_subj_' + l + '_bl_' + str(i) + '_int_' + cur_int + '.txt'
            if os.path.isfile(name) and os.path.exists(name):
                int_length=np.genfromtxt(name, dtype='str')
                for k in range(1,16):
                    int_single = int_length[k,15]
                    int_single = float(int_single)
                    if int_single < outliers_lim:
                        if i == 1:
                            x1.append(int_single)
                            x_long.append(int_single)
                            
                        elif i == 2:
                            x2.append(int_single)
                            x_short.append(int_single)
                            
                        elif i == 3:
                            x3.append(int_single)
                            x_long.append(int_single)
                            
                        elif i == 4:
                            x4.append(int_single)
                            x_short.append(int_single)
                            
                        elif i == 5:
                            x5.append(int_single)
#                            x_short.append(int_single)
                            
                        elif i == 6:
                            x6.append(int_single)
                            x_long.append(int_single)
                    else:
                        pass

def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier    

#%% Not fixed for these arrays etc 
               
## Calculate the means and the standard deviations 
#x1_arr = np.array(x1)
#x2_arr = np.array(x2)
#x3_arr = np.array(x3)
##
#x1_mean = np.mean(x1_arr, axis=0)
#x2_mean = np.mean(x2_arr, axis=0)
#x3_mean = np.mean(x3_arr, axis=0)
##
#x1_sd = truncate(np.std(x1_arr, axis=0), 3)
#x2_sd = truncate(np.std(x2_arr, axis=0), 3)
#x3_sd = truncate(np.std(x3_arr, axis=0), 3)
#
## Keeps all values between mean +/- 3sd
## x1
#x1_final = [x for x in x1 if (x > x1_mean - 3*x1_sd)]
#x1_final = [x for x in x1_final if (x < x1_mean + 3*x1_sd)]
## x2
#x2_final = [x for x in x2 if (x > x2_mean - 3*x2_sd)]
#x2_final = [x for x in x2_final if (x < x2_mean + 3*x2_sd)]
## x3
#x3_final = [x for x in x3 if (x > x3_mean - 3*x3_sd)]
#x3_final = [x for x in x3_final if (x < x3_mean + 3*x3_sd)] # changed this to 2, it was too long
#
## Calculate the SDs and Means of the data without the outliers
#x1_fin_arr = np.array(x1_final)
#x2_fin_arr = np.array(x2_final)
#x3_fin_arr = np.array(x3_final)
##
#x1_fin_mean = np.mean(x1_fin_arr, axis=0)
#x2_fin_mean = np.mean(x2_fin_arr, axis=0)
#x3_fin_mean = np.mean(x3_fin_arr, axis=0)
##
#x1_fin_sd = truncate(np.std(x1_fin_arr, axis=0), 3)
#x2_fin_sd = truncate(np.std(x2_fin_arr, axis=0), 3)
#x3_fin_sd = truncate(np.std(x3_fin_arr, axis=0), 3)
    #%%

######################### 2.9
#x_s_sd = truncate(np.std(x_short),3)
#x_l_sd = truncate(np.std(x_long),3)
#x3_sd = truncate(np.std(x3),3)
#
##with sns.color_palette("GnBu"):
#with sns.diverging_palette(145, 10, s=85, l=25, n=3):
#    plt.title(cur_int+" second interval productions across blocks")
#    plt.ylabel("Density", fontsize=12) 
#    plt.xlabel("Produced intervals", fontsize=12) 
##    plt.xlim(0,30)
#    sns.distplot(x_short, rug=True, hist=False, color='green', label='Blocks 1, 4, 5 - after 1.45s, SD='+str(x_s_sd))
#    sns.distplot(x3, rug=True, hist=False, color='pink', label='Block 3 - after 2.9s, SD='+str(x3_sd))
#    sns.distplot(x_long, rug=True, hist=False, color='maroon', label='Blocks 2, 6 - after 5.8s, SD='+str(x_l_sd))
#
#
######################### 1.45
#x_s_sd = truncate(np.std(x_short),3)
#x_l_sd = truncate(np.std(x_long),3)
#x1_sd = truncate(np.std(x1),3)
#
#with sns.diverging_palette(145, 10, s=85, l=25, n=3):
#    plt.title(cur_int+" second interval productions across blocks")
#    plt.ylabel("Density", fontsize=12) 
#    plt.xlabel("Produced intervals", fontsize=12) 
#    sns.distplot(x_short, rug=True, hist=False, color='green', label='Blocks 4, 6 - after 2.9s, SD='+str(x_s_sd))
#    sns.distplot(x3, rug=True, hist=False, color='pink', label='Block 1 - first interval, SD='+str(x1_sd))
#    sns.distplot(x_long, rug=True, hist=False, color='maroon', label='Blocks 2, 3, 5 - after 5.8s, SD='+str(x_l_sd))

######################## 5.8
x_s_sd = truncate(np.std(x_short),3)
x_l_sd = truncate(np.std(x_long),3)
x5_sd = truncate(np.std(x5),3)
#%%
with sns.diverging_palette(145, 10, s=85, l=25, n=3):
    plt.title(cur_int+" second interval productions across blocks")
    plt.ylabel("Density", fontsize=12) 
    plt.xlabel("Produced intervals", fontsize=12) 
    sns.distplot(x_short, rug=False, hist=False, color='indianred', kde_kws={"shade": True},
                 label='Blocks 2, 4 - after 1.45s')
    sns.distplot(x3, rug=False, hist=False, color='cornflowerblue', kde_kws={"shade": True},
                 label='Block 5 - after 5.8s')
    sns.distplot(x_long, rug=False, hist=False, color='green', kde_kws={"shade": True},
                 label='Blocks 1, 3, 6 - after 2.9s')
    plt.yticks([], [])
    plt.xticks([5.8])
    plt.xlim(right=10)
sns.despine()
plt.legend(loc='upper left')

#%%
#%%
#%% CV-ER box plot

x1=[]
x2=[]
x3=[]


#pax = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
#       '11', '12', '13', '14', '15', '16', '17', '18']
pax = ['1', '2', '7', '8', '1369']
for k in pax:
    for i in range(1,7): # 1, 2, 3, 4, 5, 6
        data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
#        data_path = 'D:/ScaledTime/Matlab data/'
        data_path_subj = os.path.join(data_path, 'ScaledTime'+k)
        os.chdir(data_path_subj)
        for j in ['1.45','2.9','5.8']:
            name = 'ScaledTime_Play_subj_'+ k +'_bl_' + str(i) + '_int_' + j + '.txt'
            if os.path.isfile(name) and os.path.exists(name):
                int_length=np.genfromtxt(name, dtype='str')
                for n in range(1,16):
                    int_single = int_length[n,15] # 17
                    int_single = float(int_single)
                    if j == '1.45':
                        x1.append(int_single)
                    if j == '2.9':
                        x2.append(int_single)
                    if j == '5.8':
                        x3.append(int_single)
                    
# A function to truncate the number of decimal places
def truncate(n, decimals=0):
    multiplier = 10 ** decimals
    return int(n * multiplier) / multiplier  

# Calculate the means and the standard deviations 
x1_arr = np.array(x1)
x2_arr = np.array(x2)
x3_arr = np.array(x3)
#
x1_all_mean = np.mean(x1_arr, axis=0)
x2_all_mean = np.mean(x2_arr, axis=0)
x3_all_mean = np.mean(x3_arr, axis=0)
#
x1_all_sd = truncate(np.std(x1_arr, axis=0), 3)
x2_all_sd = truncate(np.std(x2_arr, axis=0), 3)
x3_all_sd = truncate(np.std(x3_arr, axis=0), 3)

#%%

x1=[]
x2=[]
x3=[]

cvs1 = []
cvs2 = []
cvs3 = []
ers1 = []
ers2 = []
ers3 = []

rows = []

# subject 11 is 111 and 112
#pax = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 
#       '11', '12', '13', '14', '15', '16', '17', '18']
pax = ['1', '2', '7', '8', '1369']

#df1 = pd.DataFrame({'cv1': [], 'er1': [], 'cv2': [], 'er2': [], 'cv3': [], 'er3': []})


for k in pax:
    for i in range(1,7): # 1, 2, 3, 4, 5, 6
        data_path = 'C:/Users/Dragana/Documents/MATLAB/m_M1_internship/Multifracts/Data/'
#        data_path = 'D:/ScaledTime/Matlab data/'
        data_path_subj = os.path.join(data_path, 'ScaledTime'+k)
        os.chdir(data_path_subj)
        for j in ['1.45','2.9','5.8']:
            name = 'ScaledTime_Play_subj_'+ k +'_bl_' + str(i) + '_int_' + j + '.txt'
            if not os.path.exists(name):
                continue
            else:
                int_length=np.genfromtxt(name, dtype='str')
                for n in range(1,16):
                    int_single = int_length[n,15] # 17
                    int_single = float(int_single)
                    if j == '1.45':
                        x1.append(int_single)
                    if j == '2.9':
                        x2.append(int_single)
                    if j == '5.8':
                        x3.append(int_single)
                        
        # Keeps all values between mean +/- 3sd
        # x1
    x1_final = [x for x in x1 if (x > x1_all_mean - 3*x1_all_sd)]
    x1_final = [x for x in x1_final if (x < x1_all_mean + 3*x1_all_sd)]
    # x2
    x2_final = [x for x in x2 if (x > x2_all_mean - 3*x2_all_sd)]
    x2_final = [x for x in x2_final if (x < x2_all_mean + 3*x2_all_sd)]
    # x3
    x3_final = [x for x in x3 if (x > x3_all_mean - 3*x3_all_sd)]
    x3_final = [x for x in x3_final if (x < x3_all_mean + 3*x3_all_sd)] # changed this to 2, it was too long

    # Calculate the SDs and Means of the data per subject w/o the outliers

    x1_mean = np.mean(x1_final)
    x2_mean = np.mean(x2_final)
    x3_mean = np.mean(x3_final)
    
    x1_sd = np.std(x1_final)
    x2_sd = np.std(x2_final)
    x3_sd = np.std(x3_final)
    
    x1_target = 1.45
    x2_target = 2.9
    x3_target = 5.8    

    # Calculate the CVs  
    cv1 = x1_sd / x1_mean
    cv2 = x2_sd / x2_mean
    cv3 = x3_sd / x3_mean
    
    cvs1.append(cv1)
    cvs2.append(cv2)  
    cvs3.append(cv3)
    
    # Calculate the ERs
    er1 = x1_mean / x1_target
    er2 = x2_mean / x2_target
    er3 = x3_mean / x3_target
    
    ers1.append(er1)
    ers2.append(er2)
    ers3.append(er3)


#%% Box plot
import pandas as pd
import seaborn as sns
import itertools
import matplotlib.style as style
#%matplotlib qt

#ERs = [ers1, ers2, ers3]
#ERs_flat = list(itertools.chain.from_iterable(ERs)) # we have list of lists, and we need a flat list
#CVs = [cvs1, cvs2, cvs3]
#CVs_flat = list(itertools.chain.from_iterable(CVs))
#ints = [1.45, 1.45, 1.45, 1.45, 1.45, 
#        2.9,  2.9,  2.9,  2.9,  2.9, 
#        5.8,  5.8,  5.8,  5.8,  5.8]

CV_ER = [ers1, ers2, ers3, cvs1, cvs2, cvs3]
CV_ER_flat = list(itertools.chain.from_iterable(CV_ER))

ints = [1.45, 1.45, 1.45, 1.45, 1.45, 
        2.9,  2.9,  2.9,  2.9,  2.9, 
        5.8,  5.8,  5.8,  5.8,  5.8,
        1.45, 1.45, 1.45, 1.45, 1.45, 
        2.9,  2.9,  2.9,  2.9,  2.9, 
        5.8,  5.8,  5.8,  5.8,  5.8]
cver_divis = ['ER', 'ER', 'ER', 'ER', 'ER',
              'ER', 'ER', 'ER', 'ER', 'ER',
              'ER', 'ER', 'ER', 'ER', 'ER',
              'CV', 'CV', 'CV', 'CV', 'CV',
              'CV', 'CV', 'CV', 'CV', 'CV',
              'CV', 'CV', 'CV', 'CV', 'CV']


df1 = pd.DataFrame({'CV':CV_ER_flat, 'Ints': ints, 'Division': cver_divis})


with sns.color_palette("GnBu_d"):
    sns.set_style("whitegrid")
#    style.use('seaborn-poster')
    # Draw a pointplot to show pulse as a function of three categorical factors
    spl = sns.catplot(x="Ints", y="CV_ER", hue = "Division", # alpha=1.5, # hue="kind", col="diet",
                    # capsize=.2, #palette=sns.color_palette("Reds", 9), # height=6, aspect=.75,
                    kind="point", data=df1)

    intss = ['1.45', '2.9', '5.8']
    plt.title("Average values of CV and ER per interval", fontsize=12)
    plt.xlabel("Produced intervals", fontsize=12) 
    plt.ylabel("Average values of CV and ER", fontsize=12) 
    spl.set_xticklabels(intss, fontsize=12)
    sns.despine()    
    plt.show()

    
