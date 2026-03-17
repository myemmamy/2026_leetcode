class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        MOD=10**9+7
        ans = 0
        for i in range(len(arr)-2):
            l = i+1
            r = len(arr)-1
            while l < r:
                total = arr[i]+arr[l]+arr[r]
                if total == target:
                    lcount,rcount = 1,1
                    if arr[l] != arr[r]:
                        while l+1 < r and arr[l+1] == arr[l]:
                            lcount += 1
                            l += 1
                        while l+1 < r and arr[r-1] == arr[r]:
                            rcount += 1
                            r -= 1
                        ans += lcount*rcount
                    else:
                        m = r-l+1
                        ans += m*(m-1)//2
                        break
                    l += 1 
                    r -= 1
                elif total < target:
                    l += 1
                else:
                    r -= 1
        return ans%MOD
