class Solution {
    func fib(_ n: Int) -> Int {
        var dpTable : [Int] = [Int](repeating : 0, count : n)
        if n == 0 {
            return 0
        } else if n == 1 {
            return 1
        }
        dpTable[0] = 1
        dpTable[1] = 1
        for idx in 2..<n {
            dpTable[idx] = dpTable[idx-1] + dpTable[idx-2]
        }
        return dpTable[n-1]
    }
