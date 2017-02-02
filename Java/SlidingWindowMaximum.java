/* Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right.

   You can only see the k numbers in the window. Each time the sliding window moves right by one position.  */

public class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        if (nums.length == 0) {
            return nums;
        }
        int result_length = nums.length - k + 1;
        int[] result = new int[result_length];
        int i = 0;
        while (i < result_length) {
            int ind_max = nums[i];
            for (int temp = i + 1; temp < i + k; temp += 1) {
                ind_max = Math.max(ind_max, nums[temp]);
            }
            result[i] = ind_max;
            i += 1;
        }
        return result;
    }
}
