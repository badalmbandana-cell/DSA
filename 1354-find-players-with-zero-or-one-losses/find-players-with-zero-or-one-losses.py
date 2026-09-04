class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set()
        oneloss=set()
        multiloss=set()
        for winner,looser in matches:
            players.add(winner)
            players.add(looser)
            if looser not in oneloss and looser not in multiloss:
                oneloss.add(looser)
            elif looser in oneloss:
                oneloss.remove(looser)
                multiloss.add(looser)
        noloss=players-oneloss-multiloss
        return [sorted(noloss),sorted(oneloss)]            
        