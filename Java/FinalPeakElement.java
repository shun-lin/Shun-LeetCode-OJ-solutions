/* A peak element is an element that is greater than its neighbors.

  Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

  The array may contain multiple peaks, in that case return the index to any one of the peaks is fine. */

public class Solution {
    public int findPeakElement(int[] nums) {
        int biggest = Integer.MIN_VALUE;
        int index = 0;
        int result = 0;
        int tlen = nums.length;
        while (index < tlen) {
            if (nums[index] > biggest) {
                biggest = nums[index];
                result = index;
            }
            index += 1;
        }
        return result;
    }
}
