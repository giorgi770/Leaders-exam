def show_balance(balance):
    print(f"your balance is ${balance:.2f}")
    #ამ კოდში ფუნქცია show_balance იღებს ერთ არგუმენტს
    #balance და ბეჭდავს ბალანსს ფორმატირებული სტრიქონით, სადაც დოლარის სიმბოლოა გამოყენებული
    #და ბალანსი ორი ათობითი ნიშნითაა ნაჩვენები.

def deposit():
    amount = float(input("enter an amount to be deposited: "))
    #აქ შევქმენი ცვალდი სახელად თანხა და შიგნით დავწერე:შეიყვანეთ შესატანი თანხა(მომხმარებელს შემოვატანინებთ ათწილად რიცხვს,რამდენის უნდა)

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        return amount
    #თუ amount ნაკლებია ნულზე, ბეჭდავს შეტყობინებას "That's not a valid amount" და აბრუნებს 0-ს.
    #წინააღმდეგ შემთხვევაში, აბრუნებს amount-ს.

def withdraw(balance):
    amount = float(input("Enter amount to be withdraw: "))
    #ცვალდი სახელად თანხა,დავწერე;შეიყვანეთ გასატანი თანხა

    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount <0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount
    #თუ amount მეტია balance-ზე, ბეჭდავს შეტყობინებას "Insufficient funds" და აბრუნებს 0-ს.
    #თუ amount ნაკლებია ნულზე, ბეჭდავს შეტყობინებას "Amount must be greater than 0" და აბრუნებს 0-ს.
    #წინააღმდეგ შემთხვევაში, აბრუნებს amount-ს.

def main():
    balance = 0
    is_running = True
    #შეიქმნა main-ფუნქცია და ეს კოდი ასრულებს;ინიციალიზებს balance ცვლადს 0-ით.
    #ინიციალიზებს is_running ცვლადს True-ით.

    while is_running:
        print("  banking program  ")
        #ბანკის პროგრამა
        print("1.show balance")
        #მაჩვენე ბალანსი
        print("2.deposit")
        #დეპოზიტი
        print("3.withdraw")
        #ამოღება
        print("4.exit")
        #გასვლა

        choice = input("Enter your choice (1-4): ")
        #შეიყვანეთ არჩევანი

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            is_running = False
        else:
            print("Thats is not a valid choice")
            #დავპრინტე:ეს არ არის სწორი არჩევანი!
            print("Thank you! have a nice day")
            #დავპრინტე:გმადლობთ!კარგ დღეს გისურვებთ.


if __name__ == '__main__':
    main()