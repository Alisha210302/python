class bank_interest_calculator:
    __interest_rate = 8.6
    __interest_rate_senior_citizen = 8.4
    def __init__(self,p_amount,duration,senior_citizen=0):
        self.p_amount = p_amount
        self.duration = duration
        self.senior_citizen = senior_citizen

    def simple_interest_calculator(self):
        if self.senior_citizen==1:
            print(f"Simple interest for senior citizens is {(self.p_amount * self.duration * bank_interest_calculator.__interest_rate_senior_citizen)/100}")
        else:
            print(f"Simple interest is {(self.p_amount * self.duration * self.__interest_rate)/100}")

    # def equated_monthly_installment(self):
    #     if self.senior_citizen == 1:
    #         print(f"Equated monthly installment is:{(self.p_amount*self.__interest_rate_senior_citizen*(1+self.__interest_rate_senior_citizen)^self.duration)/((1+self.__interest_rate_senior_citizenself.duration-1))}")
    #     else:
    #         print(f"Equated monthly installment is:{(self.p_amount*self.__interest_rate*(1+self.__interest_rate)^self.duration)/((1+self.__interest_rate^self.duration-1))}")

c1 = bank_interest_calculator(1000,2,0)
c1.simple_interest_calculator()
c2 = bank_interest_calculator(2000,1,1)
c2.simple_interest_calculator()
