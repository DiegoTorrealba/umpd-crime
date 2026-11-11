import pandas as pd


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
SEMESTER_LABELS = ['Winter 2018', 'Spring 2018', 'Summer 2018', 'Fall 2018', 'Winter 2019', 'Spring 2019', 'Summer 2019', 'Fall 2019', 'Winter 2020', 'Spring 2020', 'Summer 2020', 'Fall 2020', 'Winter 2021', 'Spring 2021', 'Summer 2021', 'Fall 2021', 'Winter 2022', 'Spring 2022', 'Summer 2022', 'Fall 2022', 'Winter 2023', 'Spring 2023', 'Summer 2023', 'Fall 2023', 'Winter 2024', 'Spring 2024', 'Summer 2024', 'Fall 2024', 'Winter 2025', 'Spring 2025', 'Summer 2025', 'Fall 2025', 'Winter 2026', 'Spring 2026', 'Summer 2026', 'Fall 2026']
# Semester start and end dates
SEMESTER_RANGES = {
  # 2017-2018
  'W_2018' : {'start_date': pd.to_datetime('2018-01-02'), 'end_date': pd.to_datetime('2018-01-22')},
  'SP_2018' : {'start_date': pd.to_datetime('2018-01-24'), 'end_date': pd.to_datetime('2018-05-18')},
  'SU_2018' : {'start_date': pd.to_datetime('2018-05-29'), 'end_date': pd.to_datetime('2018-08-17')},
  
  # 2018-2019
  'F_2018' : {'start_date': pd.to_datetime('2018-08-27'), 'end_date': pd.to_datetime('2018-12-18')},
  'W_2019' : {'start_date': pd.to_datetime('2019-01-02'), 'end_date': pd.to_datetime('2019-01-22')},
  'SP_2019' : {'start_date': pd.to_datetime('2019-01-28'), 'end_date': pd.to_datetime('2019-05-22')},
  'SU_2019' : {'start_date': pd.to_datetime('2019-05-28'), 'end_date': pd.to_datetime('2019-08-16')},
  
  # 2019-2020
  'F_2019' : {'start_date': pd.to_datetime('2019-08-26'), 'end_date': pd.to_datetime('2019-12-17')},
  'W_2020' : {'start_date': pd.to_datetime('2020-01-02'), 'end_date': pd.to_datetime('2020-01-22')},
  'SP_2020' : {'start_date': pd.to_datetime('2020-01-27'), 'end_date': pd.to_datetime('2020-05-20')},
  'SU_2020' : {'start_date': pd.to_datetime('2020-06-01'), 'end_date': pd.to_datetime('2020-08-21')},
  
  # 2020-2021
  'F_2020' : {'start_date': pd.to_datetime('2020-08-31'), 'end_date': pd.to_datetime('2020-12-22')},
  'W_2021' : {'start_date': pd.to_datetime('2021-01-04'), 'end_date': pd.to_datetime('2021-01-22')},
  'SP_2021' : {'start_date': pd.to_datetime('2021-01-25'), 'end_date': pd.to_datetime('2021-05-19')},
  'SU_2021' : {'start_date': pd.to_datetime('2021-06-01'), 'end_date': pd.to_datetime('2021-08-20')},
  
  # 2021-2022
  'F_2021' : {'start_date': pd.to_datetime('2021-08-30'), 'end_date': pd.to_datetime('2021-12-21')},
  'W_2022' : {'start_date': pd.to_datetime('2022-01-03'), 'end_date': pd.to_datetime('2022-01-21')},
  'SP_2022' : {'start_date': pd.to_datetime('2022-01-24'), 'end_date': pd.to_datetime('2022-05-18')},
  'SU_2022' : {'start_date': pd.to_datetime('2022-05-31'), 'end_date': pd.to_datetime('2022-08-19')},
  
  # 2022-2023
  'F_2022' : {'start_date': pd.to_datetime('2022-08-29'), 'end_date': pd.to_datetime('2022-12-20')},
  'W_2023' : {'start_date': pd.to_datetime('2023-01-03'), 'end_date': pd.to_datetime('2023-01-23')},
  'SP_2023' : {'start_date': pd.to_datetime('2023-01-25'), 'end_date': pd.to_datetime('2023-05-19')},
  'SU_2023' : {'start_date': pd.to_datetime('2023-05-30'), 'end_date': pd.to_datetime('2023-08-18')},
  
  # 2023-2024
  'F_2023' : {'start_date': pd.to_datetime('2023-08-28'), 'end_date': pd.to_datetime('2023-12-19')},
  'W_2024' : {'start_date': pd.to_datetime('2024-01-02'), 'end_date': pd.to_datetime('2024-01-22')},
  'SP_2024' : {'start_date': pd.to_datetime('2024-01-24'), 'end_date': pd.to_datetime('2024-05-17')},
  'SU_2024' : {'start_date': pd.to_datetime('2024-05-28'), 'end_date': pd.to_datetime('2024-08-16')},
  
  # 2024-2025
  'F_2024' : {'start_date': pd.to_datetime('2024-08-26'), 'end_date': pd.to_datetime('2024-12-17')},
  'W_2025' : {'start_date': pd.to_datetime('2025-01-02'), 'end_date': pd.to_datetime('2025-01-22')},
  'SP_2025' : {'start_date': pd.to_datetime('2025-01-27'), 'end_date': pd.to_datetime('2025-05-21')},
  'SU_2025' : {'start_date': pd.to_datetime('2025-06-02'), 'end_date': pd.to_datetime('2025-08-22')},
  
  # 2025-2026
  'F_2025' : {'start_date': pd.to_datetime('2025-09-02'), 'end_date': pd.to_datetime('2025-12-20')},
  'W_2026' : {'start_date': pd.to_datetime('2026-01-05'), 'end_date': pd.to_datetime('2026-01-23')},
  'SP_2026' : {'start_date': pd.to_datetime('2026-01-26'), 'end_date': pd.to_datetime('2026-05-18')},
  'SU_2026' : {'start_date': pd.to_datetime('2026-06-01'), 'end_date': pd.to_datetime('2026-08-21')},
  
  # 2026-now
  'F_2026': {'start_date': pd.to_datetime('2026-08-31'), 'end_date': pd.Timestamp.today().normalize()}
}
# for time of day categorization
## 0 = 12 am; 23:59 - 11:59 pm
TOD_CATEGORIES = {
  'bins' : [0, 5, 11, 17, 23, 24],
  'labels' : ['night', 'morning', 'afternoon', 'evening', 'night']
}