# write.py
from collections import deque
import heapq
from datetime import datetime

# Queues and stack
ticket_queue = deque()      
priority_queue = []         
undo_stack = []             

# Save tickets to file
def save_tickets_to_file(tickets, filename="tickets.txt"):
    with open(filename, "w") as f:
        for t in tickets.values():
            f.write(
                f"Ticket ID:{t['Ticket ID']}, Title:{t['Title']}, Description:{t['Description']}, "
                f"Priority:{t['Priority']}, Status:{t['Status']}, Reporter Name:{t['Reporter Name']}, "
                f"Parent Ticket:{t['Parent Ticket']}, Created On:{t['Created On']}\n"
            )

# Loads the tickets from file
def load_tickets_from_file(ticket_history, filename="tickets.txt"):
    tickets = {}
    try:
        with open(filename, "r") as f:
            for line in f:
                if line.strip() == "":
                    continue
                parts = line.strip().split(", ")
                ticket = {}
                for p in parts:
                    key, value = p.split(":", 1)
                    key = key.strip()
                    value = value.strip()
                    if key in ["Ticket ID", "Parent Ticket"]:
                        value = int(value) if value != "None" else None
                    ticket[key] = value
                tickets[ticket["Ticket ID"]] = ticket
                # Queue 
                if ticket["Status"] == "Open":
                    if ticket["Priority"].lower() == "high":
                        heapq.heappush(priority_queue, (1, ticket["Ticket ID"]))
                    else:
                        ticket_queue.append(ticket["Ticket ID"])
                
                ticket_history.add_ticket(ticket)
    except FileNotFoundError:
        pass
    return tickets


def save_queues():
    with open("queues.txt", "w") as f:
        f.write("Priority Queue:\n")
        f.write(",".join(str(tid) for _, tid in priority_queue) + "\n")
        f.write("Standard Queue:\n")
        f.write(",".join(str(tid) for tid in ticket_queue) + "\n")


def load_queues():
    import heapq
    try:
        with open("queues.txt", "r") as f:
            lines = f.readlines()
            if len(lines) >= 2:
                pq = lines[1].strip()
                if pq:
                    for tid in pq.split(","):
                        heapq.heappush(priority_queue, (1, int(tid)))
            if len(lines) >= 4:
                sq = lines[3].strip()
                if sq:
                    for tid in sq.split(","):
                        ticket_queue.append(int(tid))
    except FileNotFoundError:
        pass

# Creating ticket
def create_ticket(ticket_counter, tickets, action_stack, ticket_history):
    print("\n=== Create New Ticket ===")
    title = input("Title: ")
    description = input("Description: ")
    priority = input("Priority (High/Medium/Low): ")
    reporter_name = input("Reporter Name: ")

   
    while True:
        parent_ticket = input("Parent Ticket ID (or press Enter if none): ")
        if parent_ticket == "":
            parent_ticket = None
            break
        elif parent_ticket.isdigit() and int(parent_ticket) in tickets:
            parent_ticket = int(parent_ticket)
            break
        else:
            print("❌ Invalid Ticket ID. Enter an existing Ticket ID or leave blank.")

    status = "Open"
    created_on = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    ticket = {
        "Ticket ID": ticket_counter,
        "Title": title,
        "Description": description,
        "Priority": priority,
        "Status": status,
        "Reporter Name": reporter_name,
        "Parent Ticket": parent_ticket,
        "Created On": created_on
    }

    tickets[ticket_counter] = ticket
    ticket_history.add_ticket(ticket)

  
    import heapq
    if priority.lower() == "high":
        heapq.heappush(priority_queue, (1, ticket_counter))
    else:
        ticket_queue.append(ticket_counter)

    # Save and undo
    save_tickets_to_file(tickets)
    save_queues()
    action_stack.append(("create", ticket_counter))

    print(f"✅ Ticket {ticket_counter} created successfully!")
    return ticket_counter + 1
