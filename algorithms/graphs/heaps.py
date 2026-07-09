import heapq

my_heap = []
heapq.heappush(my_heap, 9)
heapq.heappush(my_heap, 8)
heapq.heappush(my_heap, 7)
print(my_heap)  #[7, 9, 8]

heapq.heappop(my_heap)
print(my_heap)  #[8, 9]

heapq.heappushpop(my_heap, 7)
print(my_heap)   #[]

nums = [5, 7, 3, 1]
heapq.heapify(nums)
print(nums)  #[1, 5, 3, 7]

my_heap = []
heapq.heappush(my_heap, (3, "A"))
heapq.heappush(my_heap, (2, "B"))
heapq.heappush(my_heap, (1, "A"))
print(my_heap)  #[(1, 'A'), (3, 'A'), (2, 'B')]

print(heapq.heappop(my_heap))  #(1, 'A')


#heap: time complexity(O(logn))