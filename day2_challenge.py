#day2_challenge.py

print("==== Day2 : Challenge - Learning Tracker ====\n")  # Print a greeting message

# 自分の専用の学習トラッカーを作成する
# TODO 1:自分のプロフィールを辞書で作成する
my_profile = {
    "name": "Rin",
    "age": 35,
    "city": "Tokyo",
    "job": "AI Engineer",
    "experience_years":10
}   

# TODO 2:学習中のスキルをリストで作成する
skills_to_learn = [
    "Python",
    "OpenAI API",
    "LangChain",
    "RAG",
    "FastAPI",
    "Vector Databases"
]

# TODO 3:学習中のスキルを月ごとに辞書で管理する
learning_plan = {
    "month_1": {"skills": ["Python", "OpenAI API"],
                "hours": 30   # 30 hours planned
            },
    "month_2": {"skills": ["LangChain"],
                "hours": 40   # 30 hours planned
            },
    "month_3": {"skills": ["RAG"],
                "hours": 20   # 30 hours planned
            },
    "month_4": {"skills": ["FastAPI"],
                "hours": 20   # 30 hours planned
            },
    "month_5": {"skills": ["Vector Databases"],
                "hours": 30   # 30 hours planned
            },
    "month_6": {"skills": ["Project Integration"],
                "hours": 25   # 30 hours planned
            }
    #他の月も追加
}

# TODO 4:進捗を表示する関数を作る
def show_progress(current_month, total_months = 12):
    """学習進捗を表示"""
    print(f"学習進捗: Month {current_month} / {total_months}")

    month = "month_" + str(current_month)

    if month in learning_plan:
        month_info = learning_plan[f"month_{current_month}"]
        skills = month_info["skills"]
        hours = month_info["hours"]
        print(f"今月の学習スキル: {', '.join(skills)}")
        print(f"予定学習時間: {hours} 時間\n")
    else:
        print("今月の学習計画はまだ設定されていません。\n") 

    pass


#実行してみる
for month in range(1, 12):
    show_progress(month)





