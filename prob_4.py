class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_length = 0
        char_set = set()

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_length = max(max_length, right - left + 1)

        return max_length


# -------- Testing in VS Code --------

if __name__ == "__main__":
    solution = Solution()

    s1 = "abcabcbb"
    s2 = "bbbbb"

    print("Input:", s1)
    print("Output:", solution.lengthOfLongestSubstring(s1))

    print("\nInput:", s2)
    print("Output:", solution.lengthOfLongestSubstring(s2))
 
#  O/P - Input: abcabcbb
        # Output: 3

        # Input: bbbbb
        # Output: 1