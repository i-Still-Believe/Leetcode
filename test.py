# a = [1,2,3,4]
# a.pop()
# print(a)
#
# score = [5, 5.75, 5.25, 5.25, 5.5, 5.75, 5.75, 5.75]
# credit = [10, 8, 8, 9, 8, 8, 8, 2]
# print(sum([i*j for (i, j) in zip(score, credit)]) / sum(credit))
#
# a = 5*10+5.75*8+5.25*8+5.25*9+5.5*8+5.75*8+5.75*8+5.75*2
# b = 10+8+8+9+8+8+8+2
# print(a/b)
# print((1,2)+(3, 4))
#
# A = ([(c, i), (j, c), (int(i / 3), int(j / 3), c)]
#                     for i in range(9) for j in range(9)
#                     for c in [0, 1] if c != '.')
# for i in A:
#     print(i)
# a = ([(1,2),(3,4)],[(5,6),(7,8)])
# print(a)
# print(sum(a,[]))
#
# a = [""]
# print(a[0])
# a = [list(x) for x in a]
# print(a)
#
# a = {1:2, 3:4}
# print(a.keys())

# intervals = [[7,3],[2,6],[8,10],[15,18]]
# print(sorted(intervals, key=lambda t:t[1]))

# print(len([0]))

a = [3,5,7]
a=enumerate(a)
print(list(a))
for i in range(0,-1,-1):
    print(i)

stack = [1,2,3,4]
print(stack.pop())