class StudentList:
    def __init__(self, size):
        self.students = [None] * size
        self.free_stack = []   # stack to store free indexes
        self.next_index = 0

    def insert(self, name):
        if self.free_stack:
            index = self.free_stack.pop()
            self.students[index] = name
            print(f"{name} inserted at reused index {index}")
        else:
            if self.next_index >= len(self.students):
                print("List is full!")
                return
            self.students[self.next_index] = name
            print(f"{name} inserted at index {self.next_index}")
            self.next_index += 1

    def delete(self, index):
        if 0 <= index < len(self.students) and self.students[index] is not None:
            print(f"{self.students[index]} deleted from index {index}")
            self.students[index] = None
            self.free_stack.append(index)
        else:
            print("Invalid delete operation")

    def display(self):
        print("Student List:", self.students)

s = StudentList(5)

s.insert("Ananjay")
s.insert("Hisham")
s.insert("Mani")
s.display()

s.display()

s.insert("Madhav")
s.display()

s.insert("Aadil")
s.display()

s.delete(2)
s.display()