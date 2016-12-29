import re

def seperate_expression(expression):
        #We just convert our expression to it's parts and return it as a list.
	return re.findall(r'\d+\.\d+|\d+|[\+\*\-\/]', expression)




def calculate(expression):
    
	num_sym_list=seperate_expression(expression)
        
	#Solve our expresion by multiplication
	result_list=solve_exp_by_mark("*",num_sym_list);

        #Solve our expression by Division
	result_list=solve_exp_by_mark("/",result_list);

        #Solve our expression by Subtraction
	result_list=solve_exp_by_mark("-",result_list);

	#Solve our expression by Addition
	result_list=solve_exp_by_mark("+",result_list);

        
	#In this point there is only one item in the list  and that is the result of expression,
	#So  we pop it from list
	print(result_list)
	
	
def solve_exp_by_mark(mark,expression_list):
	length=len(expression_list)
	for i in range(length):
		if expression_list[i]==mark:
			if mark=="*":
				expression_list[i]=float(expression_list[i-1])*float(expression_list[i+1])
			elif mark=="/":
				expression_list[i]=float(expression_list[i-1])/float(expression_list[i+1])
			elif mark=="-":
				expression_list[i]=float(expression_list[i-1])-float(expression_list[i+1])
			else:
				expression_list[i]=float(expression_list[i-1])+float(expression_list[i+1])

			#we assign del to those list items which have been solved and later will be deleted.	
			expression_list[i-1]='del'
			expression_list[i+1]=expression_list[i]
			expression_list[i]='del'
			
	i=0
	while i<len(expression_list):
		if expression_list[i]=='del':
			expression_list.remove(expression_list[i])
			i=i-1
		i=i+1
	

	return expression_list
        
	

        
	



def take_user_expression():
        while True:
                expression=input("Type an expression to solve for you , or type q to quit  : ")
                expression=expression.strip(" ")
                if expression=="q":
                        break
                # Here we only check the reqularity of our expression to prevent any kind of exception,
                elif re.findall(r'[A-Za-z_][\+\-\*\/]\D*|\D+\D|^[\*\/]|[\-\+\*\/]$|\w*_\w*',expression):
                        print("Your expressin was not valid. ")
                        continue
                #Here we check pattern which starts with - or + , because I was not able to solve such expression.
                elif re.match(r'^[\+\-]\d+',expression):
                        expression='0'+expression
                        calculate(expression)
                else:
                        calculate(expression)

        

#Run our program from this point
take_user_expression()

