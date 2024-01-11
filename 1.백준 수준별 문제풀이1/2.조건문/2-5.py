#오븐문제
hour, minute = input().split()
hour = int(hour)
minute = int(minute)

mintime = hour*60 + minute - 45


if mintime < 0:
    mintime += 24*60    #00시45분이하일때 24시간 더해서 11시 00분 만들기

alhour = mintime//60
almin = mintime % 60

print("%d %d" % (alhour,almin))
