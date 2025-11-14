class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index_map = {}  # 存储字符及其最新索引位置
        max_length = 0  # 最长子串长度
        start = 0  # 滑动窗口起始位置

        for end in range(len(s)):
            # 如果当前字符已经在窗口中出现过
            if s[end] in char_index_map and char_index_map[s[end]] >= start:
                # 移动窗口起始位置到重复字符的下一位置
                start = char_index_map[s[end]] + 1

            # 更新字符的最新位置
            char_index_map[s[end]] = end

            # 更新最大长度
            max_length = max(max_length, end - start + 1)

        return max_length