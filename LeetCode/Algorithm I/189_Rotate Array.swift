class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        var resultArr = [Int](repeating: 0, count: nums.count)
        for i in 0..<nums.count {
            resultArr[(i+k)%(nums.count)] = nums[i]
        }
        nums = resultArr
    }
}
