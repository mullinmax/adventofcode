class elf():
    def __init__(self, inventory:str):
        self.snacks = [int(i) for i in inventory.split('\n')]
    
    def __str__(self):
        return str(self.snacks)

    def total_calories(self):
        return sum(self.snacks)


with open('data.txt') as f:
    raw_text = f.read()
    elves = [elf(inventory) for inventory in raw_text.split('\n\n')]
    elves.sort(key=lambda x:x.total_calories())


print(elves[-1].total_calories())
print(sum([e.total_calories() for e in elves[-3:]]))

