from Graph import *

def buildGraph(wordLen, wordFile):
    d = {}
    g = Graph()
    wFile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wFile:
        word = line[:-1]
        if len(word) == wordLen:
            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
    # add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


def bfs(g, start, end):
    explored = [start]
    searched = []
    while explored:
        if end in searched:
            pathNode = end
            while pathNode is not None:
                print(pathNode.id)
                pathNode = pathNode.father
            return True
        currNode = explored.pop(0)
        searched.append(currNode)
        for nextNode in currNode.getConnections():
            if nextNode not in searched and nextNode not in explored:
                nextNode.father = currNode
                explored.append(nextNode)
    return False




if __name__ == "__main__":
    g = buildGraph(4, "words.txt")
    bfs(g, g.vertList['fool'], g.vertList['sage'])
