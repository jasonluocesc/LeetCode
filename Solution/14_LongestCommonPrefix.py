class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return " "


        for i, letter_group in enumerate(zip(*strs)):

            print(set(letter_group))
            if len(set(letter_group))>1:
                print("o")
                return strs[0][:i]
            else:
                print("s")
                return min(strs)

strs_1 = ['avce','avco','avcd']
print(Solution().longestCommonPrefix(strs_1))
