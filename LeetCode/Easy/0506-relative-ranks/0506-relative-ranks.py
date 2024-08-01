class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sorted_scores = sorted(range(len(score)), key=lambda k: score[k], reverse=True)
        result = ['']*len(score)

        for i in range(len(score)):
            if i == 0:
                result[sorted_scores[i]] = 'Gold Medal'
            elif i == 1:
                result[sorted_scores[i]] = 'Silver Medal'
            elif i == 2:
                result[sorted_scores[i]] = 'Bronze Medal'
            else:
                result[sorted_scores[i]] = str(i+1)
        return result