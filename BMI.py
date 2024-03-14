import random
print('''
      
                                                                            ,--,                              ,--,                         ,----,                        
                     ____                                            ,---.'|                           ,---.'|                       ,/   .`|  ,----..               
    ,---,.         ,'  , `.   ,---,          ,----..     ,---,       |   | :     ,----..               |   | :      ,---,          ,`   .'  : /   /   \  ,-.----.    
  ,'  .'  \     ,-+-,.' _ |,`--.' |         /   /   \   '  .' \      :   : |    /   /   \         ,--, :   : |     '  .' \       ;    ;     //   .     : \    /  \   
,---.' .' |  ,-+-. ;   , |||   :  :        |   :     : /  ;    '.    |   ' :   |   :     :      ,'_ /| |   ' :    /  ;    '.   .'___,/    ,'.   /   ;.  \;   :    \  
|   |  |: | ,--.'|'   |  ;|:   |  '        .   |  ;. /:  :       \   ;   ; '   .   |  ;. / .--. |  | : ;   ; '   :  :       \  |    :     |.   ;   /  ` ;|   | .\ :  
:   :  :  /|   |  ,', |  ':|   :  |        .   ; /--` :  |   /\   \  '   | |__ .   ; /--`,'_ /| :  . | '   | |__ :  |   /\   \ ;    |.';  ;;   |  ; \ ; |.   : |: |  
:   |    ; |   | /  | |  ||'   '  ;        ;   | ;    |  :  ' ;.   : |   | :.'|;   | ;   |  ' | |  . . |   | :.'||  :  ' ;.   :`----'  |  ||   :  | ; | '|   |  \ :  
|   :     \'   | :  | :  |,|   |  |        |   : |    |  |  ;/  \   \'   :    ;|   : |   |  | ' |  | | '   :    ;|  |  ;/  \   \   '   :  ;.   |  ' ' ' :|   : .  /  
|   |   . |;   . |  ; |--' '   :  ;        .   | '___ '  :  | \  \ ,'|   |  ./ .   | '___:  | | :  ' ; |   |  ./ '  :  | \  \ ,'   |   |  ''   ;  \; /  |;   | |  \  
'   :  '; ||   : |  | ,    |   |  '        '   ; : .'||  |  '  '--'  ;   : ;   '   ; : .'|  ; ' |  | ' ;   : ;   |  |  '  '--'     '   :  | \   \  ',  / |   | ;\  \ 
|   |  | ; |   : '  |/     '   :  |        '   | '/  :|  :  :        |   ,/    '   | '/  :  | : ;  ; | |   ,/    |  :  :           ;   |.'   ;   :    /  :   ' | \.' 
|   :   /  ;   | |`-'      ;   |.'         |   :    / |  | ,'        '---'     |   :    /'  :  `--'   \'---'     |  | ,'           '---'      \   \ .'   :   : :-'   
|   | ,'   |   ;/          '---'            \   \ .'  `--''                     \   \ .' :  ,      .-./          `--''                         `---`     |   |.'     
`----'     '---'                             `---`                               `---`    `--`----'                                                      `---'       
                                                                                                                                                                     
      
      
      
      ''')
 
health_quotes = [
    "The greatest wealth is health "
    "He who has health, has hope; and he who has hope, has everything"
    "Health is a state of complete physical, mental and social well-being and not merely the absence of disease or infirmity"
]

def print_health_quote(random):
    print(health_quotes[random - 1])
    
random_number = random.randint(1,3)
    
print_health_quote(random_number)



def calculateBMI(weight,height):
 
    height_calc = height/100
    
    bmi = weight / (height_calc ** 2)
    return bmi

weight = float(input("Enter your weight : "))
height = float(input("Enter your height : "))

bmi_result = calculateBMI(weight,height)
print (" Your BMI is : ", bmi_result)

if bmi_result < 18.5:
    print("Underweight")
elif 18.5 <= bmi_result <= 24.9:
    print("Healthy weight")
elif 25.0 <= bmi_result <= 29.9:
    print("Overweight")
else:
    print("Obesity")
   