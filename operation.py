# operation.py

import heapq
from write import ticket_queue, priority_queue, undo_stack, save_queues, save_tickets_to_file


def is_ticket_resolvable(ticket_id, tickets):
    ticket = tickets[ticket_id]
    if ticket["Parent Ticket"] is None:
        return True
    parent_id = ticket["Parent Ticket"]
    if tickets[parent_id]["Status"] != "Closed":
        return False
    return is_ticket_resolvable(parent_id, tickets)

# Update ticket status 
def update_ticket_status(tickets, action_stack):
    print("\n=== Update Ticket Status ===")
    next_ticket_id = None

    # Priority first
    while priority_queue:
        _, tid = heapq.heappop(priority_queue)
        if tid in tickets and tickets[tid]["Status"] == "Open":
            next_ticket_id = tid
            break

    # Standard queue
    if next_ticket_id is None:
        while ticket_queue:
            tid = ticket_queue.popleft()
            if tid in tickets and tickets[tid]["Status"] == "Open":
                next_ticket_id = tid
                break

    if next_ticket_id is None:
        print("⚠ No open tickets available to update.")
        return

    tid = next_ticket_id
    if not is_ticket_resolvable(tid, tickets):
        print(f"⚠ Cannot resolve Ticket {tid}: Parent ticket still open!")
        return

    prev_status = tickets[tid]["Status"]
    tickets[tid]["Status"] = "Closed"
    action_stack.append(("update", tid, prev_status))
    save_tickets_to_file(tickets)
    save_queues()
    print(f"✅ Ticket {tid} status updated to Closed.")

# Undo last action 
def undo_last_action(tickets, action_stack):
    print("\n=== Undo Last Action ===")
    if not action_stack:
        print("⚠ No actions to undo.")
        return
    action = action_stack.pop()
    if action[0] == "create":
        tid = action[1]
        if tid in tickets:
            tickets.pop(tid)
            save_tickets_to_file(tickets)
            save_queues()
            print(f"✅ Undo: Ticket {tid} creation removed.")
    elif action[0] == "update":
        tid, prev_status = action[1], action[2]
        if tid in tickets:
            tickets[tid]["Status"] = prev_status
            save_tickets_to_file(tickets)
            save_queues()
            print(f"✅ Undo: Ticket {tid} status reverted to {prev_status}.")
