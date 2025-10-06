#day2_dictionaries.py

print("==== Day2 : Dictionaries ====\n")  # Print a greeting message

#1. 辞書の作成
profile = {
    "name": "RIN",
    "age": 35,
    "city": "Tokyo",
    "job": "Full-Stack Engineer",
    "experience_years": 10,
    "current_salary": 550  # 万円/年
}


print("プロファイル：")
for key, value in profile.items():
    print(f"{key}: {value}")    
print()

#2. 要素へのアクセス
print("要素へのアクセス:")
print(f"名前: {profile['name']}")
print(f"年齢: {profile.get('age')}")
print(f"職業: {profile.get('job')}\n")


#3. 辞書の追加・変更
profile["target_salary"] = 1000  # in 万円
profile["learning"] = "AI/LLM"
profile["current_salary"] = 600  # Update current salary

print("更新後のプロファイル：")
print(f"目標年収: {profile['target_salary']} 万円")
print(f"学習中の分野: {profile['learning']}")
print(f"現在の年収: {profile['current_salary']} 万円\n")

#4. キーの存在確認
if "target_salary" in profile:
    print("目標年収は設定されています。\n")

if "hobby" not in profile:
    print("Hobbyキーは未設定です。\n")

#5. 実用例：技術スタック
tech_stack = {
    "languages": ["Java", "Python", "C#", "PHP", "Ruby", "Go"],
    "frontend": ["React", "Next.js", "jQuery"],
    "backend": ["Spring Boot", "FastAPI"],
    "databases": ["PostgreSQL", "MySQL"],
    "cloud": ["AWS"],
    "learning": ["OpenAI API", "LangChain", "RAG"]
}


print("技術スタック：")
for category, skills in tech_stack.items():
    print(f"\n{category.upper()}:")
    for skill in skills:
        print(f" - {skill}")
print()

#6. ネストした辞書（辞書の中に辞書 ）
carreer_timeline = {
    "current": {
        "company": "Current Company",
        "position": "Full-stack Engineer",
        "salary": 550,
        "satisfaction": "Low"
    },
    "target": {
        "position": "AI Engineer",
        "salary": 1000,
        "timeline": "12 months",
        "satisfaction": "High"
    }
}

print("キャリアタイムライン：")
print("\n現在の状況:")
for key, value in carreer_timeline["current"].items():
    print(f"{key}: {value}")    


print("\n目標の状況（１２ヶ月後）:")
for key, value in carreer_timeline["target"].items():
    print(f"{key}: {value}")
print()



#7. 実用的な関数：辞書を使った計算
def calculate_carreer_gap(current, target):
    """キャリアギャップを計算する関数"""
    salary_gap = target["salary"] - current["salary"]
    increase_rate = (salary_gap / current["salary"]) * 100

    return{
        "salary_increase": salary_gap,
        "increase_rate": round(increase_rate , 1),
        "months_to_achieve": target["timeline"]
    }

result = calculate_carreer_gap(carreer_timeline["current"], carreer_timeline["target"])
print("キャリアギャップ分析:")
print(f"  年収増加額: + {result['salary_increase']} 万円")
print(f"  増加率: {result['increase_rate']}%")
print(f"  達成期限:  {result['months_to_achieve']}\n")



