# program for Boggle game
class Boogle(object):

    def __init__(self, dictionary, graph):
        self.d = dictionary
        self.g = graph
        self.n = len(self.g)
        self.m = len(self.g[0])

    # A recursive function to print all words present on boggle
    def find_word_util(self, visited, i, j, string):
        # Mark current cell as visited and append current character to string
        visited[i][j] = True
        string = string + self.g[i][j]

        # If str is present in dictionary, then print it
        if string in self.d:
            print(string)

        # Traverse 8 adjacent cells of boggle[i][j]
        for row in range(max(0, i-1), min(i+2, self.n)):
            for col in range(max(0, j-1), min(j+2, self.m)):
                if visited[row][col] is False:
                    self.find_word_util(visited, row, col, string)

        # Erase current character from string and mark visited of current cell as false
        visited[i][j] = False

    # Prints all words present in dictionary.
    def find_word(self):
        # Mark all characters as not visited
        visited = [[False for _ in range(self.m)] for _ in range(self.n)]

        # Initialize current string
        string = ""

        # Consider every character and look for all words starting with this character
        for i in range(self.n):
            for j in range(self.m):
                if visited[i][j] is False:
                    self.find_word_util(visited, i, j, string)


if __name__ == "__main__":
    dictionary = ["GEEKS", "FOR", "QUIZ", "GO"]
    graph = [['G', 'I', 'Z'],
             ['U', 'E', 'K'],
             ['Q', 'S', 'E']]

    boogle = Boogle(dictionary, graph)
    boogle.find_word()
