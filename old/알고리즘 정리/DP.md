# Algorithm_study
## DP algoritm

- Dynamic Programming (DP) 는 부분적인 최적해 (작은 문제의 결과)를 저장해 큰 문제의 결과와 합하는 방식
- 점화식을 아는게 중요!

### DP 속성
- Overlapping SUbproblem (부분 문제 겹치는 경우)
- Optimal Substructure (최적 부분 구조)

## Memoization
- ex) fibonacci 수열
  - 물론 재귀함수를 호출 할 수 있지만, 수가 커지면서 같은 함수를 계속 호출하는 경우 다반사
  - ex : f(4)를 호출할때, f(3) + f(2) = f(2) + f(1) + f(2) 로 되면서 f(2)값은 이미 알게 된다.
  - 말인 즉슨, 다시 호출할 이유가 없다.
- 작은 문제들이 반복되는데, 그 문제들을 구할 때 마다 답이 같으면 memoization 사용  

  
## LIS


### reference
- https://developer-mac.tistory.com/77
- https://medium.com/@wooder2050/%EB%8F%99%EC%A0%81%EA%B3%84%ED%9A%8D%EB%B2%95-dynamic-programming-%EC%A0%95%EB%A6%AC-58e1dbcb80a0
