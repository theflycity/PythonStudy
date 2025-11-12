# 创建测试类
import unittest
from ListNode import ListNode
from Exercise02 import Solution

class TestAddTwoNumbers(unittest.TestCase):
    def create_linked_list(self, values):
        """辅助方法：根据数值列表创建链表"""
        if not values:
            return None
        head = ListNode(values[0])
        current = head
        for i in range(1, len(values)):
            current.next = ListNode(values[i])
            current = current.next
        return head

    def linked_list_to_list(self, head):
        """辅助方法：将链表转换为数值列表"""
        result = []
        current = head
        while current:
            result.append(current.val)
            current = current.next
        return result

    def test_basic_addition(self):
        """测试基本加法：243 + 564 = 807"""
        solution = Solution()
        l1 = self.create_linked_list([2, 4, 3])  # 表示数字342
        l2 = self.create_linked_list([5, 6, 4])  # 表示数字465
        result = solution.addTwoNumbers(l1, l2)
        expected = [7, 0, 8]  # 表示数字807
        self.assertEqual(self.linked_list_to_list(result), expected)

    def test_with_carry(self):
        """测试进位情况：99 + 1 = 100"""
        solution = Solution()
        l1 = self.create_linked_list([9, 9])  # 表示数字99
        l2 = self.create_linked_list([1])     # 表示数字1
        result = solution.addTwoNumbers(l1, l2)
        expected = [0, 0, 1]  # 表示数字100
        self.assertEqual(self.linked_list_to_list(result), expected)

    def test_zero_case(self):
        """测试零的情况：0 + 0 = 0"""
        solution = Solution()
        l1 = self.create_linked_list([0])  # 表示数字0
        l2 = self.create_linked_list([0])  # 表示数字0
        result = solution.addTwoNumbers(l1, l2)
        expected = [0]  # 表示数字0
        self.assertEqual(self.linked_list_to_list(result), expected)

# 运行测试
if __name__ == '__main__':
    unittest.main()


