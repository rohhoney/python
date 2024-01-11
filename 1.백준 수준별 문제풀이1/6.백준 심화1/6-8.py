#성적 딕셔너리
d_score = {"A+": 4.5, "A0": 4.0, "B+": 3.5, "B0": 3.0, "C+": 2.5, "C0": 2.0, "D+": 1.5, "D0": 1.0, "F": 0}

#학점합, 성적 합 변수 선언
hak_sum = 0.0
sung_sum = 0.0

for _ in range(20):
    s = input()
    slist = s.split()
    if slist[2] == "P":
        pass
    else:
        hak_sum = hak_sum + float(slist[1])
        sung_sum = sung_sum + d_score[slist[2]] * float(slist[1])

print(sung_sum/hak_sum)