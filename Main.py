class CustomPackage:
    def __init__(self, name):
        self.name = name
        self.flights = []
        self.hotels = []
        self.activities = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def add_hotel(self, hotel):
        self.hotels.append(hotel)

    def add_activity(self, activity):
        self.activities.append(activity)

    def calculate_total_cost(self):
        total_cost = sum([item.price for item in self.flights + self.hotels + self.activities])
        return total_cost


class CustomPackageCreation:
    def __init__(self):
        self.custom_packages = []

    def create_custom_package(self):
        name = input("Enter package name: ")
        custom_package = CustomPackage(name)

        add_flights = input("Add flights to the package? (y/n): ")
        while add_flights.lower() == "y":
            flight_name = input("Enter flight name: ")
            flight_price = float(input("Enter flight price: "))
            flight = Flight(flight_name, flight_price)
            custom_package.add_flight(flight)
            add_flights = input("Add another flight? (y/n): ")

        add_hotels = input("Add hotels to the package? (y/n): ")
        while add_hotels.lower() == "y":
            hotel_name = input("Enter hotel name: ")
            hotel_price = float(input("Enter hotel price: "))
            hotel = Hotel(hotel_name, hotel_price)
            custom_package.add_hotel(hotel)
            add_hotels = input("Add another hotel? (y/n): ")

        add_activities = input("Add activities to the package? (y/n): ")
        while add_activities.lower() == "y":
            activity_name = input("Enter activity name: ")
            activity_price = float(input("Enter activity price: "))
            activity = Activity(activity_name, activity_price)
            custom_package.add_activity(activity)
            add_activities = input("Add another activity? (y/n): ")

        self.custom_packages.append(custom_package)
        print("Custom package created successfully!")

    def browse_custom_packages(self):
        print("Custom Packages:")
        if self.custom_packages:
            for package in self.custom_packages:
                print("Package:", package.name)
                print("Total Cost:", package.calculate_total_cost())
                print("-------------------------")
        else:
            print("No custom packages found.")
class Package:
    def __init__(self, name, flights, hotels, activities):
        self.name = name
        self.flights = flights
        self.hotels = hotels
        self.activities = activities

    def calculate_total_cost(self):
        total_cost = sum([item.price for item in self.flights + self.hotels + self.activities])
        return total_cost


class Flight:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Hotel:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Activity:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Booking:
    def __init__(self, customer, package):
        self.customer = customer
        self.package = package

    def calculate_total_cost(self):
        return self.package.calculate_total_cost()

    def display_booking_details(self):
        print("Booking Details:")
        print("Customer:", self.customer.name)
        print("Package:", self.package.name)
        print("Total Cost:", self.calculate_total_cost())


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class PaymentInfo:
    def __init__(self, card_number, card_holder, expiration_date, cvv):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiration_date = expiration_date
        self.cvv = cvv


class Agent:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def view_reports(self, reports):
        print("Reports:")
        for report in reports:
            print("Report ID:", report.report_id)
            print("Agent:", report.agent.name)
            print("Booking:", report.booking.package.name)
            print("Revenue:", report.revenue)
            print("-------------------------")

    def view_revenue(self, reports):
        total_revenue = sum([report.revenue for report in reports])
        print("Total Revenue:", total_revenue)

    def send_notification(self, customer, message):
        print("Sending notification to", customer.name)
        print("Message:", message)


class Report:
    report_id_counter = 1

    def __init__(self, agent, booking, revenue):
        self.report_id = Report.report_id_counter
        Report.report_id_counter += 1
        self.agent = agent
        self.booking = booking
        self.revenue = revenue


class Notification:
    def __init__(self, sender, receiver, message):
        self.sender = sender
        self.receiver = receiver
        self.message = message


