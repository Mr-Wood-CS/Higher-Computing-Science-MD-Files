def populateContacts():
    from dataclasses import dataclass

    @dataclass
    class contact:
        Name : str
        Age : int
        PhoneNum : str
        WhatsApp : bool
        OutOfTen : float
    
    contacts = [contact] * 4 
    
    contacts[0] = ("Bruce Taylor", 15,  "01123298567", True, 7.6)
    contacts[1] = ("Gina Williams", 13, "01234567897", False, 4.9)
    contacts[2] = ("Trevor Youngson", 18, "02222222222", False, 6.1)
    contacts[3] = ("Tyler Ice", 12, "07777777777", True, 8.2)
    
    return contacts

def displayContacts(contacts):
    print("All Contacts...\n\n")
    
    for i in range(len(contacts)):
        print(contacts[i].Name, "(" + str(contacts[i].OutOfTen) + ")", "- On WhatsApp", contacts[i].WhatsApp + "- Number", contacts[i].PhoneNum, "\n")
        
def UnderFourteens(contacts):
    for i in range(len(contacts)):
        if contacts[i].Age <= 14:
            print(contacts[i].Name, contacts[i].PhoneNum)
            
def main():
   contacts = populateContacts()
   displayContacts(contacts)
   UnderFourteens(contacts)
   
main()