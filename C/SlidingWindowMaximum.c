/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdlib.h>

int* maxSlidingWindow(int* nums, int numsSize, int k, int* returnSize) {
    if (numsSize < 1) {
        return nums;
    }
    int resultLength = numsSize - k + 1;
    int* result = malloc(resultLength * sizeof(int));
    int i = 0;
    while ( i < resultLength) {
        int ind_max = nums[i];
        for (int temp = i; temp < i + k; temp = temp + 1) {
            if (nums[temp] > ind_max) {
                ind_max = nums[temp];
            }
        }
        *(result +i) = ind_max;
        i = i + 1;
    }
    return result;
}
