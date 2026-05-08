import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:

    salaries = employee["salary"].drop_duplicates().sort_values(ascending=False)

    # Handle invalid N
    if N <= 0 or N > len(salaries):
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    nth_salary = salaries.iloc[N - 1]

    return pd.DataFrame({f"getNthHighestSalary({N})": [nth_salary]})