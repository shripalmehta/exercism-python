class Matrix:
    def __init__(self, matrix_string):
        self.matrix = matrix_string
        self.rows = matrix_string.split('\n')

    def row(self, index):
        try:
            extracted_row = self.rows[index-1].split()
            extracted_row = list(map(int, extracted_row))
            return extracted_row
        except:
            print(f"Exception while getting row {index}")

    def column(self, index):
        try: 
            col = []
            for row in self.rows:
                col.append(int(row.split()[index-1]))
            return col
        except (Exception):
            print(f"Exception while getting column {index}")
