class Solution:
    def game(self, disk, source, middle, destination):
        if disk == 1:
            print(f"Disk {disk} from {source} to {destination}")
            return
        
        self.game(disk - 1, source, destination, middle)
        print(f"Disk {disk} from {source} to {destination}")
        self.game(disk - 1, middle, source, destination)

sol = Solution()
sol.game(4, "A", "B", "C")

