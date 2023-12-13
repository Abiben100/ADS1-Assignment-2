# Import all the neccesary functions
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# Define a function to remove rows with zeros
def remove_rows_with_zero(data_frame):
    # Iterate through the rows
    for index, row in data_frame.iterrows():
        # Check if the row contains the number 0
        if 0 in row.values:
            # Remove the entire row
            data_frame = data_frame.drop(index)

    return data_frame


def forest_data(forest_area):
    # Read the World Bank data into a pandas dataframe and cleaning the data by manipulation methods
    forest_area = pd.read_csv(
        "C:/Users/abigi/OneDrive/Desktop/Assignments/Applied data science 1/Applied data science 1 Assignment 2/Forest area/forest_area.csv", 
        skiprows = 4
    )
    forest_area = forest_area.loc[:, ~forest_area.columns.isin(["Country Code", "Indicator Name", "Indicator Code"])]
    forest_area = forest_area.dropna(axis = 1, how = "all")
    # Replace NaN values with 0
    forest_area = forest_area.fillna(0)
    # Calling the function to remove all rows of 0 from the data frames
    forest_area = remove_rows_with_zero(forest_area)
    # forest_area_years = remove_rows_with_zero(forest_area_years)
    forest_area_years = forest_area.set_index("Country Name").T
    forest_area_years = forest_area_years.dropna(how = "all")
    
    return forest_area, forest_area_years


forest_area, forest_area_years = forest_data("forest_area.csv")

# Statistical methods to explore data
forest_area_summary = forest_area_years.describe()
forest_area_median = forest_area_years.median()
forest_area_var = forest_area_years.var()


def arable_lnd_data(arable_land):
    # Read the World Bank data into a pandas dataframe and cleaning the data by manipulation methods
    arable_land = pd.read_csv(
        "C:/Users/abigi/OneDrive/Desktop/Assignments/Applied data science 1/Applied data science 1 Assignment 2/Arable land % land area/arable_land.csv", 
        skiprows = 4
    )
    arable_land = arable_land.loc[:, ~arable_land.columns.isin(["Country Code", "Indicator Name", "Indicator Code"])]
    arable_land = arable_land.dropna(axis = 1, how = "all")
    # Replace NaN values with 0
    arable_land = arable_land.fillna(0)
    # Calling the function to remove all rows of 0 from the data frames
    arable_land = remove_rows_with_zero(arable_land)
    arable_land_years = arable_land.set_index("Country Name").T
    arable_land_years = arable_land_years.dropna(how = "all")
    # Selecting years from 1990 to 2021
    arable_land_years = arable_land_years.iloc[29:]

    return arable_land, arable_land_years


arable_land, arable_land_years = arable_lnd_data("arable_land.csv")

# Statistical methods to explore data
arable_land_summary = arable_land_years.describe()
arable_land_median = arable_land_years.median()
arable_land_var = arable_land_years.var()


def co2_data(co2_emission):
    # Read the World Bank data into a pandas dataframe and cleaning the data by manipulation methods
    co2_emission = pd.read_csv(
        "C:/Users/abigi/OneDrive/Desktop/Assignments/Applied data science 1/Applied data science 1 Assignment 2/Co2 emission/co2_emission.csv", 
        skiprows = 4
    )
    co2_emission = co2_emission.loc[:, ~co2_emission.columns.isin(["Country Code", "Indicator Name", "Indicator Code"])]
    co2_emission = co2_emission.dropna(axis = 1, how = "all")
    # Replace NaN values with 0
    co2_emission = co2_emission.fillna(0)
    # Calling the function to remove all rows of 0 from the data frames
    co2_emission = remove_rows_with_zero(co2_emission)
    co2_emission_years = co2_emission.set_index("Country Name").T
    co2_emission_years = co2_emission_years.dropna(how = "all")
    
    return co2_emission, co2_emission_years


co2_emission, co2_emission_years = co2_data("co2_emission.csv")

# Statistical methods to explore data
co2_emission_summary = co2_emission_years.describe()
co2_emission_median = co2_emission_years.median()
co2_emission_var = co2_emission_years.var()


def population_data(population_total):
    # Read the World Bank data into a pandas dataframe and cleaning the data by manipulation methods
    population_total = pd.read_csv(
        "C:/Users/abigi/OneDrive/Desktop/Assignments/Applied data science 1/Applied data science 1 Assignment 2/Population total/population_total.csv", 
        skiprows = 4
    )
    population_total = population_total.loc[:, ~population_total.columns.isin(["Country Code", "Indicator Name", "Indicator Code"])]
    population_total = population_total.dropna(axis = 1, how = "all")
    # Replace NaN values with 0
    population_total = population_total.fillna(0)
    # Calling the function to remove all rows of 0 from the data frames
    population_total = remove_rows_with_zero(population_total)
    population_total_years = population_total.set_index("Country Name").T
    population_total_years = population_total_years.dropna(how = "all")
    
    # Selecting years from 1990 to 2021
    population_total_years = population_total_years.iloc[30:]
    
    return population_total, population_total_years


