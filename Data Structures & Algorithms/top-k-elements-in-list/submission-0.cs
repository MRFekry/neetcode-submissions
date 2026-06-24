public class Solution {
    public int[] TopKFrequent(int[] nums, int k) {
        if (k <= 0 || k > nums.Length)
            return [];

        var result = new int[k];
        var numsSpan = nums.AsSpan();
        var numCountsDic = new Dictionary<int, int>();

        foreach (var number in numsSpan)
        {
            if (numCountsDic.ContainsKey(number))
                numCountsDic[number]++;
            else
                numCountsDic.Add(number, 1);
        }

        result =
            [.. numCountsDic
            .OrderByDescending(static v => v.Value)
            .Take(k)
            .Select(p => p.Key)];

        return result;
    }
}
