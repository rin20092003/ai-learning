# day 2 variables.py
# This script demonstrates the use of variables in Python.

print("==== Day2 : Variables and Data types ====\n")  # Print a greeting message

#1 .基本的な型
name = "RIN"
age = 35
height = 1.75
is_engineer = True
monthly_salary = 46 # in 万円

print("基本情報：")
print(f"名前: {name} (型: {type(name).__name__})")
print(f"年齢: {age} (型: {type(age).__name__})")
print(f"身長: {height} (型: {type(height).__name__})")
print(f"エンジニア: {is_engineer} (型: {type(is_engineer).__name__})")
print(f"月収: {monthly_salary} (型: {type(monthly_salary).__name__})")


#2.型変換
age_str = str(age)
salary_float = float(monthly_salary)
print(f"文字列に変換：'{age_str}' (型: {type(age_str).__name__})")
print(f"浮動小数点数に変換：{salary_float} (型: {type(salary_float).__name__})")

#3. 計算
annual_salary = monthly_salary * 12
target_salary = 83 #　月収目標
target_annual = target_salary * 12
increase = target_annual - annual_salary

print("年収計算：")
print(f"現在の年収: {annual_salary} 万円")
print(f"目標年収: {target_annual} 万円")
print(f"必要な増加額 : {increase} 万円")
print(f"増加率: {increase / annual_salary * 100:.1f}%\n")

#4.文字列操作
greeting = f"Hello AI Engineer！"
print("文字列操作：")
print(f"元の文字列: {greeting}")
print(f"大文字: {greeting.upper()}")
print(f"小文字: {greeting.lower()}")
print(f"文字数: {len(greeting)}")
print(f"分割: {greeting.split()}\n")





