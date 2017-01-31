/* A peak element is an element that is greater than its neighbors.

  Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

  The array may contain multiple peaks, in that case return the index to any one of the peaks is fine. */

  int findPeakElement(int* nums, int numsSize) {
    int biggest = nums[0];
    int index = 0;
    int result = 0;
    while (index < numsSize) {
        if (nums[index] >= biggest) {
            biggest = nums[index];
            result = index;
        }
        index += 1;
    }
    return result;

}
