class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for i in range(len(strs)):
            if tuple(sorted(Counter(strs[i]).items())) not in d:
                d[tuple(sorted(Counter(strs[i]).items()))] = [strs[i]]
            else:
                d[tuple(sorted(Counter(strs[i]).items()))].append(strs[i])
        print(d)
        return list(d.values())


# if use defaultdict, then you don't need to check key exist or not
# when use defaultdict, give default_factory defaultdict(list), otherwise it's same as regular dictionary
