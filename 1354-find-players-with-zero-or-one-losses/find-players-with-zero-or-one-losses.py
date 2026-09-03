class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players=set()
        one_loss=set()
        multiple_loss=set()
        for winner,looser in matches:
            players.add(winner)
            players.add(looser)
            if looser not in one_loss and looser not in multiple_loss:
                one_loss.add(looser)
            elif looser in one_loss:
                one_loss.remove(looser)
                multiple_loss.add(looser)
        zero_loss=players-one_loss-multiple_loss
        return [sorted(zero_loss),sorted(one_loss)]            

        