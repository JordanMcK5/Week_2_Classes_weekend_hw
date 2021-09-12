class Guest:
    def __init__(self, guest_name, cash):
        self.guest_name = guest_name
        self.cash = cash

    def pay_entry_fee(self, entry_fee):
        self.cash -= entry_fee.entry_fee
