# basics.py - Python基礎練習

# 1. 変数と型
name = "RIN"
age = 35
height = 1.75
is_engineer = True

print(f"名前: {name}")
print(f"年齢: {age}")
print(f"身長: {height}m")
print(f"エンジニア: {is_engineer}")

# 型を確認
print(f"\nnameの型: {type(name)}")
print(f"ageの型: {type(age)}")

# 2. リスト（配列）
skills = ["Java", "Spring Boot", "React", "jQuery"]
print(f"\nスキル: {skills}")
print(f"最初のスキル: {skills[0]}")
print(f"スキル数: {len(skills)}")

# スキルを追加
skills.append("Python")
print(f"Python追加後: {skills}")

# 3. 辞書（Dictionary）- JavaのMapみたいなもの
profile = {
    "name": "RIN",
    "country": "Vietnam",
    "city": "Tokyo",
    "job": "Full-stack Engineer"
}

print(f"\nプロフィール: {profile}")
print(f"出身: {profile['country']}")