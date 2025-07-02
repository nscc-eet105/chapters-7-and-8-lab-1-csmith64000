#Chris smith
#Chapter 7&8 Lab
#07/01/2025
def main():


    try:
    
        File_Name = input("Enter the name of your file: ")
        mode = input("Are you going to (r)ead or (w)rite this file? ")

        if mode == 'w':
            First_name = input("Enter the first name: ")

            Last_name = input("Enter the last name: ")

            Street_Adress = str(input("Enter the street adress: "))

            City = input("Enter the city : ")

            State_name = input("Enter the state: ")

            Zip_Code = input("Enter the zip code: ")


            File = open(File_Name, 'w')
            All_Info =(
                First_name + " " + Last_name + "\n" +
                Street_Adress + "\n" +
                City + "," + State_name + " " + Zip_Code
                )
            File.write(All_Info)
        


        
            File.close()


        elif mode == 'r':
            file =  open(File_Name, 'r')
            Contents = file.read()
            print("The contents of the file are: ")
            print(Contents)
            file.close()
            

        else:
            print("Error, Please enter 'w' or 'r'")


    except IOError:
        print(' An error occured please try again')
                
  


if __name__ == '__main__':
    main()
    
    
    

