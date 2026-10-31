# MATCH CASE STATEMENTS::
day = "thursday"
match day:
    case "monday":
        print("START WORKING BRO")
    case "tuesday" | "wednesday" | "thursday" | "friday":
        print("working day")
    case "saturday" | "sunday":
        print("its a weekend bro")
    case _:
        print("other day")

# example 2
num = int(input("ENTER A NUMBER:"))
match num:  # syntax is ---        match variable                                      #case variable value
    case 1:  # here 1 is num                                        #print("somethingg")
        print("one ")
    case 2:
        print("two")
    case 3:
        print("threee")
    case 4:
        print("four")
    case _:
        print("other number ")