class PackageManagement:
    def __init__(self):
        self.packages = []
        self.bookings = []
        self.agents = []
        self.reports = []
        self.notifications = []

    def create_package(self):
        name = input("Enter package name: ")
        flights = []
        hotels = []
        activities = []

        add_flights = input("Add flights to the package? (y/n): ")
        while add_flights.lower() == "y":
            flight_name = input("Enter flight name: ")
            flight_price = float(input("Enter flight price: "))
            flight = Flight(flight_name, flight_price)
            flights.append(flight)
            add_flights = input("Add another flight? (y/n): ")

        add_hotels = input("Add hotels to the package? (y/n): ")
        while add_hotels.lower() == "y":
            hotel_name = input("Enter hotel name: ")
            hotel_price = float(input("Enter hotel price: "))
            hotel = Hotel(hotel_name, hotel_price)
            hotels.append(hotel)
            add_hotels = input("Add another hotel? (y/n): ")

        add_activities = input("Add activities to the package? (y/n): ")
        while add_activities.lower() == "y":
            activity_name = input("Enter activity name: ")
            activity_price = float(input("Enter activity price: "))
            activity = Activity(activity_name, activity_price)
            activities.append(activity)
            add_activities = input("Add another activity? (y/n): ")

        package = Package(name, flights, hotels, activities)
        self.packages.append(package)
        print("Package created successfully!")

    def modify_package(self):
        if self.packages:
            package_name = input("Enter package name to modify: ")
            package = self.find_package_by_name(package_name)
            if package:
                print("Package found!")
                self.display_package_details(package)
                modify_option = input("Enter the option to modify (flights/hotels/activities): ")
                if modify_option.lower() == "flights":
                    self.modify_flights(package)
                elif modify_option.lower() == "hotels":
                    self.modify_hotels(package)
                elif modify_option.lower() == "activities":
                    self.modify_activities(package)
                else:
                    print("Invalid option.")
            else:
                print("Package not found.")
        else:
            print("No packages found.")

    def find_package_by_name(self, package_name):
        for package in self.packages:
            if package.name == package_name:
                return package
        return None

    def display_package_details(self, package):
        print("Package Details:")
        print("Name:", package.name)
        print("Flights:")
        for flight in package.flights:
            print(flight.name, "-", flight.price)
        print("Hotels:")
        for hotel in package.hotels:
            print(hotel.name, "-", hotel.price)
        print("Activities:")
        for activity in package.activities:
            print(activity.name, "-", activity.price)

    def modify_flights(self, package):
        print("Modify Flights:")
        flight_names = [flight.name for flight in package.flights]
        for i, flight_name in enumerate(flight_names):
            print(i+1, ".", flight_name)

        flight_index = int(input("Enter the flight index to modify: ")) - 1
        if 0 <= flight_index < len(package.flights):
            flight = package.flights[flight_index]
            new_price = float(input("Enter the new price for the flight: "))
            flight.price = new_price
            print("Flight modified successfully!")
        else:
            print("Invalid flight index.")

    def modify_hotels(self, package):
        print("Modify Hotels:")
        hotel_names = [hotel.name for hotel in package.hotels]
        for i, hotel_name in enumerate(hotel_names):
            print(i+1, ".", hotel_name)

        hotel_index = int(input("Enter the hotel index to modify: ")) - 1
        if 0 <= hotel_index < len(package.hotels):
            hotel = package.hotels[hotel_index]
            new_price = float(input("Enter the new price for the hotel: "))
            hotel.price = new_price
            print("Hotel modified successfully!")
        else:
            print("Invalid hotel index.")

    def modify_activities(self, package):
        print("Modify Activities:")
        activity_names = [activity.name for activity in package.activities]
        for i, activity_name in enumerate(activity_names):
            print(i+1, ".", activity_name)

        activity_index = int(input("Enter the activity index to modify: ")) - 1
        if 0 <= activity_index < len(package.activities):
            activity = package.activities[activity_index]
            new_price = float(input("Enter the new price for the activity: "))
            activity.price = new_price
            print("Activity modified successfully!")
        else:
            print("Invalid activity index.")

    def browse_packages(self):
        print("Packages:")
        if self.packages:
            for package in self.packages:
                print("Package:", package.name)
                print("Total Cost:", package.calculate_total_cost())
                print("-------------------------")
        else:
            print("No packages found.")

    def search_package(self):
        if self.packages:
            package_name = input("Enter package name to search: ")
            package = self.find_package_by_name(package_name)
            if package:
                print("Package found!")
                self.display_package_details(package)
            else:
                print("Package not found.")
        else:
            print("No packages found.")

    def create_booking(self):
        if self.packages:
            package_name = input("Enter package name for booking: ")
            package = self.find_package_by_name(package_name)
            if package:
                customer_name = input("Enter customer name: ")
                customer_email = input("Enter customer email: ")
                customer = Customer(customer_name, customer_email)

                booking = Booking(customer, package)
                self.bookings.append(booking)
                print("Booking created successfully!")

                agent_email = input("Enter agent email for the booking: ")
                agent = self.find_agent_by_email(agent_email)
                if agent:
                    revenue = booking.calculate_total_cost() * 0.1
                    report = Report(agent, booking, revenue)
                    self.reports.append(report)
                    print("Report generated successfully!")

                    message = "Booking confirmed for package: " + package.name
                    agent.send_notification(customer, message)
                else:
                    print("Agent not found.")
            else:
                print("Package not found.")
        else:
            print("No packages found.")

    def find_agent_by_email(self, agent_email):
        for agent in self.agents:
            if agent.email == agent_email:
                return agent
        return None

    def create_agent(self):
        name = input("Enter agent name: ")
        email = input("Enter agent email: ")
        agent = Agent(name, email)
        self.agents.append(agent)
        print("Agent created successfully!")

    def view_reports(self):
        if self.reports:
            agent_email = input("Enter agent email to view reports: ")
            agent_reports = [report for report in self.reports if report.agent.email == agent_email]
            if agent_reports:
                agent = agent_reports[0].agent
                agent.view_reports(agent_reports)
            else:
                print("No reports found for the agent.")
        else:
            print("No reports found.")

    def view_revenue(self):
        if self.reports:
            agent_email = input("Enter agent email to view revenue: ")
            agent_reports = [report for report in self.reports if report.agent.email == agent_email]
            if agent_reports:
                agent = agent_reports[0].agent
                agent.view_revenue(agent_reports)
            else:
                print("No reports found for the agent.")
        else:
            print("No reports found.")

    def send_notification(self):
        sender_email = input("Enter sender's email: ")
        receiver_email = input("Enter receiver's email: ")
        message = input("Enter notification message: ")

        sender = None
        receiver = None

        for agent in self.agents:
            if agent.email == sender_email:
                sender = agent
            elif agent.email == receiver_email:
                receiver = agent

        if sender and receiver:
            notification = Notification(sender, receiver, message)
            self.notifications.append(notification)
            print("Notification sent successfully!")
        else:
            print("Invalid sender or receiver email.")


def main():
    package_management = PackageManagement()
    custom_package_creation = CustomPackageCreation()
    
    while True:
        print("1. Create Package")
        print("2. Modify Package")
        print("3. Browse Packages")
        print("4. Search Package")
        print("5. Create Booking")
        print("6. View Reports")
        print("7. View Revenue")
        print("8. Send Notification")
        print("9. Create Agent")
        print("10. Create Custom Package")
        print("11. Browse Custom Packages")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            package_management.create_package()
        elif choice == "2":
            package_management.modify_package()
        elif choice == "3":
            package_management.browse_packages()
        elif choice == "4":
            package_management.search_package()
        elif choice == "5":
            package_management.create_booking()
        elif choice == "6":
            package_management.view_reports()
        elif choice == "7":
            package_management.view_revenue()
        elif choice == "8":
            package_management.send_notification()
        elif choice == "9":
            package_management.create_agent()
        elif choice == "10":
            custom_package_creation.create_custom_package()
        elif choice == "11":
            custom_package_creation.browse_custom_packages()
        elif choice == "12":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
