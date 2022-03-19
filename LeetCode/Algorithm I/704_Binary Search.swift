class Solution {
    func search(_ nums: [Int], _ target: Int) -> Int {
        var startIdx : Int = 0
        var endIdx : Int = nums.count - 1
        
        while startIdx <= endIdx {
            let midIdx : Int = (startIdx + endIdx) / 2
            if target == nums[midIdx] {
                return midIdx
            } else if nums[midIdx] > target {
                endIdx = midIdx - 1
            } else if nums[midIdx] < target {
                startIdx = midIdx + 1
            }
        }
        
        return -1 
    }
}
