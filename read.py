
# read.py

# Linked List for Ticket History
class Node:
    def __init__(self, ticket):
        self.ticket = ticket
        self.next = None

class TicketHistory:
    def __init__(self):
        self.head = None

    def add_ticket(self, ticket):
        new_node = Node(ticket)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def show_history(self):
        print("\n📜 --- Ticket History ---")
        current = self.head
        if not current:
            print("No tickets created yet.")
            return
        while current:
            t = current.ticket
            print(f"Ticket ID: {t['Ticket ID']}")
            print(f"Title: {t['Title']}")
            print(f"Description: {t['Description']}")
            print(f"Priority: {t['Priority']}")
            print(f"Status: {t['Status']}")
            print(f"Reporter Name: {t['Reporter Name']}")
            print(f"Parent Ticket: {t['Parent Ticket']}")
            print(f"Created On: {t['Created On']}")
            print("-"*50)
            current = current.next
        print("------------------------\n")

# Ticket History instance
ticket_history = TicketHistory()

# Dashboard analytics
def show_dashboard(tickets):
    print("\n=== Dashboard ===")
    if not tickets:
        print("No tickets available.")
        return
    total = len(tickets)
    open_tickets = sum(1 for t in tickets.values() if t["Status"] == "Open")
    closed_tickets = sum(1 for t in tickets.values() if t["Status"] == "Closed")
    high_priority = sum(1 for t in tickets.values() if t["Priority"].lower() == "high")
    medium_priority = sum(1 for t in tickets.values() if t["Priority"].lower() == "medium")
    low_priority = sum(1 for t in tickets.values() if t["Priority"].lower() == "low")

    print(f"Total Tickets: {total}")
    print(f"Open Tickets: {open_tickets}")
    print(f"Closed Tickets: {closed_tickets}")
    print("Priority Levels:")
    print(f"  High: {high_priority}")
    print(f"  Medium: {medium_priority}")
    print(f"  Low: {low_priority}")
    print("----------------------------")

# View all tickets
def view_all_tickets(tickets):
    print("\n=== All Tickets ===")
    if not tickets:
        print("No tickets available.")
        return
    for t in tickets.values():
        print(f"Ticket ID: {t['Ticket ID']} | Title: {t['Title']} | Status: {t['Status']} | Priority: {t['Priority']} | Reporter: {t['Reporter Name']}")
