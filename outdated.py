month = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    Date = input("Date:")
    try:
        x,y,z = Date.split("/")
        if(int(x)) >=1 and(int(x))<=12 and(int(y)) >=1 and(int(y)) <=31 :
            break
    except:
        try:

            ox,oy,z = Date.split(" ")
            for i in range(len(month)):
                if ox ==month[i] :
                    x =i+1
            y = oy.replace(",","")
            oy = oy.strip()
            z = int(z.strip())
            if(int(x)) >=1 and(int(x))<=12 and(int(y)) >=1 and(int(y)) <=31 :
                break
        except:
            print()


print(f"{int(z):04}-{int(x):02}-{int(y):02}")