#gpt의 답

if __name__ == "__main__":
    N = int(input())  # 점의 개수 N 입력
    points = []  # 점들을 저장할 리스트

    # 점들을 입력받아 points 리스트에 저장합니다.
    for _ in range(N):
        x, y = map(int, input().split())
        points.append([x, y])

    # 점들을 x 좌표를 오름차순으로, x 좌표가 같을 경우 y 좌표를 오름차순으로 정렬합니다.
    sorted_points = sorted(points)  #그냥 sort함수 쓰면 됐다.... 어이가 없어!

    # 정렬된 결과를 출력합니다.
    print(sorted_points)
    for point in sorted_points:
        print(point[0], point[1])