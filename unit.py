import unittest
from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()

    def put(self, item):
        self.queue.append(item)

    def get(self):
        return self.queue.popleft()

    def empty(self):
        return len(self.queue) == 0

class TestQueue(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.put(1)
        self.assertEqual(self.queue.queue[0], 1, "Front should be 1 after enqueueing.")
        self.assertEqual(self.queue.queue[-1], 1, "Rear should be 1 after enqueueing.")
        self.assertFalse(self.queue.empty(), "Queue should not be empty after enqueueing.")

    def test_dequeue(self):
        self.queue.put(1)
        self.queue.put(2)
        self.queue.put(3)
        self.queue.get()
        self.assertEqual(self.queue.queue[0], 2, "Front should be 2 after dequeuing one item.")
        self.assertEqual(self.queue.queue[-1], 3, "Rear should be 3 after dequeuing one item.")
        self.assertFalse(self.queue.empty(), "Queue should not be empty after dequeuing.")

    def test_dequeue_empty_queue(self):
        with self.assertRaises(IndexError):
            self.queue.get()

    def test_front(self):
        self.queue.put(1)
        self.assertEqual(self.queue.queue[0], 1, "Front should be 1 after enqueueing.")

    def test_rear(self):
        self.queue.put(1)
        self.assertEqual(self.queue.queue[-1], 1, "Rear should be 1 after enqueueing.")

    def test_is_empty(self):
        self.assertTrue(self.queue.empty(), "Queue should be empty initially.")
        self.queue.put(1)
        self.assertFalse(self.queue.empty(), "Queue should not be empty after enqueueing an item.")

if __name__ == '__main__':
    unittest.main()
