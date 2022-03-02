## Yahav Shalom
## 207650052

#QA 1
def my_func(x1, x2, x3):
    if type(x1) != float or type(x2) != float or type(x3) != float:
        return "Error: parameters should be float"
    numerator = ((x1+x2+x3)*(x2+x3)*x3)
    denomi = (x1+x2+x3)
    if denomi == 0:
        return "Not a number – denominator equals zero"
    else:
        return float(numerator/denomi)


#QA 2 
#I didn't check if the input is String (not required)
def convert(hours = 0, minutes = 0):
    if hours < 0 or minutes < 0 :
        return "Input error!"
    hours = hours * 3600
    minutes = minutes * 60
    solu = hours + minutes
    return int(solu)
    
