public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        if (k <= 0 || k > nums.Length)
            return [];

        var numsSpan = nums.AsSpan();
        var numCountsDic = new Dictionary<int, int>(numsSpan.Length);
        for (int i = 0; i < numsSpan.Length; i++)
        {
            if (!numCountsDic.TryGetValue(numsSpan[i], out _))
            {
                int num = numsSpan[i];
                int maxCount = 0;

                foreach (var number in numsSpan)
                {
                    if (number == num)
                        maxCount++;
                }

                numCountsDic[num] = maxCount;
            }
        }

        var result = new int[k];
        for (int i = 0; i < k; i++)
        {
            int maxFrequency = 0;
            int maxCount = 0;
            foreach (var item in numCountsDic)
            {
                if (item.Value > maxCount)
                {
                    maxCount = item.Value;
                    maxFrequency = item.Key;
                }
            }

            numCountsDic[maxFrequency] = 0;
            result[i] = maxFrequency;
        }

        return result;
    }
}
