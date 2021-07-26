"""
로그를 재정렬하라
1. 로그의 가장 앞 부분은 식별자
2. 문자로 구성된 로그가 숫자 로그보다 앞에
3. 식별자는 순서에 영향을 끼치지 않지만 문자가 동일할 경우 식별자 순
4. 숫자 로그는 입력 순서대로
"""

def reorderLogFiles(self, logs: List[str]) -> List[str]:
    letters, digits = [], []
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
    return letters + digits

