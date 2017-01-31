/* There are two sorted arrays nums1 and nums2 of size m and n respectively.

   Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)). */

public class Solution {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {

        int[] nums = new int[nums1.length + nums2.length];
        System.arraycopy(nums1, 0, nums, 0, nums1.length);
        System.arraycopy(nums2, 0, nums, nums1.length, nums2.length);
        java.util.Arrays.sort(nums);
        int tlen = nums.length;
        if (nums.length % 2 != 0) {
            return nums[tlen / 2];
        }
        else {
            return (float) ((nums[tlen / 2 - 1] + nums[tlen / 2])) / 2;
        }
    }
}
