from Rfid_Encoding import draw



with open("input.txt", "r") as file:
    
    times = int(file.readline())
    
    i = 0
    
    while i < times:
        
        encoded = []
        
        str = file.readline();
        
        for x in str:
           
           if x != "\n": 
               
                encoded.append(int(x))
            
        print(f"#####{i+1}#####")

        for x in encoded:

            print(x, end="")

        print("\n")
        draw(encoded)
    
        i += 1
