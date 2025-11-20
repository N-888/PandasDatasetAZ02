import pandas as pd # импорт библиотеки pandas для работы с таблицами
import os # импорт модуля os для работы с файловой системой

# ================================
# 1. СОЗДАНИЕ ДАННЫХ + DATAFRAME
# ================================

# СЛОВАРЬ ДАННЫХ - СОЗДАЕМ ТАБЛИЦУ: 10 учеников × 5 предметов
# ОЦЕНКИ В ДИАПАЗОНЕ 3 - 5 баллов
data = {
    "Имя": ["Алексей", "Мария", "Иван", "Екатерина", "Дмитрий", "Анна", "Сергей", "Ольга", "Павел", "Наталья"],
    "Математика": [5, 4, 3, 5, 4, 5, 3, 4, 5, 4],   # 10 оценок
    "Русский язык": [4, 5, 4, 5, 3, 4, 5, 5, 4, 4], # 10 оценок
    "Литература": [5, 5, 4, 4, 3, 5, 4, 5, 4, 5],   # 10 оценок
    "Физика": [4, 4, 3, 5, 5, 4, 3, 4, 5, 4],       # 10 оценок
    "Информатика": [5, 5, 4, 5, 4, 5, 4, 5, 5, 4],  # 10 оценок
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

# ПЕРВЫЕ 5 строк DataFrame - БЫСТРО ПРОВЕРИТЬ исходные данные
head_df = df.head()

# Средние (mean) значения по предметам (исключаем столбец Имя)
mean_values = df.drop(columns=["Имя"]).mean()

# Медианы по предметам
median_values = df.drop(columns=["Имя"]).median()

# Квартиль 1 и квартиль 3 по Математике
Q1_math = df["Математика"].quantile(0.25)
Q3_math = df["Математика"].quantile(0.75)
IQR_math = Q3_math - Q1_math   # межквартильный размах

# Стандартное отклонение по предметам
std_values = df.drop(columns=["Имя"]).std()

# ================================
# 4. ФОРМИРОВАНИЕ / СБОРКА ТАБЛИЦЫ summary
# ================================

summary = pd.DataFrame({
    "mean": mean_values,
    "median": median_values,
    "std": std_values
})

# Добавляем отдельные Столбцы Квартилей и IQR
# - только для Математики, остальным ставим NaN
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

# Сохраняем исходную таблицу учеников
df.to_csv(students_file, index=False, encoding="utf-8-sig")

# Сохраняем summary (сводные метрики)
summary.to_csv(summary_file, encoding="utf-8-sig")

# Отдельная таблица только для Квартилей и IQR Математики
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
print("ТАБЛИЦА УСПЕВАЕМОСТИ ВСЕХ 10 УЧЕНИКОВ по 5 ПРЕДМЕТАМ:")
print("="*60)
print(df)

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
