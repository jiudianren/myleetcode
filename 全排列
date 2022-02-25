class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        re = [[nums[0],],]
        for cur_to_deal in nums[1:]:
            next_re = []
            for this_kind in re:
                for index_to_insert in range(len(this_kind)+1):
                    tmp = this_kind[:]
                    tmp.insert(index_to_insert, cur_to_deal)
                    #print(f"{tmp},")
                    next_re.append(tmp)
            #print("\n")
            re = next_re
        return re
