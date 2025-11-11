import os
import random
import csv

def get_names(file_name: str) -> list[str]:
    """傳入檔案名稱，讀取assets內的txt，並轉換為list"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'assets', file_name)

    with open(file_path, encoding="utf-8") as file:
        content = file.read()

    return [name.strip() for name in content.split('\n') if name.strip()]

def get_scores(names: list[str], num=10) -> list[dict]:
    if num > len(names):
        raise ValueError(f"學生數量({num})不能超過名單({len(names)})")
    
    stu_names = random.sample(names, num)
    scores = []
    for name in stu_names:
        info = {"姓名": name,
                "國文": random.randint(50, 100),
                "英文": random.randint(50, 100),
                "數學": random.randint(50, 100)}
        scores.append(info)
    return scores

def save_csv(students: list[dict], filename: str) -> None:
    fieldnames = students[0].keys()
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'assets', filename)

    with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(students)

def main():
    try:
        names = get_names("names.txt")
        num = int(input(f"請輸入學生數量(最多{len(names)}): "))
        students = get_scores(names, num=num)
        save_csv(students, 'students.csv')
        print(f"成功產生 {num} 位學生的成績單")
    except FileNotFoundError:
        print("錯誤: 找不到 names.txt 檔案")
    except ValueError as e:
        print(f"錯誤: {e}")

if __name__ == '__main__':
    main()