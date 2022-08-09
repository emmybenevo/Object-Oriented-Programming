# building a class called investment that can calculate 
# compound interest. formular is principal(1 + interest)**years

class Investment:

    def __init__(self,principal,interest):
        self._principal =principal
        self._interest=interest

    def value_after(self,years):
        val =self._principal*(self._interest + 1)**years
        return val

    def __str__(self): 
        return 'Principal: ${}, interest rate: {}%'.format(self._principal,self._interest*100)



if __name__ =="__main__":
    invest =Investment(100,0.05)
    comp_int = invest.value_after(5)
    print(f'the elements are: {invest}')
    print(f'the compound interest is ${comp_int}')
