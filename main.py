from helpers.list_node import ListNode

from lc_21_merge_two_sorted_lists.merge_two_sorted_lists import Solution


if __name__ == '__main__':
    result = Solution().mergeTwoLists(ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4))))
    print(result)
