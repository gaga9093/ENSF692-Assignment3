# school_data.py
# @Author Alireza Ghasemi
# A terminal-based application for computing and printing statistics based on given input.
# I acknowlege use of chatgpt to write, debug,learn my code. I did my best to learn what I am provideing as code here.
# I added two arrays to the given_data class for school name and school code to be exactly the same as the samople output procided.


import numpy as np
# Importing data from given_data.
from given_data import (
    year_2013, year_2014, year_2015, year_2016, year_2017,
    year_2018, year_2019, year_2020, year_2021, year_2022,
    school_codes, school_names
)

# Combine data from all years into a 3D array
# Reshaping the data structure into 3D to reflect 10 years of data, 20 schools, and 3 grades.
dataset = np.array([
    year_2013, year_2014, year_2015, year_2016, year_2017,
    year_2018, year_2019, year_2020, year_2021, year_2022
]).reshape((10, 20, 3))

# Defining a function to provide information about a selected school by the user following a prompt.
def get_school_statistics(school_index):
    """
    Compute statistics for a specific school.

    Args:
        school_index (int): The index of the school (0 to 19).

    Returns:
        dict: A dictionary with school-specific statistics.
    """
    grades = dataset[:, school_index, :]
    total_enrollment_per_year = np.nansum(grades, axis=1)
    stats = {
        'mean_enrollment': np.nanmean(grades, axis=0).astype(int),
        'highest_enrollment': np.nanmax(grades),
        'lowest_enrollment': np.nanmin(grades),
        'total_enrollment_per_year': total_enrollment_per_year.astype(int),
        'total_ten_year_enrollment': np.nansum(grades).astype(int),
        'mean_total_yearly_enrollment': np.nanmean(total_enrollment_per_year).astype(int),
        'enrollments_over_500': grades[grades > 500]
    }
    return stats
# Providing general statistics about all grades in schools.
def get_general_statistics():
    """
    Compute general statistics for all schools combined.

    Returns:
        dict: A dictionary with general statistics.
    """
    all_grades = dataset.reshape(-1, 3)
    total_enrollment_per_year = np.nansum(dataset, axis=(1, 2))
    stats = {
        'mean_enrollment_2013': np.nanmean(dataset[0]).astype(int),
        'mean_enrollment_2022': np.nanmean(dataset[-1]).astype(int),
        'total_graduating_class_2022': np.nansum(dataset[-1][:, 2]).astype(int),
        'highest_enrollment': np.nanmax(dataset),
        'lowest_enrollment': np.nanmin(dataset)
    }
    return stats
# Defining the main function including the executing code lines including user prompt.
def main():
    print("ENSF 692 School Enrollment Statistics")

    # Print Stage 1 requirements here
    print("\n***Stage 1: Print Data Shape and Dimensions***\n")
    print(f"Shape of full data array: {dataset.shape}")
    print(f"Dimensions of full data array: {dataset.ndim}")

    # Prompt for user input
    try:
        user_input = input("Please enter the high school name or school code: ").strip()
        if user_input.isdigit():
            school_index = np.where(school_codes == int(user_input))[0][0]
        else:
            school_index = np.where(school_names == user_input)[0][0]
    except IndexError:
        print("You must enter a valid school name or code.")
        return

    # Print Stage 2 requirements here
    print("\n***Requested School Statistics***\n")
    school_stats = get_school_statistics(school_index)
    print(f"School Name: {school_names[school_index]}, School Code: {school_codes[school_index]}")
    print(f"Mean enrollment for Grade 10: {school_stats['mean_enrollment'][0]}")
    print(f"Mean enrollment for Grade 11: {school_stats['mean_enrollment'][1]}")
    print(f"Mean enrollment for Grade 12: {school_stats['mean_enrollment'][2]}")
    print(f"Highest enrollment for a single grade: {school_stats['highest_enrollment']}")
    print(f"Lowest enrollment for a single grade: {school_stats['lowest_enrollment']}")
    print(f"Total enrollment for 2013: {school_stats['total_enrollment_per_year'][0]}")
    print(f"Total enrollment for 2014: {school_stats['total_enrollment_per_year'][1]}")
    print(f"Total enrollment for 2015: {school_stats['total_enrollment_per_year'][2]}")
    print(f"Total enrollment for 2016: {school_stats['total_enrollment_per_year'][3]}")
    print(f"Total enrollment for 2017: {school_stats['total_enrollment_per_year'][4]}")
    print(f"Total enrollment for 2018: {school_stats['total_enrollment_per_year'][5]}")
    print(f"Total enrollment for 2019: {school_stats['total_enrollment_per_year'][6]}")
    print(f"Total enrollment for 2020: {school_stats['total_enrollment_per_year'][7]}")
    print(f"Total enrollment for 2021: {school_stats['total_enrollment_per_year'][8]}")
    print(f"Total enrollment for 2022: {school_stats['total_enrollment_per_year'][9]}")
    print(f"Total ten year enrollment: {school_stats['total_ten_year_enrollment']}")
    print(f"Mean total enrollment over 10 years: {school_stats['mean_total_yearly_enrollment']}")
    if len(school_stats['enrollments_over_500']) == 0:
        print("No enrollments over 500.")
    else:
        print(f"For all enrollments over 500, the median value was: {int(np.median(school_stats['enrollments_over_500']))}")

    # Print Stage 3 requirements here
    print("\n***General Statistics for All Schools***\n")
    general_stats = get_general_statistics()
    print(f"Mean enrollment in 2013: {general_stats['mean_enrollment_2013']}")
    print(f"Mean enrollment in 2022: {general_stats['mean_enrollment_2022']}")
    print(f"Total graduating class of 2022 across all schools: {general_stats['total_graduating_class_2022']}")
    print(f"Highest enrollment for a single grade within the entire time period: {general_stats['highest_enrollment']}")
    print(f"Lowest enrollment for a single grade within the entire time period: {general_stats['lowest_enrollment']}")
#To run the program
if __name__ == '__main__':
    main()

