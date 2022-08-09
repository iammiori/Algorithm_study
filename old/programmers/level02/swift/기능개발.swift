import Foundation

func solution(_ progresses:[Int], _ speeds:[Int]) -> [Int] {
    var remainArr : [Int] = []
    var ansArr : [Int] = []
    for i in 0..<progresses.count {
        if (100-progresses[i])%speeds[i] == 0 {
        remainArr.append((100-progresses[i])/speeds[i])
    } else {
        remainArr.append((100-progresses[i])/speeds[i] + 1)
    }
    }
    var pointer : Int = 0
    var cnt : Int 
    while pointer < remainArr.count {
        let nowDue = remainArr[pointer]
        cnt = 0
        while pointer < remainArr.count && remainArr[pointer] <= nowDue {
            cnt += 1
            pointer += 1
        }
        ansArr.append(cnt)
    }
    return ansArr
}
