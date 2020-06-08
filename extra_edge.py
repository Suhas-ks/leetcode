class DisjointSet(object):

    def __init__(self):
        self._parent = {}
        self._rank = {}

    @property
    def get_ranks(self):
        return list(self._rank.values())

    @property
    def get_parents(self):
        return list(self._parent.values())

    def make_set(self, e):
        self._parent[e] = e
        self._rank[e] = 0

    def find(self, i):
        """
        With Path Compression
        """
        while i != self._parent[i]:
            self._parent[i] = self.find(self._parent[i])
            i = self._parent[i]
        return i

    def union(self, i, j):
        i_id = self.find(i)
        j_id = self.find(j)
        if i_id == j_id:
            return
        if self._rank[i_id] > self._rank[j_id]:
            self._parent[j_id] = i_id
        else:
            self._parent[i_id] = j_id
            if self._rank[i_id] == self._rank[j_id]:
                self._rank[j_id] += 1


class Solution:
    def findRedundantConnection(self, edges):
        extra_edges = []
        dset = DisjointSet()
        for edge in edges:
            u, v = edge
            dset.make_set(u)
            dset.make_set(v)
        for edge in edges:
            u, v = edge
            if dset.find(u) != dset.find(v):
                dset.union(u, v)
            else:
                extra_edges.append(edge)

        return extra_edges.pop()


# sol = Solution()
# print(sol.findRedundantConnection([[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]))
