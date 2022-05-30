import math

logo = """           
 ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     ` Y8 88P'   "Y8  
8b          ,adPPPPP88  8PP\\"\"\"\"\"\"   `"Y8ba,  , adPPPPP88  88          
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88          
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88   
            
                             88                                 
            88               88                                 
            ""               88                                 
 ,adPPYba,  88  8b,dPPYba,   88,dPPYba,    ,adPPYba,  8b,dPPYba,  
a8"     ""  88  88P'    "8a  88P'    "8a  a8P_____88  88P'   "Y8  
8b          88  88       d8  88       88  8PP"""""""  88          
"8a,   ,aa  88  88b,   ,a8"  88       88  "8b,   ,aa  88          
 `"Ybbd8"'  88  88`YbbdP"'   88       88   `"Ybbd8"'  88          
                88                                             
                88           
"""

print(logo)

while True:
  choice = input("Enter 'encode' to Encode a string and 'decode' to Decode a string !!\n")

  if(choice == "encode"):
    shift = int(input("Enter number of shift required\n"))
    shift = shift%26
    inputString = input("Enter string to encode\n")
    inputString = inputString.lower()
    EncodedString = ""
    for i in range (len(inputString)):
      if(inputString[i] >= 'a' and inputString[i]<='z'):
        temp = ord(inputString[i]) + shift
        if(temp > 122):
          temp = 96 + (temp-122)
        EncodedString += chr(temp)
      else:
        EncodedString += inputString[i]
    
    print(f"Encoded string is {EncodedString}")
  elif(choice == "decode"):
    shift = int(input("Enter number of shift chosen earlier\n"))
    shift = shift%26
    inputString = input("Enter string to encode\n")
    inputString = inputString.lower()
    DecodedString = ""
    for i in range(len(inputString)):
      if(inputString[i] >= 'a' and inputString[i]<='z'):
        temp = ord(inputString[i]) - shift
        if(temp<97):
          temp = 123 - (97-temp)
        DecodedString += chr(temp)
      else:
        DecodedString += inputString[i]
        
        
    print(f"Decoded String {DecodedString}")
  ch = input ("Enter Y to Continue\nEnter N to exit\n")
  if(ch == "N"):
    break



    

