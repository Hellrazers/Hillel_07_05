



class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def __del__(self):
        pass

    def __str__(self):
        return f'{self.make} {self.model}'





class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = open(filename, mode)
        # self.file = None

    def read_data(self):
        return self.file.read()

    def write_data(self, some_text):
        self.file.write(some_text)
    # def __del__(self):
    #     self.file.close()
    #     print(f"File {self.filename} has been closed.")

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self

    def file_close(self):
        self.file.close()
        self.file = None
        print('file_close закриває файл')
    # def __exit__(self, exc_type, exc_val, exc_tb):

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print('Прогрма закриває файл')
        else:
            print('ФАйл не існує')




file_1 = FileHandler('car1.txt', 'w')
file_2 = FileHandler('car1.txt', 'r')
print(file_2.read_data())
file_1.write_data('Hello world')
#
# with FileHandler('car1.txt', 'r') as file:
#     print(file.read_data())
#     file.file_close()


# with open('car1.txt', 'r') as file:
#     print(file.read())

# car_1 = Car('Ford', 'Mustang')
# print(car_1.make)
# with open('test.txt', 'r') as f:
#     f = f.read()
#     print(car_1)
#     del f
#
#
# car_1.__del__ # del car_1
#
# # print("Done")
# # print(car_1)
#
# car_1.model = 'Mustang'