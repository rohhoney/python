#GPT의 답

def coordinate_compression(N, coordinates):
    # 입력 좌표를 (좌표값, 인덱스) 튜플로 변환
    coords_with_index = [(coord, i) for i, coord in enumerate(coordinates)]

    # 좌표값을 기준으로 오름차순으로 정렬
    sorted_coords = sorted(coords_with_index)

    # 정렬된 좌표값들에 대해 순서대로 순위를 부여하여 저장
    rank = 0
    compressed_coords = [0] * N
    for i in range(N):
        if i > 0 and sorted_coords[i][0] != sorted_coords[i - 1][0]:
            rank += 1
        compressed_coords[sorted_coords[i][1]] = rank

    return compressed_coords


# 입력 받기
N = int(input())
coordinates = list(map(int, input().split()))

# 좌표 압축 적용
result = coordinate_compression(N, coordinates)

# 결과 출력
print(*result)
