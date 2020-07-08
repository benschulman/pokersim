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
        hand_1 = ['3S', '3H', '4C', '5D', '6S']
        assert not Hand._isStraight(hand_1)

        hand_2 = ['7H', '8H', '9C', 'TD', 'JS']
        assert Hand._isStraight(hand_2)

        hand_3 = ['2H', '3H', '4C', '5D', 'AS']
        assert Hand._isStraight(hand_3)

        hand_4 = ['TC', 'JC', 'QS', 'KS', 'AS']
        assert Hand._isStraight(hand_4)

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

    def test_isFullHouse(self):
        """
        Tests the isFullHouse method in the Hand class
        """
        hand_1 = ['4H', '5S', 'AC', 'AD', 'AH']
        assert not Hand._isFullHouse(hand_1)
        
        hand_2 = ['4H', '4S', '4C', 'AD', 'AS']
        assert Hand._isFullHouse(hand_2)

        hand_3 = ['QC', 'QD', 'QH', 'KC', 'KD']
        assert Hand._isFullHouse(hand_3)
    
    def test_isThreeOfAKind(self):
        """
        Tests the isThreeOfAKind method in the Hand class
        """
        hand_1 = ['4H', 'KS', 'AC', 'AD', 'AH']
        assert Hand._isThreeOfAKind(hand_1)
        
        hand_2 = ['4H', '4S', '5C', '5D', 'AS']
        assert not Hand._isThreeOfAKind(hand_2)

        hand_3 = ['QC', 'QD', 'QH', 'KC', 'AD']
        assert Hand._isThreeOfAKind(hand_3)

        hand_4 = ['JC', 'QD', 'QH', 'QC', 'KD']
        assert Hand._isThreeOfAKind(hand_4)

    def test_isTwoPair(self):
        """
        Tests the isTwoPair method in the Hand class
        """
        hand_1 = ['4H', 'KS', 'KC', 'AD', 'AH']
        assert Hand._isTwoPair(hand_1)
        
        hand_2 = ['4H', '4S', '5C', '6D', 'AS']
        assert not Hand._isTwoPair(hand_2)

        hand_3 = ['QC', 'QD', 'KH', 'KC', 'AD']
        assert Hand._isTwoPair(hand_3)

        hand_4 = ['JC', 'JD', 'QH', 'KC', 'AD']
        assert not Hand._isTwoPair(hand_4)
    
    def test_isPair(self):
        """
        Tests the isPair method in the Hand class
        """
        hand_1 = ['4H', '4S', 'QC', 'KD', 'AH']
        assert Hand._isPair(hand_1)
        
        hand_2 = ['4H', '5S', '6C', '7D', 'AS']
        assert not Hand._isPair(hand_2)

        hand_3 = ['JC', 'QD', 'KH', 'KC', 'AD']
        assert Hand._isPair(hand_3)

        hand_4 = ['TC', 'JD', 'QH', 'AC', 'AD']
        assert Hand._isPair(hand_4)


if __name__ == "__main__":
    unittest.main()