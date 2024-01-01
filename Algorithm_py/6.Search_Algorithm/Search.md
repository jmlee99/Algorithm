## 범위를 반씩 좁혀가는 탐색

***1. 순차탐색***

가장 기본적인 탐색방법이다. 

**순차 탐색**이란 리스트 안에 있는 특정한 데이터를 찾기 위해 앞에서부터 데이터를 하나씩 차례대로 확인하는 방법이다. 

보통 정렬되지 않은 리스트에서 데이터를 찾아야 할 때 사용한다. 

리스트 내에 데이터가 아무리 많아도 시간만 충분하다면 항상 원하는 원소(데이터)를 찾을 수 있다는 장점이 있다. 


            # Q1 7-1 순차 탐색 소스코드
            def sequential_search(n, tar, array):
                #각 원소를 하나씩 확인하며
                for i in range(n):
                    #현재 원소가 찾고자 하는 원소와 동일한 경우
                    if array[i] == tar:
                        return i + 1 # 현재의 위치 반환 (인덱스는 0부터 시작하므로 1 더하기)
            
            print('생성할 원소 개수를 입력한 다음 한 칸 띄고 찾을 문자열을 입력하세요.')
            input_data = input().split()
            n = int(input_data[0]) # 원소의 갯수
            tar = input_data[1] # 찾고자 하는 문자열
            
            print('앞서 적은 원소 개수만큼 문자열을 입력하세요. 구분은 띄어쓰기 한 칸으로 합니다.')
            array = input().split()
            
            # 순차 탐색 수행 결과 출력
            print(sequential_search(n, tar, array))

***2. 이진 탐색***

배열 내부의 데이터가 정렬되어 있어야만 사용할 수 있는 알고리즘이다.

이진 탐색은 탐색 범위를 절반씪 좁혀가며 데이터를 탐색하는 특징이 있다.

이진 탐색은 위치를 나타내는 변수 3개를 사용하는데 탐색하고자 하는 범위의 **시작점**, **끝점**, 그리고 **중간점**이다.

찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교해서 원하는 데이터를 찾는 게 이진 탐색 과정이다. 


            # 7-2 재귀함수로 구현한 이진 탐색 소스코드
            # 이진 탐색 소스코드 구현 (재귀 함수)
            def binary_search(array, tar, st, end):
                if st > end:
                    return None
                mid = (st + end) // 2
                #찾을 경우 중간점 인덱스 반환
                if array[mid] == tar:
                    return mid
                # 중간점의 값보다 찾고자하는 값이 작은 경우 왼쪽 확인
                elif array[mid] > tar:
                    return binary_search(array, tar, st, mid-1)
                # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
                else:
                    return binary_search(array, tar, mid+1, end)
            
            # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
            n, tar = list(map(int, input().split()))
            # 전체 원소 입력받기
            array = list(map(int, input().split()))
            
            # 이진 탐색 수행 결과 출력
            result = binary_search(array, tar, 0, n-1)
            if result == None:
                print('원소가 존재하지 않습니다.')
            else:
                print(result + 1)
            



            # 7-3 반복문으로 구현한 이진 탐색 소스코드
            def bi_search(array, tar, st, end):
                while st <= end:
                    mid = (st + end)//2
                    # 찾은 경우 중간점 인덱스 반환
                    if array[mid] == tar:
                        return mid
                      # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
                    elif array[mid] > tar:
                        end = mid -1
                    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
                    else:
                        st = mid +1
                return None
            # n(원소의 개수)과 target(찾고자 하는 문자열)을 입력받기
            n, tar = list(map(int, input().split()))
            # 전체 원소 입력받기
            array = list(map(int, input().split()))
            
            # 이진 탐색 수행 결과 출력
            result = binary_search(array, tar, 0, n-1)
            if result == None:
                print('원소가 존재하지 않습니다.')
            else:
                print(result + 1)

***빠르게 입력받기***

이진 탐색 문제는 입력 데이터가 많거나, 탐색 범위가 매우 넓은 편이다. 

예를 들어 데이터의 개수가 1,000만 개를 넘어가거나 탐색 범위의 크기가 1,000억 이상이라면 이진 탐색 알고리즘을 의심해 보자.

        # 빠르게 입력받기
        import sys
        # 하나의 문자열 데이터 입력받기
        input_data = sys.stdin.readline().rstrip()
        
        # 입력받은 문자열 그대로 출력
        print(input_data)


