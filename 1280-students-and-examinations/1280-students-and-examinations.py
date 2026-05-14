import pandas as pd

def students_and_examinations(
    students: pd.DataFrame,
    subjects: pd.DataFrame,
    examinations: pd.DataFrame
) -> pd.DataFrame:

    # Create all student-subject combinations
    df = students.merge(subjects, how='cross')

    # Count exams attended
    attended = (
        examinations.groupby(['student_id', 'subject_name'])
        .size()
        .reset_index(name='attended_exams')
    )

    # Merge counts with all combinations
    result = df.merge(
        attended,
        on=['student_id', 'subject_name'],
        how='left'
    )

    # Fill missing values with 0
    result['attended_exams'] = result['attended_exams'].fillna(0).astype(int)

    # Sort output
    result = result.sort_values(
        by=['student_id', 'subject_name']
    )

    return result

    df = pd.concat([df1, df2])

    result = (
        df.groupby('id')
          .size()
          .reset_index(name='num')
          .sort_values(by='num', ascending=False)
          .head(1)
    )

    return result