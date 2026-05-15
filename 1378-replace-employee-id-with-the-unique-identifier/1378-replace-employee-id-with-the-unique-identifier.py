import pandas as pd

def replace_employee_id(employees: pd.DataFrame,
                        employee_uni: pd.DataFrame) -> pd.DataFrame:

    df = pd.merge(employee_uni, employees,
                  how='right',
                  on='id')

    return df[['unique_id', 'name']]
    