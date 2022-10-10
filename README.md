# Data Science Project

## Introduccion

I am part of the course of Samsung Innovation, and this is the final work to the section in programming. I have been in this moment like 2 months learning about python, with a experience level of 0. We learn about all the basics in Python, and on python, Numpy, Pandas, Matplotlib and Seaborn. In this project we use everything to show our knowledge.

## Objectives

Make an automatization tha let us extract and interpret the data from files names: 'Student-mat.csv' and 'Student-por.csv'. 

## Activities

1. [X] Obtain the date that the script is executed
2. [X] Create a dataframe for each school with the columns: school, sex, age, address, Pstatus,
    guardian, traveltime, studytime, failures, paid, internet, health, absences,
    G1,G2,G3
3. [X] Verify that the dataframe dont have null value, if they have the row is delete.
4. [X] Make a pie chart that show the percentajes of female and male.
5. [X] Make a bar chart that show the number of students that have the same age
6. [X] Show the mean of ages for each course in each school
7. [X] Show the mean of grades for each period in each school
8. [X] Find the max number of absences and use it like the total number of class, and find the percentaje of assistance for each student.
9. [X] With the result of the activity below, create a new column named 'Extra'
1. [X] Create a new column named 'Approved' in which if the student approve you assign an 1 else 0.

* If the student have less than 80% in assistance, have 0
* if the student have more than 80% in assistance, but have less than 10 in G3, have 0
* If the student have more than 80%, and the grade in G3 is between 10 and 15, have 1 in 'extra' and 'approved'
* if the student have more than 80% and the grade is bigger than 15, have 1 in 'approved' and 0 in 'extra'
