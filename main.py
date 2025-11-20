import pandas as pd
import os

# ================================
# 1. СОЗДАНИЕ ДАННЫХ + DATAFRAME
# ================================

# словарь с данными - Создаем ТАБЛИЦУ: 10 учеников × 5 предметов
data = {
    "Имя": ["Алексей", "Мария", "Иван", "Екатерина", "Дмитрий", "Анна", "Сергей", "Ольга", "Павел", "Наталья"],
    "Математика": [5, 4, 3, 5, 4, 5, 3, 4, 5, 4],
    "Русский язык": [4, 5, 4, 5, 3, 4, 5, 5, 4, 4],
    "Литература": [5, 5, 4, 4, 3, 5, 4, 5, 4, 5],
    "Физика": [4, 4, 3, 5, 5, 4, 3, 4, 5, 4],
    "Информатика": [5, 5, 4, 5, 4, 5, 4, 5, 5, 4],
}

# преобразуем словарь → DataFrame
df = pd.DataFrame(data)

# ================================
# 2. ПУТЬ ДЛЯ СОХРАНЕНИЯ CSV
# ================================

output_dir = r"C:\Users\Lenovo\Documents\GitHub\PandasDatasetAZ02csv\PandasDatasetAZ02"

# создаём папку, если её нет
os.makedirs(output_dir, exist_ok=True)

# ================================
# 3. РАСЧЁТ СТАТИСТИК
# ================================

# первые строки DataFrame
head_df = df.head()

# средние значения по предметам
mean_values = df.drop(columns=["Имя"]).mean()

# медианы по предметам
median_values = df.drop(columns=["Имя"]).median()

# квартиль 1 и квартиль 3 по математике
Q1_math = df["Математика"].quantile(0.25)
Q3_math = df["Математика"].quantile(0.75)
IQR_math = Q3_math - Q1_math

# стандартное отклонение по предметам
std_values = df.drop(columns=["Имя"]).std()

# ================================
# 4. ФОРМИРОВАНИЕ ТАБЛИЦЫ summary
# ================================

summary = pd.DataFrame({
    "mean": mean_values,
    "median": median_values,
    "std": std_values
})

# добавляем отдельные столбцы квартилей только для математики
summary["Q1_math"] = pd.NA
summary["Q3_math"] = pd.NA
summary["IQR_math"] = pd.NA

summary.loc["Математика", "Q1_math"] = Q1_math
summary.loc["Математика", "Q3_math"] = Q3_math
summary.loc["Математика", "IQR_math"] = IQR_math

summary.index.name = "Предмет"

# ================================
# 5. СОХРАНЕНИЕ ВСЕХ CSV-ФАЙЛОВ
# ================================

students_file = os.path.join(output_dir, "students_grades.csv")
summary_file = os.path.join(output_dir, "grades_summary.csv")
iqr_file = os.path.join(output_dir, "math_quartiles_and_iqr.csv")

df.to_csv(students_file, index=False, encoding="utf-8-sig")
summary.to_csv(summary_file, encoding="utf-8-sig")

# отдельная таблица только для квартилей математики
pd.DataFrame({
    "Q1_math": [Q1_math],
    "Q3_math": [Q3_math],
    "IQR_math": [IQR_math],
}).to_csv(iqr_file, index=False, encoding="utf-8-sig")

# ================================
# 6. КРАСИВЫЙ ВЫВОД В КОНСОЛЬ
# ================================

print("\n" + "="*60)
print("ПЕРВЫЕ СТРОКИ ТАБЛИЦЫ:")
print("="*60)
print(head_df)

print("\n" + "="*60)
print("СРЕДНИЕ ЗНАЧЕНИЯ:")
print("="*60)
print(mean_values)

print("\n" + "="*60)
print("МЕДИАНЫ:")
print("="*60)
print(median_values)

print("\n" + "="*60)
print("КВАРТИЛИ И IQR ПО МАТЕМАТИКЕ:")
print("="*60)
print(f"Q1  = {Q1_math}")
print(f"Q3  = {Q3_math}")
print(f"IQR = {IQR_math}")

print("\n" + "="*60)
print("СТАНДАРТНОЕ ОТКЛОНЕНИЕ:")
print("="*60)
print(std_values)

print("\n" + "="*60)
print("ВСЕ CSV-ФАЙЛЫ СОХРАНЕНЫ УСПЕШНО:")
print("="*60)
print(students_file)
print(summary_file)
print(iqr_file)
print("="*60 + "\n")
