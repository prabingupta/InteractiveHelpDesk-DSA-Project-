# Interactive Help Desk System

## Overview
The **Interactive Help Desk System** is a Python-based ticket management application designed to help organizations manage support tickets efficiently. It allows users to create, view, update, and track tickets with priorities, parent-child relationships, and undo functionality. This system implements all tasks from **Week 1 to Week 5**, including dashboards, priority queues, linked list ticket history, and undo operations.

---

## Features
- **Create Tickets:** Users can submit new tickets with title, description, priority, and reporter information.
- **View All Tickets:** Displays a list of all tickets with their ID, title, status, priority, and reporter name.
- **Update Ticket Status:** Allows tickets to be marked as `Closed`. High-priority tickets are automatically resolved first.
- **Undo Last Action:** Supports undoing the last ticket creation or status update.
- **Dashboard Analytics:** Shows total tickets, open and closed tickets, and priority distribution.
- **Ticket History:** Maintains a chronological history of all tickets using a linked list.
- **Parent-Child Ticket Validation:** Ensures a ticket cannot be closed until its parent ticket is closed.
- **File Persistence:** Tickets and queues are saved to files, enabling the system to persist data between sessions.

---

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/prabingupta/InteractiveHelpDesk-DSA-Project-.git
   ```
