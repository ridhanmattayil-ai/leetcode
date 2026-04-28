import pandas as pd
def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    
  return (employees.groupby(['emp_id', 'event_day']).agg(sum)
                   .reset_index(names = ['emp_id', 'day'])
                   .assign(total_time = lambda x: x.out_time - x.in_time)
                   .iloc[:,[1,0,4]])
    