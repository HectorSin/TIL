### 셀 정렬

def shell_sort(A):
    n = len(A)
    gap = n//2

    while gap>0:
        if (gap%2) == 0:
            gap += 1
        for i in range(gap):
            sortGapInsertion(A, i, n-1, gap)
        print('   Gap=', gap, A)
        gap = gap//2

def sortGapInsertion(A, first, last, gap):
    for i in range(first+gap, last+1, gap):
        key = A[i]
        j = i - gap
        while j >= first and key<A[j]:
            A[j+gap] = A[j]
            j = j - gap
        A[j+gap] = key

### 힙 정렬(Heapify 알고지즘)

### 병합 정렬

### 퀵 정렬

### 이중피벗 퀵 정렬

### 기수, 카운팅 정렬

### 정렬 알고리즘의 성능 비교
