#!/usr/bin/env python
# coding: utf-8

# # Analysis of Freshman English Composition Grade Distributions
# 
# ## Introduction
# 
# Southern Wesleyan University (SWU) is committed to maximizing students' learning, course completions, persistence at SWU, and ultimately their completion of a degree. SWU writing foundation courses in English, Freshman Composition I and Freshman Composition II (plus associated labs), equip students with proficiencies in writing, critical thinking, analysis, and communication necessary for students' future success throughout the whole of their degrees.
# 
# Regular analysis of grade distributions in foundation courses such as the Freshman Composition sequence is an important component of supporting faculty collaboration and development. In turn, SWU faculty can expect higher student achievement in their individual courses and throughout students' whole degree.
# 
# ## Data Set
# 
# Per my request on March 11, 2020, the Assistant Director of Institutional Research and Reporting extracted final grade data from all "ENGL"-prefix courses, including completed Freshman Composition I, Freshman Composition II, and associated labs/workshops (hereafter referred to as "composition courses"). The data set includes composisition courses spanning from Spring 2018 to Spring 2020 (online "A" term only since other terms were not complete at the time).
# 
# The Assistant Director of Institutional Research and Reporting completed pivot table analyses for the data. In addition to the observable findings there as one clicks through filters and examines patterns, this analysis of the raw data brings in narrative as the findings are unpacked step by step. The raw data was drawn from the "ENGL Grade Dist_xxxx" attachment within the 2020-03-11 email from xxxx@swu.edu to rbjohnson@swu.edu. I copied the raw data tab to a new file and then saved in comma-separated format (CSV) in a new file, "englS18S20", which is the basis for the present analysis.
# 
# The below document contains Python 3 code supported by comments prefaced by '#" signs to explain the analysis process. Interspersed with the code are longer narrative text sections such as this title and introductory section.
# 
# ### Import Data

# In[1]:


# Import the "pandas" Python package to facilitate analysis.
import pandas as pd

# Open the specific file containing the data set and save to a pandas data frame.
engl1820 = pd.read_csv("englS18S20.csv")

# Display the first five rows of data to inspect the data visually.
print(engl1820.head())


# In[2]:


# Calculate the dimensions of the data set to verify that the import was successful.
engl1820_dimensions = engl1820.shape
print(engl1820_dimensions)

# Inspect the data types within the columns of data set as it was imported into the present data frame.
columns_types = engl1820.dtypes
print(columns_types)


# ### Verfication of Data Set
# 
# The "(1947, 26)" annotation above shows that the data frame is 1,947 rows by 26 columns. These dimensions match the raw data dimensions as measured when opened in Excel and all rows/columns are selected and inspected. During the import process the pandas package automatically recognized integer, "int64", data types for the following columns: Student ID, Year, Enrolled, Credit_Hours, and lead_instructr_id. All other columns were imported as objects, which are appropriate for handling strings. The imported data appears to match the original set exactly.
# 
# ## Analysis of Overall Grade Distributions
# 
# This first analysis will include all instructors who have taught composition courses, including full-time and affiliate professors. The data set includes all SWU courses with the "ENGL" course prefix, many more courses than the composition courses under review at present.
# 
# We'll first filter out any non-composition courses and then calculate grade distributions solely for composition courses. (Non-composition courses may be reviewed later on as a comparison data set to the composition courses.)

# In[3]:


# Filter out only composition courses from the complete ENGL course data set and save as a new data frame, comp_courses.
comp_courses = engl1820[engl1820["Course Title"].isin(["Freshman Composition I", "Freshman Composition II", "Freshman Composition I Lab", "English Foundations Workshop"])]

# Inspect the number of rows and columns of the comp_courses data frame.
print(comp_courses.shape)
print('The number of composition courses equals', comp_courses.shape[0], 'courses.')
print('Composition courses represent', (comp_courses.shape[0]/engl1820.shape[0])*100, 'percent of all ENGL courses.')


# Next, we'll examine the overall grade distributions for each of the two courses and two labs that are part of the composition course sequence. This distribution includes distributions for all instructors, plus separate distributions separating full-time and affiliate faculty.
# 
# ### Overall Grade Distribution by All Faculty

# In[4]:


# Create a list of unique grades assigned in the data set.
grades_assigned = comp_courses["Grade"].unique()
print(grades_assigned)


# In[5]:


# Create a dictionary of unique grades assigned along with the number of times each grade was assigned.
all_grades_count = {}

for grade in grades_assigned:
    selected_rows = comp_courses[comp_courses["Grade"] == grade]
    all_grades_count[grade] = selected_rows.shape[0]

# Create a sorted list from the dictionary.
all_grades_sorted = pd.Series(all_grades_count)
print(all_grades_sorted.sort_index())


# As we can see from the above frequency table, pure grade letters (A, B, C, D, F) are more common than their associated modified grade letters (e.g., B+ and B-, associated with the pure grade letter, B). So, students seem to tend to land in the middle of each grade letter tier (or professors assign grades mostly in the middle of the tier and use modified letters in more exceptional circumstances).
# 
# Below is a grade distribution (in percentages) sorted from the most common grades to the least common.

# In[6]:


comp_courses["Grade"].value_counts(normalize=True).sort_values(ascending=False)


# The above grade distribution shows that the grades of A, B, and F account for over 50% of all grades. F grades alone account for a little over 12% of all grades. Of further concern are the number of W grades at just over 4%, about equal in frequency to B- (4.1%) and nearing in frequency to A- (6.1%).
# 
# Aside from the expected small occurences of I (incomplete) and NR (not reported) grades, the least common grades are C- and D+ (1.3% and 1.4%, respectively). This is interesting (and somewhat concerning) because students must earn at least a C- to successfully pass the General Education requirement for ENGL. The much higher occurrence of C and F grades suggests the presence of a) an "all or nothing" grading bias by professors, or b) "all or nothing" performance by students who either decide to succeed in the course or not.

# ## Grade Distributions of Each Faculty Member
# 
# (sample only for confidentiality)
# 
# . . .

# Respectfully Submitted,
# 
# Dr. Randolph Johnson
# Dean, College of Arts and Sciences
# Southern Wesleyan University
