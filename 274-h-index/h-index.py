class Solution(object):
    def hIndex(self, citations):
        n = len(citations)

        count = [0] * (n + 1)

        for c in citations:
            count[min(c, n)] += 1

        papers = 0

        for h in range(n, 0, -1):
            papers += count[h]

            if papers >= h:
                return h

        return 0