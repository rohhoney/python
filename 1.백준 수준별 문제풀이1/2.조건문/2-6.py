#요리시간 계산기
hour, minute = input().split()
cktime = input()
hour = int(hour)
minute = int(minute)
cktime = int(cktime)

minresult = hour*60 + minute + cktime

if minresult >= 24*60:
    minresult -= 24*60

resulthour = int(minresult / 60)
resultmin = minresult % 60

print("%d %d" % (resulthour, resultmin))