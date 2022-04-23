def minimumTotal( triangle) -> int:
    triangle.reverse()

    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i]) - 1):
            triangle[i + 1][j] = min(triangle[i][j], triangle[i][j + 1]) + triangle[i + 1][j]
            print(triangle[i+1][j])
    return triangle[len(triangle) - 1][0]
minimumTotal(triangle =[[2],[3,4],[6,5,7],[4,1,8,3]])