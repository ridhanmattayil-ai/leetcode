import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    # Merge employee and department tables
    df = employee.merge(department, left_on='departmentId', right_on='id')

    # Find highest salary in each department
    max_salary = df.groupby('name_y')['salary'].transform('max')

    # Filter employees with highest salary
    result = df[df['salary'] == max_salary]

    # Select required columns
    result = result[['name_y', 'name_x', 'salary']]

    # Rename columns
    result.columns = ['Department', 'Employee', 'Salary']

    return result