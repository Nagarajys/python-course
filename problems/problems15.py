# problems : 15 remove duplicate and sort for understanding purpose
def remove_dup_sort(numbers):
    unique = [ 4,2,7,9,1] ##ಒಂದು ಖಾಲಿ list create ಮಾಡಿ
    
    # when they asked to duplicate

    for num in numbers: ##ಪ್ರತಿಯೊಂದು element ಅನ್ನು check ಮಾಡಿ
        if num not in unique:##Duplicate ಇಲ್ಲದಿದ್ದರೆ add ಮಾಡಿ both 2 lines
            unique.append(num)
            
    ## when they asked to sort

    for i in range(len(unique)):#i ಒಂದೊಂದು index ಅನ್ನು ಹಿಡಿಯುತ್ತದೆ.
        for j in range(i + 1, len(unique)):#j ಯಾವಾಗಲೂ i ನಂತರದ elements ಅನ್ನು check ಮಾಡುತ್ತದೆ.
         
            if unique[i] > unique[j]:
                unique[i], unique[j] = unique[j], unique[i] ## yalladru i > j agidre adhun swap madi j first amel i hakok heodhu , for example list alii 4 ,2 edhre 4 i agirutte and 2j agirutte avaga 4> 2 alvva adhike asending order alli beku adhie j first barutte amel i bartte ,ondh vele i ayy small agithu andre swap agalla

    return unique ## used to send output outside
#i = ಈಗ ನಾವು ನೋಡುತ್ತಿರುವ number
#j = ಅದರ ನಂತರದ numbers
# i>j ಆಗಿದ್ದರೆ swap
print(remove_dup_sort([4,2,7,9,1]))
