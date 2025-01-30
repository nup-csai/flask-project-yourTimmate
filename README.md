# Burning Man Experiences Web App - Deployment Guide

## Project Overview

This Flask-based web application is designed to facilitate ticket purchases for the world's largest music festival, **Burning Man**. Due to the overwhelming demand on ticket-selling platforms, festival organizers have sought our solution to manage and slightly slow down the ticketing process. By requiring users to log in with a publicly known password within a **24-hour window**, we help distribute traffic more evenly, ensuring a smoother ticketing experience.

## Application Features

### Homepage

- The **homepage** allows users to scroll down and explore a brief history of past Burning Man festivals.
- Each festival experience is displayed with a **short description**, an image, and a **"View Details"** button.
- Clicking **"View Details"** redirects the user to a dedicated page with more information about the selected festival, including a detailed description and relevant images.

### Navigation Menu

- The menu is located in the **top right corner** and includes three key functions:
  1. **Contacts**: Users can view the contact details of the event organizers.
  2. **History**: Provides a broader overview of the Burning Man festival’s origins and evolution.
  3. **Ticket Purchase**: Redirects users to a page where they can obtain a unique ticket number.

### Ticket Purchase Process

- Users are required to enter their **personal details** (name, surname, country of origin) in designated input fields.
- After submission, the system generates a **random ticket number**.
- This ticket number can be used on the official **Burning Man** website for finalizing the ticket purchase through the official payment system.

### Homepage Navigation

- To **return to the homepage**, users can click the **Burning Man logo**, which is located in the center of the **gray top bar**.
- This will redirect them back to the main experience list.

## How to Deploy the Project

### Using a Virtual Environment

Follow these steps to set up and deploy the project locally:

1. **Create and activate a virtual environment:**

   ```sh
   python -m venv venv
   .\venv\Scripts\activate  # Windows
   source venv/bin/activate  # macOS/Linux
   ```

2. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run the project locally:**

   ```sh
   python app.py
   ```

### Using Docker

For deploying the project using Docker, follow these steps:

1. **Ensure Docker is installed and running.**
2. **Run the following command to start the application:**
   ```sh
   docker-compose up
   ```

## Accessing the Application

Once the project is running, you can access it using the following links:

- **Web Application:** [Burning Man Ticketing](https://burningman-ticketing.onrender.com)
- **Local Version (Swagger API Docs):** [http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)

## Authentication Details

### How Authentication Works

This web application uses a simple authentication mechanism to manage access and control ticket purchases. To prevent excessive traffic, bots, and cyberattacks on the official **Burning Man ticketing platform**, festival organizers distribute a publicly known **username and password** to registered pre-sale participants. 

These credentials allow users to access our platform and receive a randomly generated **ticket number**, which they can then use on the official **Burning Man** website to finalize and pay for their ticket through the festival’s payment system. This approach provides multiple benefits:

- **Reduces Load on the Official Site**: Users are filtered through our platform, preventing an overwhelming rush of traffic to the main ticket sales page.
- **Protects Against Cyber Attacks**: By requiring authentication, automated bots are deterred from causing site crashes or ticket scalping.
- **Streamlines the Ticketing Process**: Users receive a pre-assigned ticket number through our randomizer, making checkout on the main Burning Man website faster and smoother.

### Login Credentials

To access the application, use the following publicly available credentials:

- **Username:** Burner
- **Password:** Tickets

All users share the same login information, ensuring fair access to ticket distribution.

## How to Run Tests

To execute tests, follow these steps:

1. **Ensure your virtual environment is activated.**
2. **Run the tests using pytest:**
   ```sh
   pytest
   ```

## How to Get Logs

### For Local Development

Logs will be displayed in the terminal where the application is running.

### For Docker

To view logs from the Docker container, use the following command:

```sh
   docker-compose logs
```

## HTML Templates Overview

The application consists of several HTML templates to structure the web interface:

1. **base.html** - The main template that provides the navigation bar and basic layout.
2. **404.html** - Custom error page for missing resources.
3. **experience_details.html** - Displays details for each Burning Man experience.
4. **contacts.html** - Contact information page.
5. **home.html** - Main page listing all experiences.
6. **login.html** - Login page for authentication.
7. **tickets.html** - Page for users to purchase tickets and receive a randomly generated ticket number.
8. **history.html** - Displays information about the history of Burning Man.

## Static Assets

- **CSS:** Styling is provided via `static/style.css`.
- **Icons & Fonts:** The app uses Font Awesome icons and external fonts.
- **Images:** Event images are stored in `static/` directory.

## Development Mode

To enable debug mode, modify the last line in `app.py`:

```python
   app.run(host='0.0.0.0', port=8080, debug=True)
```

This README provides all necessary steps and details for deploying, running, and modifying the Burning Man Experiences Web App. Enjoy the journey!

