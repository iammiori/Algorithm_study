import Foundation

func solution(_ numbers:[Int]) -> [Int] {

    var ansSet : Set<Int> = []
    for i in 0..<numbers.count-1 {
        for j in i+1..<numbers.count {
            ansSet.insert(numbers[i]+numbers[j])
        }
    }
    var ansArr : [Int] = Array(ansSet)
    return ansArr.sorted()
}
