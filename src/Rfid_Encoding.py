
def draw(encoded):

    ZERO = "▁"
    ONE = "━"
    LOW = "┓" 
    HIGE = "┏"
    SEPARE = "|"

    decoded = [[], [], [], []]

    if encoded[0] == 0:

        decoded[0].append(SEPARE)
        decoded[0].append(ZERO)
        decoded[0].append(ZERO)
        decoded[0].append(SEPARE)

        decoded[1].append(SEPARE)
        decoded[1].append(ZERO)
        decoded[1].append(ZERO)
        decoded[1].append(SEPARE)

        decoded[2].append(SEPARE)
        decoded[2].append(ZERO)
        decoded[2].append(ONE)
        decoded[2].append(SEPARE)

        decoded[3].append(SEPARE)
        decoded[3].append(ONE)
        decoded[3].append(SEPARE)

    else:
        
        decoded[0].append(SEPARE)
        decoded[0].append(ONE)
        decoded[0].append(ZERO)
        decoded[0].append(SEPARE)

        decoded[1].append(SEPARE)
        decoded[1].append(ONE)
        decoded[1].append(ONE)
        decoded[1].append(SEPARE)

        decoded[2].append(SEPARE)
        decoded[2].append(ONE)
        decoded[2].append(ZERO)
        decoded[2].append(SEPARE)

        decoded[3].append(SEPARE)
        decoded[3].append(ZERO)
        decoded[3].append(ONE)
        decoded[3].append(SEPARE)

    i = 1
    paralleli = 4

    while i < len(encoded):

        if encoded[i] == 0:

            decoded[0].append(ZERO)
            decoded[0].append(ZERO)
            decoded[0].append(SEPARE)

            decoded[1].append(ZERO)
            decoded[1].append(ZERO)
            decoded[1].append(SEPARE)
                
            decoded[2].append(ZERO)
            decoded[2].append(ONE)
            decoded[2].append(SEPARE)
                
            if decoded[3][paralleli-2] == ONE:


                if encoded[i-1] == 1:
    
                    decoded[3].append(ONE)
                    decoded[3].append(ONE)
                    decoded[3].append(SEPARE)

                else:

                    decoded[3].append(ZERO)
                    decoded[3].append(ZERO)
                    decoded[3].append(SEPARE)
                    
            else:

                if encoded[i-1] == 1:
                    
                    decoded[3].append(ZERO)
                    decoded[3].append(ZERO)
                    decoded[3].append(SEPARE)

                else:
                    
                    decoded[3].append(ONE)
                    decoded[3].append(ONE)
                    decoded[3].append(SEPARE)
                
                
        else:
            
            decoded[0].append(ONE)
            decoded[0].append(ZERO)
            decoded[0].append(SEPARE)
            
            decoded[1].append(ONE)
            decoded[1].append(ONE)
            decoded[1].append(SEPARE)

            decoded[2].append(ONE)
            decoded[2].append(ZERO)
            decoded[2].append(SEPARE)
               

            if decoded[3][paralleli-2] == ONE:
                    
                decoded[3].append(ONE)
                decoded[3].append(ZERO)
                decoded[3].append(SEPARE)
                    
            else:
                    
                decoded[3].append(ZERO)
                decoded[3].append(ONE)
                decoded[3].append(SEPARE)
                
            
        
        i += 1
        paralleli += 3


    i = 0

    
    for x in decoded:
        
        if i == 0:
            
            print("RZ: ", end="")
            
        elif i == 1:
            
            print("NRZ: ", end="")
            
        elif i == 2:
            
            print("Manchester: ", end="")
            
        elif i == 3:
            
            print("Miller: ", end="")

        for y in x:

            print(f"{y}", end="")

        print("\n")
        
        i += 1
