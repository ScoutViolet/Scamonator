import csv

while True:
    f=open("Scamonator\Scam Detection (Responses) - Form Responses 1.csv","r")
    fb=csv.reader(f)
    print("""
    1. Search by phone number
    2. Search by email
    3. Search by content
    4. Exit
    """)
    n=int(input("Enter your choice (1-4)"))
    if n==1:
        pn=input("Enter phone number -- all numbers, no spaces or symbols (**********): ")
        print("\n")
        ctr=0
        for record in fb:
            if record[1]==pn:
                ctr+=1
                print(record) 
        if ctr==1:
            print("\nThere has been ",ctr," report of the suspicious phone number ",pn,".")
        else:
            print("\nThere have been ",ctr," reports of the suspicious phone number ",pn,".")
    elif n==2:
        ea=input("Enter email address (xxxxx@xxxxx.xxx): ")
        print("\n")
        ctr=0
        for record in fb:
            if ea.upper() in record[2].upper():
                ctr+=1
                print(record)
        if ctr==1:
            print("\nThere has been ",ctr," report of the suspicious email address ",ea,".")
        else:
            print("\nThere have been ",ctr," reports of the suspicious email address ",ea,".")
    elif n==3:
        sc=input("Enter content: ")
        print("\n")
        ctr=0
        for record in fb:
            if sc.upper() in record[3].upper():
                ctr+=1
                print(record)
        if ctr==1:
            print("\nThere has been ",ctr," report that contains the exact content you entered.")
        else:
            print("\nThere have been ",ctr," reports that contain the exact content you entered.")
    elif n==4:
        break