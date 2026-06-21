public class Solution {
    public bool IsAnagram(string s, string t) {
        if (string.IsNullOrWhiteSpace(s) || string.IsNullOrWhiteSpace(t) || s.Length != t.Length)
            return false;

        var charDict = new Dictionary<char, int>();
        foreach (var item in s)
        {
            if (!charDict.ContainsKey(item))
                charDict.Add(item, 0);
            charDict[item]++;
        }

        foreach (var item in charDict)
        {
            int count = 0;
            foreach (var c in t)
            {
                if (c == item.Key)
                    count++;
            }

            if (count != item.Value)
                return false;
        }

        return true;
    }
}
