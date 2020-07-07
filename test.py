import unittest
from src.game import Hand

class TestHand(unittest.TestCase):
    def test_isFlush(self):
        """
        Tests the isFlush method in the Hand class
        """
        hand_1 = ['2H', '5H', '6H', '7H', '8H']
        assert Hand._isFlush(hand_1)

        hand_2 = ['2H', '3H', '4H', '5H', '6D']
        assert not Hand._isFlush(hand_2)

        hand_3 = ['TD', 'JC', 'JD', 'QD', 'KD']
        assert not Hand._isFlush(hand_3)
    
    def test_isStraight(self):
        """
        Tests the isStraight method in the Hand class
        """
        hand_1 = ['2H', '3H', '4C', '5D', '6S']
        assert Hand._isStraight(hand_1)

        hand_2 = ['7H', '8H', '9C', 'TD', 'JS']
        assert Hand._isStraight(hand_1)

        hand_3 = ['2H', '3H', '4C', '5D', 'AS']
        assert Hand._isStraight(hand_2)

        hand_4 = ['TC', 'JC', 'QS', 'KS', 'AS']
        assert Hand._isStraight(hand_3)

    def test_isFourOfAKind(self):
        """
        Tests the isFourOfAKind method in the Hand class
        """
        hand_1 = ['4H', 'AS', 'AC', 'AD', 'AH']
        assert Hand._isFourOfAKind(hand_1)
        
        hand_2 = ['4H', '4S', '4C', '4D', 'AS']
        assert Hand._isFourOfAKind(hand_2)

        hand_3 = ['QC', 'QD', 'QH', 'KC', 'KD']
        assert not Hand._isFourOfAKind(hand_3)



if __name__ == "__main__":
    unittest.main()