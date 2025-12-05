 import pandas as pd

# Загрузка данных
df = pd.read_csv('tested.csv')

# 1. Основная информация
print("Пропущенные значения:")
print(df.isnull().sum(), "\n")

print("Типы данных:")
print(df.dtypes, "\n")

# 2. Вывод первых n строк
n = input("Сколько строк вывести? ")
print(df.head(int(n)), "\n")

# 3. Статистика по возрасту
print("Статистика по возрасту:")
print(df['Age'].describe(), "\n")

# 4. Количество строк и столбцов
print(f"Строк: {df.shape[0]}, Столбцов: {df.shape[1]}\n")

# 5. Заполнение пропусков в возрасте
df['Age'] = df['Age'].fillna(df['Age'].median())
print("Возраст после заполнения пропусков:")
print(df['Age'].head(), "\n")

# 6. Выживаемость по полу
male_survived = df[df['Sex'] == 'male']['Survived'].mean() * 100
female_survived = df[df['Sex'] == 'female']['Survived'].mean() * 100
print(f"Выжили: мужчины {male_survived:.1f}%, женщины {female_survived:.1f}%\n")

# 7. Средний возраст по полу
male_age = df[df['Sex'] == 'male']['Age'].mean()
female_age = df[df['Sex'] == 'female']['Age'].mean()
print(f"Средний возраст: мужчины {male_age:.1f}, женщины {female_age:.1f}\n")

# 8. Возраст выживших и погибших
male_survived_age = df[(df['Sex'] == 'male') & (df['Survived'] == 1)]['Age'].mean()
male_dead_age = df[(df['Sex'] == 'male') & (df['Survived'] == 0)]['Age'].mean()
female_survived_age = df[(df['Sex'] == 'female') & (df['Survived'] == 1)]['Age'].mean()
female_dead_age = df[(df['Sex'] == 'female') & (df['Survived'] == 0)]['Age'].mean()

print("Средний возраст:")
print(f"Мужчины: выжили {male_survived_age:.1f}, погибли {male_dead_age:.1f}")
print(f"Женщины: выжили {female_survived_age:.1f}, погибли {female_dead_age:.1f}\n")

# 9. Фильтры
filter_a = df[(df['Age'] > 30) & (df['Sex'] == 'male') & (df['Pclass'] == 1)]
filter_b = df[((df['Age'] < 18) | (df['Sex'] == 'female')) & (df['Survived'] == 1)]

print("Фильтр A (мужчины >30, 1 класс):")
print(f"Найдено: {len(filter_a)} человек\n")

print("Фильтр B (выжившие <18 или женщины):")
print(f"Найдено: {len(filter_b)} человек\n")

# 10. Сводная таблица
pivot = df.groupby(['Pclass', 'Sex']).agg({
    'Age': 'mean',
    'Survived': 'mean',
    'Fare': 'mean'
}).round(2)

pivot['Count'] = df.groupby(['Pclass', 'Sex']).size()
pivot['Survived_%'] = (pivot['Survived'] * 100).round(1)

print("Сводная таблица:")
print(pivot)