population_total, population_total_years = population_data("population_total.csv")
    
# Statistical methods to explore data
population_total_summary = population_total_years.describe()
population_total_median = population_total_years.median()
population_total_var = population_total_years.var()


# Creating a bar plot
# Select the countries and years of interest
selected_countries = ['China', 'India', 'United Arab Emirates', 'Brazil', 'Cuba', 'Spain', 'United Kingdom', 'Greece', 'Israel', 'Nigeria']
selected_years = ['1990', '2000', '2010', '2020']

# Extract the relevant data for Forest Area
forest_area_selected = forest_area_years.loc[selected_years, selected_countries]
co2_emission_selected = co2_emission_years.loc[selected_years, selected_countries]

# Transpose the data for plotting
forest_area_selected = forest_area_selected.T
co2_emission_selected = co2_emission_selected.T

# Plotting the bar chart
plt.figure(figsize=(12, 8))
forest_area_selected.plot(kind='bar', stacked=False, edgecolor='black', alpha=0.6)
plt.title('Forest Area In Percentage')
plt.xlabel('Countries')
plt.ylabel('% of Forest Area')
plt.legend(title='Year')
plt.show()


plt.figure(figsize=(12, 8))
co2_emission_selected.plot(kind='bar', stacked=False, edgecolor='black', alpha=1, color=['skyblue', 'salmon', 'lightgreen', 'lightpink'], logy=True)
plt.title('CO2 Emission for Selected Countries') 
plt.xlabel('Countries')
plt.ylabel('CO2 Emission')
plt.legend(title='Year')
plt.show()


# Creating line plots
selected_countries = ['China', 'India', 'United Arab Emirates', 'Brazil', 'Cuba', 'Spain', 'United Kingdom', 'Greece', 'Israel', 'Nigeria']
selected_years = ['1990', '1995', '2000', '2005', '2010', '2015', '2020']

# Extract the relevant data for Aerable Land
arable_land_selected = arable_land_years.loc[selected_years, selected_countries]

# Plotting the line chart
plt.figure(figsize=(12, 8))
arable_land_selected.plot(kind='line', marker='o', linestyle='--', linewidth=1.5, markersize=2)
plt.title('Arable Land')
plt.xlabel('Years')
plt.ylabel('% of Arable Land')
plt.legend(title='Countries', loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()

# Creating line plots for Population Total
population_total_selected = population_total_years.loc[selected_years, selected_countries]

# Plotting the line chart for Population Total
plt.figure(figsize=(12, 8))
population_total_selected.plot(kind='line', marker='o', linestyle='--', linewidth=1.5, markersize=2)
plt.title('Population Total for Selected Countries')
plt.xlabel('Years')
plt.ylabel('Total Population')
plt.legend(title='Countries', loc='center left', bbox_to_anchor=(1, 0.5))
plt.show()


# Heatmap creation
# Heatmap for spain
selected_country = 'Spain'

# Extract data for the selected country
forest_area_selected_country = forest_area_years[[selected_country]]
arable_land_selected_country = arable_land_years[[selected_country]]
co2_emission_selected_country = co2_emission_years[[selected_country]]
population_total_selected_country = population_total_years[[selected_country]]

# Concatenate all data frames into a single DataFrame
combined_df = pd.concat(
    [forest_area_selected_country, arable_land_selected_country, co2_emission_selected_country, population_total_selected_country],
    axis=1,
    keys=['Forest Area', 'Arable Land', 'CO2 Emission', 'Population Total'])

# Calculate the correlation matrix
correlation_matrix = combined_df.corr()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='magma', fmt=".2f", linewidths=.5)
plt.title(f'Correlation Heatmap: {selected_country}')
plt.xlabel('Indicator')
plt.ylabel('Indicator')
plt.show()


# Heatmap for Israel
selected_country = 'Israel'

# Extract data for the selected country
forest_area_selected_country = forest_area_years[[selected_country]]
arable_land_selected_country = arable_land_years[[selected_country]]
co2_emission_selected_country = co2_emission_years[[selected_country]]
population_total_selected_country = population_total_years[[selected_country]]

# Concatenate all data frames into a single DataFrame
combined_df = pd.concat(
    [forest_area_selected_country, arable_land_selected_country, co2_emission_selected_country, population_total_selected_country],
    axis=1,
    keys=['Forest Area', 'Arable Land', 'CO2 Emission', 'Population Total'])

# Calculate the correlation matrix
correlation_matrix = combined_df.corr()

# Create a heatmap for the correlation matrix
plt.figure(figsize=(12, 10))
sns.heatmap(correlation_matrix, annot=True, cmap='viridis', fmt=".2f", linewidths=.5)
plt.title(f'Correlation Heatmap: {selected_country}')
plt.xlabel('Indicator')
plt.ylabel('Indicator')
plt.show()





