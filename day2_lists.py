print("=== day 2: List ===\n")

# 1. リストの作成
current_skills = ["java", "spring boot", "react", "jquery"]

print(f"Current Skills: {current_skills}\n")

#2. 要素へのアクセス
print("要素へのアクセス:")
print(f"最初のスキル: {current_skills[0]}")
print(f"最後のスキル: {current_skills[-1]}\n")
print(f"2番目と三番目: {current_skills[1:3]}\n")
print(f"3番目と2番目: {current_skills[-2:-4:-1]}\n")  # start: stop: step

#3. リストの操作
print("リストの操作:")

# 要素の追加
current_skills.append("python")
print(f"Python追加後: {current_skills}")

current_skills.insert(2, "PostgreSQL")

print(f"PostgreSQLを2番目に追加後: {current_skills}")


# 要素の削除
current_skills.remove("jquery")
print(f"JQuery削除後: {current_skills}")

#長さ
print(f"スキル数: {len(current_skills)}")


#4. ループ処理
print("全スキルを表示:")
for i, skill in enumerate(current_skills, 1):
    print(f"{i}.{skill}")
print()


#5.学習予定のAIスキル
ai_skills = [
    "Python", 
    "OpenAI API",
    "LangChain",
    "RAG",
    "FastAPI",
    "Vector Databases"
]

print("１２か月で学ぶAIスキル:")

for month, skill in enumerate(ai_skills, 1):
    print(f"Month {month}.{skill}")
print()



#6. リスト内包表記(Pythonらしい書き方 )
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(f"元のリスト: {numbers}")
print(f"各要素を2倍にしたリスト: {doubled}\n")

#実用例：月収リスト
monthly_salaries = [46, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]  # in 万円
print("月収シミュレーション（転職後）：")
for month, salary in enumerate(monthly_salaries, 1):
    annual = salary * 12
    print(f"　{month}年後: 月 {salary} 万円 →　年収 {annual} 万円")
print()

