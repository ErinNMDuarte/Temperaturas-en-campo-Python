proceso=True
dias_sin_error=0
diasmenor=0
diasmayor=0
diascompartidos=0
promediominima=0
promediomaximo=0
temperaturamax=0
temperaturamin=0
dias_con_error=0
dias=0
while proceso:
    temperaturamax=int(input("digite la temperatura maxima: "))
    temperaturamin=int(input("digite la temperatura minima: "))
    if  temperaturamin<5 and temperaturamax>0 and temperaturamax<=35:
        diasmenor=diasmenor+1
    elif temperaturamin>=5 and temperaturamax>35:
        diasmayor=diasmayor+1
    elif temperaturamin>0 and temperaturamin<5 and temperaturamax>35:
        diascompartidos=diascompartidos+1
    elif temperaturamin>=5 and temperaturamax>0 and temperaturamax<=35:
        dias_sin_error=dias_sin_error+1
        diasmenor+diasmayor+diascompartidos+dias_sin_error    
        if  temperaturamax<=35 and temperaturamin>=5:
            promediomaximo=promediomaximo+temperaturamax 
            if temperaturamin>=5 and temperaturamax<=35:
               promediominima=promediominima+temperaturamin
        else:
            break          
    else:
        temperaturamin==0 and temperaturamax==0  
        proceso=False

maximo=promediomaximo/dias_sin_error
minino=promediominima/dias_sin_error      
dias_con_error= diasmayor+diasmenor+diascompartidos
dias=dias_con_error+dias_sin_error
porcentaje=dias_con_error*100/dias
print(dias)
print(dias_con_error)
print(diasmenor)
print(diasmayor)
print(diascompartidos)
print(maximo)
print(minino)
print(porcentaje)
