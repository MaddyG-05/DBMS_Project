### README

# IRCTC-like Railway Reservation System

This project is a comprehensive database management system designed to simulate the Indian Railway Catering and Tourism Corporation (IRCTC) reservation system. It includes functionalities for booking trains, buses, and flights, complete with a payment portal. The system is built using SQL and includes features such as meal selection, class-based pricing, and agent-based booking.

## Features

- **Multi-Transport Booking**: Book tickets for trains, buses, and flights.
- **Admin and User Roles**: Admins can manage the database, while users can book tickets.
- **Meal Selection**: Users can choose from available meal options on trains.
- **Dynamic Pricing**: Ticket prices are calculated based on distance and class multipliers.
- **Agent Booking**: Users can hire agents to book tickets on their behalf.
- **Cancellation**: Both users and admins can cancel tickets.

## Project Structure

- **Entities**:
  - `User`
  - `Agent`
  - `Train`
  - `Bus`
  - `Flight`
  - `Station`
  - `Bus Stop`
  - `Airport`
  - `Meal`
  - `Train Classes`
  - `Flight Classes`
  - `Payment`

- **Relationships**:
  - `Train Booking`
  - `Bus Booking`
  - `Flight Booking`
  - `Train Stops`
  - `Bus Stops At`
  - `Serves`
  - `Hires`
  - `Payment`

## ER Diagram
The ER diagram represents the relationships between various entities within the system. It includes ternary relationships for bookings and weak entities like `Train Classes` and `Flight Classes`.

## SQL Functions and Triggers
- Functions to find the first and last stations for a train.
- Functions to count bookings for a specific train, bus, or class.
- Triggers to handle ticket cancellations and age calculations.

## Views
- Views to aggregate payment data and identify special categories of travelers.
- Views to summarize earnings and losses from bookings and cancellations.

## Optimization
- Query optimization techniques to improve performance.
- Use of composite indexes for efficient data retrieval.

## Getting Started
1. **Clone the repository**: `git clone https://github.com/yourusername/IRCTC-DBMS.git`
2. **Set up the database**: Import the provided SQL scripts to set up the database schema.
3. **Run the application**: Use your preferred SQL client to interact with the database.

## Contributors
- Mudit Gupta
- Siya Garg
- Srijan Arora
- [Srishti Jain](https://github.com/srishti20543)
