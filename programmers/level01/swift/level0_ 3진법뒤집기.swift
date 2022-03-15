import Foundation

func solution(_ n:Int) -> Int {
    var arr: [Int] = [] 
    var number : Int = n
    var ans : Int = 0
    while number > 0 { 
        arr.append(number % 3)
        number /= 3
    }
    (0..<arr.count).forEach { 
        let powNum = Int(pow(3.0, Double($0)))
        ans += (powNum * arr[arr.count - 1 - $0])
    }
    return ans
}
