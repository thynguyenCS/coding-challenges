#class Solution(object):
def intervalIntersection(A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    intersection = []
    i = j = 0

    while i < len(A) and j < len(B):
        start = max(A[i][0], B[j][0])
        end = min(A[i][1], B[j][1])
        if start <= end:
            intersection.append([start, end])

        if A[i][1] < B[j][1]:
            i += 1
        else:
            j += 1

    return intersection

def main():
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    print(intervalIntersection(A, B))


if __name__ == '__main__':
    main()


