# -*- coding: utf-8 -*-
"""
Created on Sat Mar  8 16:49:50 2025

@author: David S. Grove
GitHUb:  https://github.com/GurnB/DSG_JunkDrawer
StatsPlus American Baseball Legion: https://statsplus.net/americanbaseballlegion/

Summary: Reads the Exported Draft history file for years 2038 -> 2051 (current) into individual Data Frame.
Then combines the separate DF into a single DF and then sorts the dat by TotalWAR (desc) to give an idea 
which teams have a better history of drafting rookie talent. Of course the 'older' the draftee, the better
chance their TotalWAR will be greater do to number of games played.

The Team listed in the results is the original team to draft the player, not the current Team Roster they 
are on.

Ability to write the report to an Excel Spreadsheet.

Future : * Build link between the Reported player and their individual StatsPlus Player Page.
         * Add indicator, per Player, it they are still active as a Player in the ABL. 
         * Populate Last Year in the league if Player no longer active in ABL.
         * update the Path & File links to the Draft History files to Variables.
         * replace the multiple code blocks (one per year) with a Def Function Loop
         * Explore possible use of StatsPlus API to pull initial reports.

"""
import numpy as np
import pandas as pd

filepath = 'C:\\Users\\dgrov\\Downloads\\ABL\\'
filename = 'statsplus2031.csv'
# ######

# ## Draft Year 2031
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2031.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2031')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2031= df.sort_values(by='TotalWAR', ascending=False)
 
# #############################


# ## Draft Year 2032
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2032.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2032')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2032 = df.sort_values(by='TotalWAR', ascending=False)
 
# #############################
# ## Draft Year 2033
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2033.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2033')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2033 = df.sort_values(by='TotalWAR', ascending=False)

# #############################
# ## Draft Year 2034
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2034.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2034')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2034 = df.sort_values(by='TotalWAR', ascending=False)
 
# #############################
# ## Draft Year 2035
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2035.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2035')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2035 = df.sort_values(by='TotalWAR', ascending=False)
 
# #############################
# ## Draft Year 2036
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2036.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2036')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2036= df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2037
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2037.csv')

# Create DataFrame
df = pd.DataFrame(data)
#Add Draft year
df.insert(10,'Year','2037')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2037 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2038
data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2038.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2038')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2038 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2039

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2039.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2039')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2039 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2040

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2040.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2040')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2040 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2041

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2041.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2041')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2041 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2042

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2042.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2042')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2042 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2043

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2043.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2043')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2043 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2044

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2044.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2044')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2044 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2045

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2045.csv')

# Create DataFrame
df = pd.DataFrame(data)
#Add Draft year
df.insert(10,'Year','2045')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2045 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2046

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2046.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2046')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2046 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2047

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2047.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2047')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2047 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2048

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2048.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2048')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2048 = df.sort_values(by='TotalWAR', ascending=False)

# #############################
# ## Draft Year 2049

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2049.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2049')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2049 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2050

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2050.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2050')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2050 = df.sort_values(by='TotalWAR', ascending=False)
# #############################
# ## Draft Year 2051

data = pd.read_csv('C:\\Users\\dgrov\\Downloads\\ABL\\statsplus2051.csv')

# Create DataFrame
df = pd.DataFrame(data)

#Add Draft year
df.insert(10,'Year','2051')

#Drop Columns
df.drop(columns=['Age','BatWAR', 'PitchWAR'], inplace=True)

search_column = 'TotalWAR'
search_value = 0

# Perform search and filter results
result = df[df[search_column] > search_value]

# Sort by 'TotalWAR' in descending order
df_2051 = df.sort_values(by='TotalWAR', ascending=False)
# ############################
# ###  Combine DataFrames #####

df = pd.concat([df_2031,df_2032,df_2033,df_2034,df_2035,df_2036,df_2037,df_2038, df_2039, df_2040, df_2041,df_2042, df_2043, df_2044, df_2045, df_2046, df_2047, df_2048, df_2049, df_2050, df_2051 ], ignore_index=True, sort=True)

df_sorted = df.sort_values(by='TotalWAR', ascending=False)
df_sorted.insert(0,'Rank', df_sorted['TotalWAR'].rank(method='dense', ascending=False).astype(int))

#df_sorted['TotalWAR'] = df_sorted['TotalWAR'].apply(lambda x: '{:,.2f}'.format(x))

df_reordered = df_sorted[['Rank', 'Rnd', 'Pick', 'Ovr', 'Player', 'Team', 'TotalWAR','Year']] # Reorder the columns
print(df_reordered [:100])  # Top 100 records


df_reordered.to_csv('C:\\Users\\dgrov\\Downloads\\ABL\\ABPL_Draft_Report.txt', sep='\t', index=False)
print(df_reordered.to_markdown('C:\\Users\\dgrov\\Downloads\\ABL\\ABPL_Draft_Report.txt',index=False, tablefmt="fancy_grid", floatfmt=(".2f"))) 
#df_sorted[:10].to_excel('C:\\Users\\dgrov\\Downloads\\ABL\\ABPL_Draft_Report.xlsx', index=False)
##df_sorted[:10].to_excel('ABPL_Draft_Report.xlsx', index=False)
   
    
