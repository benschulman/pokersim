import unittest
import src
import src.pokertools as pt

class TestHand(unittest.TestCase):
    def test_isFlush(self):
        """
        Tests the isFlush method in the Hand class
        """
        hand_1 = ['2H', '5H', '6H', '7H', '8H']
        assert pt.Hand._isFlush(hand_1)[0]
        assert pt.Hand._isFlush(hand_1)[1] == [6,5,4,3,0]

        hand_2 = ['2H', '3H', '4H', '5H', '6D']
        assert not pt.Hand._isFlush(hand_2)[0]
        assert pt.Hand._isFlush(hand_2)[1] == [1,1,1,1,1]

        hand_3 = ['TD', 'JC', 'JD', 'QD', 'KD']
        assert not pt.Hand._isFlush(hand_3)[0]
        assert pt.Hand._isFlush(hand_3)[1] == [1,1,1,1,1]
    
    def test_isStraight(self):
        """
        Tests the isStraight method in the Hand class
        """
        hand_1 = ['3S', '3H', '4C', '5D', '6S']
        assert not pt.Hand._isStraight(hand_1)[0]
        assert pt.Hand._isStraight(hand_1)[1] == [1,1,1,1,1]

        hand_2 = ['7H', '8H', '9C', 'TD', 'JS']
        assert pt.Hand._isStraight(hand_2)[0]
        assert pt.Hand._isStraight(hand_2)[1] == [9,8,7,6,5]

        hand_3 = ['2H', '3H', '4C', '5D', 'AS']
        assert pt.Hand._isStraight(hand_3)[0]
        assert pt.Hand._isStraight(hand_3)[1] == [3,2,1,0,-1]

        hand_4 = ['TC', 'JC', 'QS', 'KS', 'AS']
        assert pt.Hand._isStraight(hand_4)[0]
        assert pt.Hand._isStraight(hand_4)[1] == [12,11,10,9,8]

    def test_isFourOfAKind(self):
        """
        Tests the isFourOfAKind method in the Hand class
        """
        hand_1 = ['4H', 'AS', 'AC', 'AD', 'AH']
        assert pt.Hand._isFourOfAKind(hand_1)[0]
        assert pt.Hand._isFourOfAKind(hand_1)[1] == [12,12,12,12,2]
        
        hand_2 = ['4H', '4S', '4C', '4D', 'AS']
        assert pt.Hand._isFourOfAKind(hand_2)[0]
        assert pt.Hand._isFourOfAKind(hand_2)[1] == [2,2,2,2,12]

        hand_3 = ['QC', 'QD', 'QH', 'KC', 'KD']
        assert not pt.Hand._isFourOfAKind(hand_3)[0]
        assert pt.Hand._isFourOfAKind(hand_3)[1] == [1,1,1,1,1]

    def test_isFullHouse(self):
        """
        Tests the isFullHouse method in the Hand class
        """
        hand_1 = ['4H', '5S', 'AC', 'AD', 'AH']
        assert not pt.Hand._isFullHouse(hand_1)[0]
        assert pt.Hand._isFullHouse(hand_1)[1] == [1,1,1,1,1]
        
        hand_2 = ['4H', '4S', '4C', 'AD', 'AS']
        assert pt.Hand._isFullHouse(hand_2)[0]
        assert pt.Hand._isFullHouse(hand_2)[1] == [2,2,2,12,12]

        hand_3 = ['QC', 'QD', 'QH', 'KC', 'KD']
        assert pt.Hand._isFullHouse(hand_3)[0]
        assert pt.Hand._isFullHouse(hand_3)[1] == [10,10,10,11,11]
    
    def test_isThreeOfAKind(self):
        """
        Tests the isThreeOfAKind method in the Hand class
        """
        hand_1 = ['4H', 'KS', 'AC', 'AD', 'AH']
        assert pt.Hand._isThreeOfAKind(hand_1)[0]
        assert pt.Hand._isThreeOfAKind(hand_1)[1] == [12,12,12,11,2]
        
        hand_2 = ['4H', '4S', '5C', '5D', 'AS']
        assert not pt.Hand._isThreeOfAKind(hand_2)[0]
        assert pt.Hand._isThreeOfAKind(hand_2)[1] == [1,1,1,1,1]

        hand_3 = ['QC', 'QD', 'QH', 'KC', 'AD']
        assert pt.Hand._isThreeOfAKind(hand_3)[0]
        assert pt.Hand._isThreeOfAKind(hand_3)[1] == [10,10,10,12,11]

        hand_4 = ['JC', 'QD', 'QH', 'QC', 'KD']
        assert pt.Hand._isThreeOfAKind(hand_4)[0]
        assert pt.Hand._isThreeOfAKind(hand_4)[1] == [10,10,10,11,9]

    def test_isTwoPair(self):
        """
        Tests the isTwoPair method in the Hand class
        """
        hand_1 = ['4H', 'KS', 'KC', 'AD', 'AH']
        assert pt.Hand._isTwoPair(hand_1)[0]
        assert pt.Hand._isTwoPair(hand_1)[1] == [12,12,11,11,2]
        
        hand_2 = ['4H', '4S', '5C', '6D', 'AS']
        assert not pt.Hand._isTwoPair(hand_2)[0]
        assert pt.Hand._isTwoPair(hand_2)[1] == [1,1,1,1,1]

        hand_3 = ['QC', 'QD', 'KH', 'KC', 'AD']
        assert pt.Hand._isTwoPair(hand_3)[0]
        assert pt.Hand._isTwoPair(hand_3)[1] == [11,11,10,10,12]

        hand_4 = ['JC', 'JD', 'QH', 'KC', 'AD']
        assert not pt.Hand._isTwoPair(hand_4)[0]
        assert pt.Hand._isTwoPair(hand_4)[1] == [1,1,1,1,1]
    
    def test_isPair(self):
        """
        Tests the isPair method in the Hand class
        """
        hand_1 = ['4H', '4S', 'QC', 'KD', 'AH']
        assert pt.Hand._isPair(hand_1)[0]
        assert pt.Hand._isPair(hand_1)[1] == [2,2,12,11,10]
        
        hand_2 = ['4H', '5S', '6C', '7D', 'AS']
        assert not pt.Hand._isPair(hand_2)[0]
        assert pt.Hand._isPair(hand_2)[1] == [1,1,1,1,1]

        hand_3 = ['JC', 'QD', 'KH', 'KC', 'AD']
        assert pt.Hand._isPair(hand_3)[0]
        assert pt.Hand._isPair(hand_3)[1] == [11,11,12,10,9]

        hand_4 = ['TC', 'JD', 'QH', 'AC', 'AD']
        assert pt.Hand._isPair(hand_4)[0]
        assert pt.Hand._isPair(hand_4)[1] == [12,12,10,9,8]


if __name__ == "__main__":
    unittest.main()