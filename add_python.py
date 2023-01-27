def find_longest_substr(str1, str2):
    string1 = str1.split()
    string2 = str2.split()
    list_of_substring1 = [string1[i: j] for i in range(len(str1)) for j in range(i + 1, len(str1)+1)]
    list_of_substring2 = [string2[i: j] for i in range(len(str2)) for j in range(i + 1, len(str2)+1)]
    common_string = []
    for s in list_of_substring1:
        if s in list_of_substring2:
            common_string.append(common_string)
    get_len_dict = {}
    for s in common_string:
        get_len_dict[s] = len(s)
    max = 0
    longest_common_string = "Not Found"
    for s in get_len_dict:
        if get_len_dict[s] >= max:
            longest_common_string = s
    return longest_common_string
            
        
