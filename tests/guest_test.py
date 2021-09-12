import unittest
from src.guest import Guest
from src.room import Room
from src.song import Song

class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Katy", 20)

    def test_guest_has_name(self): 
        self.assertEqual("Katy", self.guest.guest_name) 

    def test_guest_has_cash(self): 
        self.assertEqual(20, self.guest.cash)
        
    def test_guest_pays_entry_fee(self):
        entry_fee = Room("lounge", 8, 100, 5)
        self.guest.pay_entry_fee(entry_fee)
        self.assertEqual(15, self.guest.cash)        