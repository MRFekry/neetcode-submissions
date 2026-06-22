public class Solution {
    public bool IsAnagram(string s, string t) {
        if (s.Length != t.Length)
            return false;

        Span<int> counts = new int[128];

        foreach (var c in s)
        {
            counts[c]++;
        }

        foreach (var c in t)
            if (--counts[c] < 0) return false;

        return true;
    }
}