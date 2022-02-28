def canJump(self, nums: list) -> bool:
        '''
        跳跃游戏
        :param nums: 
        :return: 
        '''
        max_jump = 0
        for i in range(len(nums)):
            if max_jump >= len(nums)-1:
                return True
            if i <= max_jump:
                jump = i + nums[i]
                max_jump = max(max_jump, jump)
                print(max_jump)
        return False
