# Check if index of row and col is valid or not, value of next position larger than 1 compare to previous position or not
def is_valid(mat, i, j, i_before, j_before):
    m, n = len(mat), len(mat[0])
    if i >= 0 and i < m and j >= 0 and j < n and mat[i][j] == mat[i_before][j_before]+1:
        return True
    return False

# Using DFS to get all the position in matrix
def dfs_longest_path(mat, dp, i, j, row, col):

    # If this subproblem is already solved
    if dp[i][j] != -1:
        return dp[i][j]

    # using tmp array to store all tmp value in each direction
    tmp_value = [-1 for _ in range(len(row))]
    for id in range(len(row)):
        if is_valid(mat, i + row[id], j+ col[id], i, j):
            tmp_value[id] = 1 + dfs_longest_path(mat, dp, i+row[id], j+col[id], row, col)

    # If none of the adjacent fours is one greater we will take 1
    # otherwise we will pick maximum from all the four directions
    dp[i][j] = max(*tmp_value, 1)

    return dp[i][j]

# Returns length of the longest path beginning with any cell
def find_longest_path(mat):
    result = 1
    m, n = len(mat), len(mat[0])
    # Create a lookup table and fill all entries in it as -1
    dp = [[-1 for _  in range(n)] for _ in range(m)]
    row = [0, 0, 1, -1]
    col = [1, -1, 0, 0]

    # Compute longest path beginning from all cells
    for i in range(m):
        for j in range(n):
            if (dp[i][j] == -1):
                dfs_longest_path(mat, dp, i, j, row, col)

            # Update result if needed
            result = max(result, dp[i][j])

    return result

if __name__ == "__main__":
    mat = [[1, 2, 9],
           [5, 3, 8],
           [4, 6, 7]]

    result = find_longest_path(mat)
    print("the lonngest path is: ", result)
