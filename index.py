
# Dictionary of the items, their IDs and prices
items_catalogue = {
    1: {"Name": "Slim Bar", "Price": 5},
    2: {"Name": "Far Bar", "Price": 10},
    3: {"Name": "Mar Bar", "Price": 20},
    4: {"Name": "Twin Bar", "Price": 50}
}


coins_allowed = (5, 10, 20, 50)


class vendingMachine:

    bal = 0

    def __init__(self):
        pass

    def deposit(self, money):
        self.money = money
        return f"Inserting {money}p."

    # Function to handing the calculating of balance
    def change(self, price):
        your_change = self.money - price
        return f"Your change is {your_change}p"

    # This function lists out all the items and their IDs
    def show(self):
        for id, item in items_catalogue.items():
            print(id, ":", item)

    def coin(self):
        while True:
            try:
                self.insert_coin = int(input("""
            ______________________________________________________
            Insert one of the following coins (5, 10, 20, 50):
            """))

                self.bal = self.insert_coin

            except ValueError:
                print("Please enter a valid coin")
                continue
            else:
                break
                # self.insert_coin = int(
                # input("You can only enter an coins (5, 10, 20 or 50). Try Again!: "))

            return self.bal

    def item_id(self):
        while True:
            try:
                self.select_item = int(
                    input("Select a product id from the ones displyed above. (Eg, 1, 2, 3 or 4): "))
                # break

            except ValueError:
                print("Please enter a valid item ID")
                continue
            else:
                break
                # self.select_item = int(
                # input("The item id can only be a positive integer (1, 2, 3 or 4): "))

        if self.select_item not in items_catalogue:
            self.select_item = int(
                input("The item id can only be a positive integer (1, 2, 3 or 4): "))

        print(
            f'You have selected {items_catalogue[self.select_item].get("Name")} and it costs {items_catalogue[self.select_item].get(str("Price"))}p')
        confirm_purchase = input(
            "Would you like to continue with the purchase? Yes or No?: ").lower()
        if confirm_purchase == "yes":
            print("balance:", self.bal)
            if items_catalogue[self.select_item].get("Price") == self.bal:
                self.bal = 0
                print(
                    f'You have successfully purchased {items_catalogue[self.select_item].get("Name")} thank you, your change is {self.bal}!')

            elif (self.bal > items_catalogue[self.select_item].get("Price")):
                self.bal = self.bal - \
                    items_catalogue[self.select_item].get("Price")

                print(
                    f'You have successfully purchased, {items_catalogue[self.select_item].get("Name")} thank you. Your bal is {self.bal}')

                take_change = self.change(
                    items_catalogue[self.select_item].get("Price"))
                # print(take_change)
                # print("You have ", str(take_change), " pounds left.")

                new_purchase = input(
                    "Would you like to buy something else? Yes or No?: ").lower()
                if new_purchase == "yes":

                    self.item_id()

                else:
                    print(
                        take_change, ". Thank you!")

            else:
                print(
                    "You do not have enough coins to make this purchase, thank you!")

        else:
            print("Please take back your ", self.bal,
                  "p, see you next time!")

            return self.bal


def main():
    m = vendingMachine()
    coin_inserted = False
    m.show()
    while coin_inserted == False:

        m.coin()

        if m.insert_coin in coins_allowed:
            break

        else:
            print("Please insert a valid coin!")

    coin_inserted == True
    print(m.deposit(m.insert_coin))
    m.show()

    m.item_id()


if __name__ == "__main__":
    main()
