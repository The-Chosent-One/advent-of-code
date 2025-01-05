with open("input.txt", "r") as file:
    disk = [int(c) for c in file.read()]

class diskParser:
    def __init__(self, disk: list[int]):
        self.disk = disk.copy()
        self.disk_mem = []
        self.disk_index = 0
        self.processing_index = 0
        self.moving_index = len(disk) - 1
        self.part1 = self.part2 = 0
    
    @property
    def current_num(self):
        return self.disk[self.processing_index]
    
    @property
    def files_to_move(self):
        return self.disk[self.moving_index]

    def calculate_checksum(self, number_of_files: int, index: int, part2=False) -> None:
        id = index // 2
        result = sum(id * i for i in range(self.disk_index, self.disk_index + number_of_files))
        if part2:
            self.part2 += result
        else:
            self.part1 += result
        
        self.disk_index += number_of_files
    
    def find_index_to_swap(self, section: str, back_index: int) -> int | None:
        spaces = len(section)
        for index, memory_section in enumerate(self.disk_mem[:back_index]):
            empty = memory_section.count(".")
            if empty == 0:
                continue

            if empty >= spaces:
                return index
        
        return

    def parse_part1(self):
        while self.processing_index <= self.moving_index:
            if self.processing_index % 2 == 0:
                self.calculate_checksum(self.current_num, self.processing_index)
                self.processing_index += 1
            
            # can move all the files to current num and have leftover
            elif self.current_num >= self.files_to_move:
                self.calculate_checksum(self.files_to_move, self.moving_index)
                self.disk[self.processing_index] -= self.files_to_move
                self.moving_index -= 2
            
            # still have files left over to be able to move
            else:
                self.calculate_checksum(self.current_num, self.moving_index)
                self.disk[self.moving_index] -= self.current_num
                self.processing_index += 1
        
        return self.part1

    def parse_part2(self):
        for index, count in enumerate(self.disk):
            if index % 2 == 0:
                self.disk_mem.append([str(index // 2)] * count)
            else:
                self.disk_mem.append(["."] * count)
        

        for index in range(len(self.disk_mem)-1, 0, -2):
            section = self.disk_mem[index]
            index_to_swap = self.find_index_to_swap(section, index)

            if index_to_swap is None:
                continue

            # contiguous_space is the empty area we will be trying to fill (from front of array)
            contiguous_space = self.disk_mem[index_to_swap]
            start_replacing = contiguous_space.index(".")
            contiguous_space[start_replacing: start_replacing + len(section)] = section
            # this does the swap from the file and the empty spaces from the front
            self.disk_mem[index_to_swap] = contiguous_space
            self.disk_mem[index] = len(section) * ["."]

        self.disk_mem = [[0 if c == "." else int(c) for c in l] for l in self.disk_mem]
        final_mem = []
        for l in self.disk_mem:
            final_mem.extend(l)
        
        self.part2 = sum(index * id for index, id in enumerate(final_mem))

        return self.part2


print(f"Part 1: {diskParser(disk).parse_part1()}")
print(f"Part 2: {diskParser(disk).parse_part2()}")
