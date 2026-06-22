public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        for (int i = 0; i < nums.Length; i++)
        {
            for (int j = 1; j < nums.Length; j++)
            {
                if (i != j && nums[i] + nums[j] == target)
                    return [i, j];
            }
        }

        return [];
    }
}
