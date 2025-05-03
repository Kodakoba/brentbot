
class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read_numbers_from_file(self, filepath):
        numbers_l = []
        with open(filepath, "r") as file:
            for line in file:
                # Remove leading/trailing whitespace and split the line into numbers
                nums = line.strip().split()
                for num in nums:
                    try:
                        numbers_l.append(int(num))  # Try converting to integer
                    except ValueError:
                        try:
                            numbers_l.append(float(num))  # If not integer, try float
                        except ValueError:
                            print(f"Invalid input: {num} on line: {line.strip()}")

        return numbers_l