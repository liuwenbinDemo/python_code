#!/usr/bin/env python
# -*- coding: utf-8 -*-
from typing import List


class SolTe:
    def summary(self,nums:List[int])->List[str]:
        res = []
        l = 0
        for i in range(len(nums)):
            while i + 1 <len(nums) and nums[i]==nums[i+1] -1:
                i +=1

            if nums[i] == nums[l]:
                res.append(str(nums[i]))
            else:
                res.append(str([nums[l]])+'->'+str(nums[i]))
            l = i + 1
        return res


print(SolTe().summary([1, 3, 5]))