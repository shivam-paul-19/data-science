import pandas as pd

# Q1
def createDataframe(student_data: list[list[int]]) -> pd.DataFrame:
    dic = {
        "student_id": [x[0] for x in student_data],
        "age": [x[1] for x in student_data]
    }

    df = pd.DataFrame(dic)
    return df

# Q2
def getDataframeSize(players: pd.DataFrame) -> list[int]:
    return list(players.shape)

# Q3
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    return employees.head(3)

# Q4
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    res_dt = students.loc[(students['student_id'] == 101)]
    return res_dt[['name', 'age']]

# Q5
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = [x*2 for x in list(employees['salary'])]
    return employees

# Q6
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates(subset='email')

# Q7
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset='name')

# Q8
def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['salary'] = [x*2 for x in employees['salary']]
    return employees

# Q9
def renameColumns(students: pd.DataFrame) -> pd.DataFrame:
    students.rename(columns={'id': 'student_id', 'first': 'first_name', 'last': 'last_name', 'age': 'age_in_years'}, inplace=True)
    return students

# Q10
def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    students['grade'] = students['grade'].astype(int)
    return students

# Q11
def fillMissingValues(products: pd.DataFrame) -> pd.DataFrame:
    products['quantity'] = products['quantity'].fillna(0)
    return products

# Q12
def concatenateTables(df1: pd.DataFrame, df2: pd.DataFrame) -> pd.DataFrame:
    df = pd.concat([df1, df2])
    return df

# Q13
def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    df_pivot = weather.pivot_table(values='temperature', index='month', columns='city')
    return df_pivot

# Q14
def meltTable(report: pd.DataFrame) -> pd.DataFrame:
    df_melted = report.melt(id_vars='product', value_vars=['quarter_1', 'quarter_2', 'quarter_3', 'quarter_4'], var_name='quarter', value_name='sales')
    return df_melted

# Q15
def findHeavyAnimals(animals: pd.DataFrame) -> pd.DataFrame:
    name_dt = animals.loc[(animals['weight'] > 100)][['name', 'weight']].sort_values(ascending=False, by='weight')
    return pd.DataFrame(name_dt['name'])