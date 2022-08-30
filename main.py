import numpy as np
from tabulate import tabulate


class ipl_match():
    
    def table_data(self):

        # using numpy we stored the data as an array into variable "a"
        a = np.array(
            [
                ["Team", "Points","Match 5","Match 4","Match 3","Match 2","Match 1"],
                ["GT",	20,	"Win",	"Win",	"Loss",	"Loss",	"Win"],
                ["LSG",	18,	"Win",	"Loss",	"Loss",	"Win",	"Win"],
                ["RR",	16,	"Win",	"Loss",	"Win",	"Loss",	"Loss"],
                ["DC",	14,	"Win",	"Win",	"Loss",	"Win",	"Loss"],
                ["RCB",	14,	"Loss",	"Win",	"Win",	"Loss",	"Loss"],
                ["KKR",	12,	"Loss",	"Win",	"Win",	"Loss",	"Win"],
                ["PBKS",12,	"Loss",	"Win",	"Loss",	"Win",	"Loss"],
                ["SRH",	12,	"Win", "Loss",	"Loss",	"Loss",	"Loss"],
                ["CSK",	8,	"Loss",	"Loss",	"Win",	"Loss",	"Win"],
                ["MI",	6,	"Loss",	"Win",	"Loss",	"Win",	"Win"]
            ]
        )

        # Here we return the table data
        return a


    def table_output(self):
        # This method is used to display the table data

        # Table_data() method is stored to a local variable "a"
        a = self.table_data()
        
        # display the table data in Tabulate format
        # For this output representation we have imported Tabulate modulu
        print(tabulate(a, tablefmt="grid", headers='firstrow'))


    def consecutive_loss(self):

        # This method is to get the list of Teams which have consecutive loss

        a = self.table_data()
        # Table_data() method is stored to a local variable "a"

        arr=[] # An empty list is created 

        rows = len(a)   # Here we store the length of the rows in a variable i.e 11
        
        cols = len(a[0])    # Here we store the length of the columns in a variable i.e 7

        for i in range(rows-1):
            # Loop for the row traversing

            for j in range(cols-1):
                # Loop for column traversing

                if (a[i][j] == a[i][j+1] == "Loss"):
                    # The condition here is to check for 2 consecutive Loss

                    if a[i][0] not in arr:
                        # The above "IF" conditions is used to avoid duplication 
                        # of the team name when 3 consecutive loss occurs 

                        arr.append(a[i][0])
                        # Here the Team names are appended into the empty list i.e arr[]

        print(arr)
        # We print the final output
        #i.e the Team names which has 2 consecutive loss


    def n_loss_win_points(self):

        # This method is to Generalize the above same solution, so that we could get teams 
        # that have n consecutive losses/wins.

        my_list = self.table_data()
        # table data is stored to a variable 
        
        val = input("Enter Loss/Win match: ")
        # "Val" is a variable where we take input from user to get the Win or Loss match results

        n = int(input("Enter required consecutive wins/losses:"))
        # "n" variables takes the number of consecutive wins or loss
        
        arr=[]  # Empty list created

        rows = len(my_list) # "rows" variable store the lenth of the rows of the table

        cols = len(my_list[0]) # "cols" variable store the lenth of the columns of the table

        sum_of_points = 0 # Initiating the points to zero 

        for i in range(rows):
            # Loop for rows travesring
            count = 0

            for j in range(cols):
                # Loop for column traversing

                if val.lower()=="loss":
                    # Checks if the input user data is "LOSS"

                    if (j < cols):

                        if n <= 5 and count <= n:
                            # Here the total matchs from the table is 5
                            # so the input data from user should not exceed 5

                            if(my_list[i][j]=="Loss"):
                                # We check for Loss

                                count += 1

                                if count == n:

                                    arr.append(my_list[i][0])
                                    # [i][0] Stores the Team name & we append the name in to the list
                                    # where i values increases i.e row value

                                    sum_of_points = sum_of_points + int(my_list[i][1])
                                    # Sum of the points will be updated for loss 

                            else:
                                # The below line return "0" if no 'n' consecutive wins or loss from the team
                                count = 0

            if val.lower() == "win":
                # Checks if the input user data is "WIN"
                
                if (j < cols):

                    if n <= 5 and count <= n:
                        # Here the total match's from the table is 5
                        # so the input data from user should not exceed 5

                        if(my_list[i][j] == "Win"):
                            # We check for win

                            count += 1

                            if count == n:

                                arr.append(my_list[i][0])
                                # [i][0] Stores the Team name & we append the name in to the list
                                # where i values increases i.e row value

                                sum_of_points = sum_of_points + int(my_list[i][1])
                                # Sum of the points will be updated

                        else:

                            count = 0

        print("Team Names are : ", arr)
        print("Avg points are : ", sum_of_points/len(arr))

        

s_obj = ipl_match()
s_obj.table_output()
print("*"*25)
s_obj.consecutive_loss()
print("*"*25)
s_obj.n_loss_win_points()

