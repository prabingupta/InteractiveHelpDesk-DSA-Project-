# main.py
from write import create_ticket, load_tickets_from_file, load_queues
from read import view_all_tickets, show_dashboard, ticket_history
from operation import update_ticket_status, undo_last_action


tickets = load_tickets_from_file(ticket_history)
load_queues()
ticket_counter = max(tickets.keys(), default=0) + 1
action_stack = []

def show_header():
    print("\n==============================================")
    print("                   Welcome TO                ")
    print("             Interactive Help Desk System    ")
    print("==============================================")
    print("📍 Address: Anamnagar-29, Kathmandu, Nepal")
    print("📞 Helpline: +977-98232132323")
    print("📧 Support: support@helpdesksystem.com")
    print("==============================================\n")

def show_menu():
    print("1. Create New Ticket")
    print("2. View All Tickets")
    print("3. Update Ticket Status")
    print("4. Show Dashboard")
    print("5. Undo Last Action")
    print("6. Show Ticket History")
    print("7. Exit")


show_header()
while True:
    show_menu()
    choice = input("Choose an option: ").strip()

    if choice == "1":
        ticket_counter = create_ticket(ticket_counter, tickets, action_stack, ticket_history)

    elif choice == "2":
        view_all_tickets(tickets)

    elif choice == "3":
        update_ticket_status(tickets, action_stack)

    elif choice == "4":
        show_dashboard(tickets)

    elif choice == "5":
        undo_last_action(tickets, action_stack)

    elif choice == "6":
        ticket_history.show_history()

    elif choice == "7":
        print("\nThank you for using Interactive Help Desk System. Goodbye!")
        break

    else:
        print("\n❌ Invalid choice! Please try again.")
