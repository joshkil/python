import heapq
items = [(1, "Josh"), (5, "Jim"), (7, "Sarah"), (3, "Sarah")]

h = list()
for i in items:
    heapq.heappush(h, i)

print(h)

while len(h) > 0:
    i = heapq.heappop(h)
    print("Components {} : {}".format(i[0], i[1]))
    print(h)