#!/usr/bin/env python


class Queue():
    def __init__(self, n):
        self.length = n
        self.lst = ['NA'] * n
        self.head = 0
        self.tail = 0

    def enqueue(self, x):
        if self.head == self.tail + 1:
            raise Exception("The queue has been full and can't be enqueued")
        self.lst[self.tail] = x
        if self.tail == self.length:
            self.tail = 0
        else:
            self.tail += 1
            if self.tail == self.length:
                self.tail = 0

    def tail_plus_one(self):
        return 0 if self.tail + 1 == self.length else self.tail + 1

    def dequeue(self):
        if self.head == self.tail and self.head == 0:
            raise Exception("The quue now is empty and can't be dequeued")
        x = self.lst[self.head]
        if self.head == self.length:
            self.head = 0
        else:
            self.head += 1
            if self.head == self.length:
                self.head = 0
        return x

    def _print_queue(self):
        print("my head is: ", self.head)
        print("my tail is:", self.tail)
        # print(self.lst[self.head:self.tail+1])
        print(self.lst)

if __name__ == '__main__':
    que1 = Queue(10)
    queue = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # msg = que1.dequeue()
    # print(msg)
    que1._print_queue()
    que1.enqueue(queue[0])
    que1._print_queue()
    item1 = 5
    que1.enqueue(item1)
    que1._print_queue()
    for i in queue:
        que1.enqueue(i)
        que1._print_queue()
