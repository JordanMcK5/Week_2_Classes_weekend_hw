class Room:
    def __init__(self, name, capacity, till, entry_fee):
        self.name = name
        self.capacity = capacity
        self.till = till
        self.entry_fee = entry_fee
        self.guest = []
        self.song = []


    def song_count(self):
        return len(self.song)
    
    def guest_count(self):
        return len(self.guest)
    
    def check_in(self, customer_to_enter):
        if self.guest_count() == self.capacity:
            return
        self.guest.append(customer_to_enter)
        if self.guest_count() > self.capacity:
            print ("Not tonight, pal")

    def check_out(self, customer_to_leave):
        self.guest.remove(customer_to_leave)

    def empty(self):
        self.guest.clear()
    
    def add_song(self, song):
        self.song.append(song)

    def till_amount(self):
        return len(self.till)