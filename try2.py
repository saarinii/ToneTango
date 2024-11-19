if __name__ == "__main__":
    s = "timetopractice"
    p = "toc"
    
    m = len(s)
    n = len(p)
    smallest_substring = ""
    min_len = float('inf')
    for i in range(m):
        count = [0] * 256
        for ch in p:
            count[ord(ch)] += 1
        
        matched_chars = len(p)

        for j in range(i, m):
            ch = s[j]
            if count[ord(ch)] > 0:
                matched_chars -= 1
            count[ord(ch)] -= 1
            if matched_chars == 0:
                curr_len = j - i + 1
                if curr_len < min_len:
                    min_len = curr_len
                    smallest_substring = s[i:j + 1]
                break

    if smallest_substring:
        print(smallest_substring)
    else:
        print("")
