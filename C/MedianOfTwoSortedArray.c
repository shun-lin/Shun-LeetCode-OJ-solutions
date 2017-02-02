/*  Given an array of integers, return indices of the two numbers such that they add up to a specific target.

    You may assume that each input would have exactly one solution.  */

    #include <stdlib.h>

    double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size) {
        int tlen = nums1Size + nums2Size;
        int* nums = malloc(tlen * sizeof(int));
        memcpy(nums, nums1, nums1Size * sizeof(int));
        memcpy(nums + nums1Size, nums2, nums2Size * sizeof(int));

         int compare( const void* a, const void* b) {
         int int_a = * ( (int*) a );
         int int_b = * ( (int*) b );

         if ( int_a == int_b ) return 0;
         else if ( int_a < int_b ) return -1;
         else return 1;
         }

         qsort(nums, tlen, sizeof(int), compare);

         if (tlen % 2 != 0) {
             return nums[tlen / 2];
         }
         else {
             return (float) ((nums[tlen / 2 - 1] + nums[tlen / 2])) / 2;
         }

    }
