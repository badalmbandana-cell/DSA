#include <bits/stdc++.h>
using namespace std;
class Solution {
public:
    bool canBeIncreasing(vector<int>& nums) {
        if (nums.size() == 2)
            return true;
        int count = 0;
        int n = nums.size();
        int size = 1;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                size++;
            } else {
                if (size == 1) {
                    count++;
                    if (count > 1)
                        return false;
                } else {
                    count++;
                    if (count > 1)
                        return false;
                    if (nums[i] > nums[i - 2]) {
                        nums[i - 1] = nums[i];
                        continue;
                    }
                    count--;
                    if (i + 1 < n && nums[i + 1] > nums[i - 1]) {
                        nums[i] = nums[i + 1];
                        count++;
                        i++;
                    } else if (i == n - 1) {
                        count++;
                        continue;
                    } else {
                        return false;
                    }
                }
            }
        }

        return true;
    }
};