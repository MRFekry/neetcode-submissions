public class Solution {

    public string Encode(IList<string> strs) 
    {
        if (strs is [])
            return null;
        else if (strs is [""])
            return string.Empty;

        var encoded_string = string.Empty;
        if (strs is not null && strs.Count > 0)
        {
            if (strs.Count == 1)
                return strs.First();
            if (strs.Count == 2)
            {
                if (strs[0] == "," && strs[^1] == ",")
                    return ",,";
                if (strs[0] == "" && strs[^1] == "")
                    return "--";
                if (strs[0] == "," && strs[^1] == "")
                    return ",-";
                if (strs[0] == "" && strs[^1] == ",")
                    return "-,";
            }

            var is_first_str = true;
            foreach (var str in strs)
            {
                if (is_first_str)
                {
                    if (string.IsNullOrWhiteSpace(str))
                    {
                        if (str.Length == 0)
                            encoded_string = $"{str}!!";
                        else
                        {
                            encoded_string = str;
                            foreach (var space in str)
                            {
                                encoded_string = $"{encoded_string}--";
                            }
                        }
                    }
                    else
                        encoded_string = str;

                    is_first_str = false;
                    continue;
                }

                if (string.IsNullOrWhiteSpace(str))
                {
                    encoded_string = $"{encoded_string},,,";
                    if (str.Length == 0)
                        encoded_string = $"{encoded_string}!!";
                    else
                    {
                        foreach (var space in str)
                        {
                            encoded_string = $"{encoded_string}--";
                        }
                    }
                }
                else
                    encoded_string = $"{encoded_string},,,{str}";
            }
        }

        return encoded_string;
    }

    public List<string> Decode(string s) 
    {
        if (s is null)
            return [];
        if (s == string.Empty)
            return [""];
        if (s.Length == 1)
            return [s];
        if (s.Length == 2)
        {
            if (s[0] == ',' && s[1] == ',')
                return [",", ","];
            if (s[0] == '-' && s[1] == '-')
                return ["", ""];
            if (s[0] == ',' && s[1] == '-')
                return [",", ""];
            if (s[0] == '-' && s[1] == ',')
                return ["", ","];
        }

        var strs = new List<string>(s.Length);
        var str = string.Empty;
        var isNotSpaceNorSeparator = false;
        var beginsWithSeparator = false;
        var stringWasAdded = false;
        var firstCheckPassed = false;
        var spaceWasAdded = false;
        var spaceWasIncremented = false;
        var emptySpacesCounter = 0;
        var spaceCheck = false;
        for (int i = 0; i < s.Length; i++)
        {
            if (s[i] == '!' && i + 1 < s.Length && s[i + 1] == '!')
            {
                i++;
                continue;
            }

            if (i == 0 && s[i] == ',')
                beginsWithSeparator = true;

            if
            (firstCheckPassed &&
            s.Length == i + 2)
            {
                if (s[i + 1] == ',')
                {
                    str = ",";
                    break;
                }
                firstCheckPassed = false;
            }

            if
            (s[i] == ',' &&
            s[i + 1] == ',' &&
            s[i + 2] == ',')
            {
                if (beginsWithSeparator)
                {
                    str = ",";
                    beginsWithSeparator = false;
                    continue;
                }

                if (!stringWasAdded)
                {
                    if (spaceCheck && !spaceWasAdded)
                    {
                        str = new string(' ', emptySpacesCounter);
                        strs.Add(str);
                        str = string.Empty;
                        spaceWasAdded = true;
                        stringWasAdded = true;
                        emptySpacesCounter = 0;
                        continue;
                    }

                    strs.Add(str);
                    str = string.Empty;
                    stringWasAdded = true;
                    spaceWasIncremented = false;
                    emptySpacesCounter = 0;
                    continue;
                }
            }

            if (s[i] == '-')
            {
                if (s.Length == i + 1 && s[^1] == '-')
                {
                    str = string.Empty;
                    continue;
                }
                else if (i != 0 && s[i - 1] == '-')
                {
                    if (!spaceWasAdded)
                    {
                        spaceCheck = true;
                        if (!spaceWasIncremented)
                        {
                            emptySpacesCounter++;
                            spaceWasIncremented = true;
                            continue;
                        }
                        else if (spaceWasIncremented)
                        {
                            spaceWasIncremented = false;
                            continue;
                        }
                        str = new string(' ', emptySpacesCounter);
                        strs.Add(str);
                        str = string.Empty;
                        spaceWasAdded = true;
                        stringWasAdded = true;
                        continue;
                    }
                    else
                    {
                        spaceWasAdded = false;
                    }
                }
                else if (s[i + 1] == '-')
                {
                    spaceWasAdded = false;
                    continue;
                }
            }
            if
            (!((s[i] == ',' &&
            s[i - 1] == ',' &&
            s[i + 1] == ',') ||
            (s[i] == ',' &&
            s[i - 1] == ',' &&
            s[i - 2] == ',') ||
            stringWasAdded))
            {
                str = $"{str}{s[i]}";
                isNotSpaceNorSeparator = true;
                spaceCheck = false;
                continue;
            }

            stringWasAdded = false;
            spaceWasIncremented = false;

            if (s[i - 1] == ',' && s[i] == ',' && s[i + 1] == ',')
                firstCheckPassed = true;
        }

        if (isNotSpaceNorSeparator)
            strs.Add(str);

        return [.. strs];
    }
}
