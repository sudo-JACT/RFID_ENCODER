
def draw(encoded):

    ZERO = "▁"
    ONE = "━"
    LOW = "┓" 
    HIGE = "┏"

    decoded = [[], [], [], []]

    if encoded[0] == 0:

        decoded[0].append(ZERO)
        decoded[0].append(ZERO)

        decoded[1].append(ZERO)

        decoded[2].append(ZERO)
        decoded[2].append(HIGE)
        decoded[2].append(ONE)

        decoded[3].append(HIGE)
        #decoded[3].append(ONE)

    else:
        
        decoded[0].append(ONE)
        decoded[0].append(LOW)
        decoded[0].append(ZERO)

        decoded[1].append(ONE)

        decoded[2].append(ONE)
        decoded[2].append(LOW)
        decoded[2].append(ZERO)

        decoded[3].append(LOW)
        #decoded[3].append(ZERO)

    i = 1

    while i < len(encoded):

        if encoded[i] == 0:

            decoded[0].append(ZERO)
            decoded[0].append(ZERO)

            if encoded[i-1] == 0:

                decoded[1].append(ZERO)
                
                decoded[2].append(LOW)
                decoded[2].append(ZERO)
                decoded[2].append(HIGE)
                decoded[2].append(ONE)

            else :

                decoded[1].append(LOW)
                decoded[1].append(ZERO)
                
                decoded[2].append(HIGE)
                decoded[2].append(ONE)
                
            if decoded[3][i-1] == HIGE:
                    
                decoded[3].append(ONE)
                decoded[3].append(LOW)
                    
            elif decoded[3][i-1] == LOW:
                    
                decoded[3].append(ZERO)
                decoded[3].append(HIGE)
            
                
                
        else:
            
            decoded[0].append(HIGE)
            decoded[0].append(LOW)
            decoded[0].append(ZERO)
            
            
            if encoded[i-1] == 0:
    
                decoded[1].append(HIGE)
                decoded[1].append(ONE)
                
                decoded[2].append(LOW)
                decoded[2].append(ZERO)

            else :

                decoded[1].append(ONE)
                
                decoded[2].append(HIGE)
                decoded[2].append(LOW)
                decoded[2].append(ZERO)
                
                
            if decoded[3][i-1] == HIGE:
                    
                decoded[3].append(ONE)
                decoded[3].append(LOW)
                    
            elif decoded[3][i-1] == LOW:
                    
                decoded[3].append(ZERO)
                decoded[3].append(HIGE)
                
            
        
        i += 1


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
