/*  Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.  */

public class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] result = new int[2];
        int i = 0;
        int j = 1;
        int reminder = target - nums[i] - nums[j];
        while (reminder != 0) {
            if (j == nums.length - 1) {
                    i += 1;
                    j = i + 1;
            }
            else {
                    j += 1;
            }
            reminder = target - nums[i] - nums[j];
        }
        result[0] = i;
        result[1] = j;
        return result;
    }
}
