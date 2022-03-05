# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        houxuan=dict()
        head = ListNode(0,None)
        cur_head =head
        while len(lists):
            to_delete=[]
            for i in range(len(lists)):
                if lists[i] != None:
                    if lists[i] not in houxuan.values():
                        
                        cur_val = lists[i].val
                        if cur_val not in houxuan.keys():
                            houxuan[cur_val] = lists[i]
                            lists[i] = lists[i].next
                else:
                    to_delete.append(i)
            #从后往前删除
            for i in to_delete[::-1]:
                #print(i)
                lists.pop(i)
            
            if len(houxuan):
                cur_head.next = houxuan[min(houxuan.keys())]
                del houxuan[min(houxuan.keys())]
            cur_head = cur_head.next
        for i in sorted(houxuan):
            cur_head.next = houxuan[i]
            cur_head = cur_head.next
        return head.next
