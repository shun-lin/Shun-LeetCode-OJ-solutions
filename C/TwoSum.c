/**
 * Given an array of integers, return indices of the two numbers such that they add up to a specific target.
 * You may assume that each input would have exactly one solution.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* twoSum(int* nums, int numsSize, int target) {
    int i = 0;
    int j = 1;
    int sum = nums[0] + nums[1];
    while (target != sum) {
            if (j == numsSize - 1) {
                    i += 1;
                    j = i + 1;
            }
            else { 
                    j += 1;
            }
            sum = nums[i] + nums[j];
    }
    int* p = malloc(2 * sizeof(int));
    *p = i;
    *(p + 1) = j;
    return p;
}
