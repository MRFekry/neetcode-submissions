public class Solution {
    public List<List<string>> GroupAnagrams(string[] strs) {
        var result = new List<List<string>>(strs.Length);
        var stringsSpan = strs.AsSpan();

        for (int i = 0; i < stringsSpan.Length; i++)
        {
            var stringWasAddedToAnagram = false;
            foreach (var sublist in result)
            {
                if (!sublist.Contains(stringsSpan[i]))
                    continue;
                stringWasAddedToAnagram = true;
                break;
            }

            if (stringWasAddedToAnagram) continue;

            var itemAnagramList = new List<string>(stringsSpan.Length);

            if (!itemAnagramList.Contains(stringsSpan[i]))
                itemAnagramList.Add(stringsSpan[i]);

            for (int j = i + 1; j < stringsSpan.Length; j++)
            {
                if (IsAnagram(stringsSpan[i], stringsSpan[j]))
                {
                    itemAnagramList.Add(stringsSpan[j]);
                }
            }

            result.Add(itemAnagramList);
        }

        return result;
    }

    private bool IsAnagram(string _s, string _t)
    {
        if (_s.Length != _t.Length) return false;

        Span<int> charCounts = new int[26];

        for (int i = 0; i < _s.Length; i++)
        {
            charCounts[_s[i] - 'a']++;
            charCounts[_t[i] - 'a']--;
        }

        foreach (int count in charCounts)
        {
            if (count != 0) return false;
        }

        return true;
    }
}
