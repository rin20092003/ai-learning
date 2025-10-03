# 1. シンプルな関数
def greet(name):
    return f"こんにちは、{name}さん！"

print(greet("RIN"))

# 2. 複数の引数
def calculate_target_income(current, increase_percent):
    target = current * (1 + increase_percent / 100)
    return int(target)

current = 550
target = calculate_target_income(current, 64)
print(f"\n現在: {current}万円")
print(f"目標: {target}万円")

# 3. デフォルト引数
def introduce(name, job="Engineer", country="Vietnam"):
    return f"I'm {name}, {job} from {country}."

print(f"\n{introduce('RIN')}")
print(introduce('RIN', 'AI Engineer', 'Vietnam'))

# 4. 実用的な関数
def calculate_study_progress(months_passed, total_months=18):
    progress = (months_passed / total_months) * 100
    remaining = total_months - months_passed
    return {
        'progress': round(progress, 1),
        'remaining_months': remaining
    }

result = calculate_study_progress(3)
print(f"\n3ヶ月後の進捗: {result['progress']}%")
print(f"残り: {result['remaining_months']}ヶ月")