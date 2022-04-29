"""
Welcome to my test of the kaprekars constant.

I will take suitable numbers and apply the algorithm to see if I get the kaprekars constant.
"""

class KaprekarsConstantTest:
    def __init__(self, detail):
        self.step = 0
        self.detail = detail

    def main(self, number):

        if self.valid(number) == False:

            return False

        listAscending = []
        numberAscending = ""
        listDescending = []
        numberDescending = ""
        result = 0

        for i in range(len(str(number))):
            listAscending.append(str(number)[i])
            listDescending.append(str(number)[i])

        listAscending.sort()
        listDescending.sort(reverse=True)

        for i in listAscending:
            numberAscending = numberAscending + i
        numberAscending = int(numberAscending)

        for i in listDescending:
            numberDescending = numberDescending + i
        numberDescending = int(numberDescending)

        result = numberDescending - numberAscending


        if self.detail:
            print(f"""
Step              : {self.step}
Starting Number   : {number}
Number Descending : {numberDescending}
Number Ascending  : {numberAscending}
Result            : {numberDescending} - {numberAscending} = {result}
""")
        else:
            print()
            print(result)

        if result != 6174:
            self.step = self.step + 1
            self.main(result)
        else:
            print(f"""
-----------------------------
Algorithm Finished !
Total Steps : {self.step}
We have achieved the Kaprekars Constant !
-----------------------------
""")


    def valid(self, number):
        if len(str(number)) != 4:
            print("\n[Error] 4 digit numbers only!")
            return False
        for i in range(4):
            for y in range(4):
                if y == i:
                    continue
                elif int(str(number)[i]) != int(str(number)[y]):
                    return True
        print("\n[Error] There must be 2 or more digits that a different to each other!")
        return False


if __name__ == "__main__":
    num = int(input("Please enter a 4 digit number : "))
    print()
    addInfo = input("Please enter whether or not you want additional info printed out (y/n) : ")
    if addInfo.lower() == "y":
        addInfo = True
    else:
        addInfo = False

    test = KaprekarsConstantTest(addInfo)
    test.main(num)
