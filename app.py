from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'playa_magic'

burning_experiences = [
    {
        "id": 1,
        "title": "Burning Man 2021: The Great Unknown",
        "mantra": "\u201cThe real voyage of discovery consists not in seeking new landscapes, but in having new eyes.\u201d  –Marcel Proust",
        "image": "2021.png",
        "description": "A year that pushed the boundaries of the unknown, inviting participants to embrace mystery and spontaneity. The Playa became a canvas for the uncharted, where the absence of answers fostered boundless creativity and deep introspection."
    },
    {
        "id": 2,
        "title": "Burning Man 2022: Waking Dreams",
        "mantra": "\u201cI dreamed I was a butterfly, flitting around in the sky; then I awoke. Now I wonder: Am I a man who dreamt of being a butterfly, or am I a butterfly dreaming that I am a man?\u201d – Zhuang Zi",
        "image": "2022.png",
        "description": "A dreamscape of ephemeral visions and waking consciousness, 2022 blurred the line between reality and imagination. Attendees wandered through surreal art installations, where the impossible felt tangible, and dreams manifested in dazzling lights and towering structures."
    },
    {
        "id": 3,
        "title": "Burning Man 2023: ANIMALIA",
        "mantra": "\u201cSometimes, I am the beast in the darkness.\u201d —Heather Durham",
        "image": "2023.png",
        "description": "An untamed celebration of the primal self, ANIMALIA transformed the Playa into a living ecosystem of wild expression. Tribes emerged, adorned in fantastical costumes, embodying the spirit of nature’s creatures, as fire and rhythm pulsed through the desert night."
    },
    {
        "id": 4,
        "title": "Burning Man 2024: Curiouser & Curiouser",
        "mantra": "\u201cIn order to attain the impossible, one must attempt the absurd.\u201d – Miguel de Cervantes",
        "image": "2024.png",
        "description": "A mad tea party of artistic exploration, 2024 celebrated the whimsical and nonsensical. Alice's Wonderland met the cosmic unknown, where art cars drifted like surreal creatures, and installations bent the laws of time and space, inviting participants into a world of playful chaos."
    },
]

@app.route('/')
def home():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('home.html', experiences=burning_experiences)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'Burner' and password == 'Tickets':
            session['logged_in'] = True
            return redirect(url_for('home'))
        else:
            error = "Invalid credentials. Please try again."
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/experience/<int:id>', methods=['GET'])
def experience_details(id):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    experience = next((exp for exp in burning_experiences if exp['id'] == id), None)
    if experience is None:
        return render_template('404.html')
    return render_template('experience_details.html', experience=experience)

@app.route('/menu')
def menu():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('menu.html')

@app.route('/contacts')
def contacts():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('contacts.html', name="Timofei Pavlov", email="mr.timmate@gmail.com")

@app.route('/history')
def history():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    return render_template('history.html', description="Burning Man was first held in 1986 on Baker Beach in San Francisco...")

@app.route('/tickets', methods=['GET', 'POST'])
def buy_tickets():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    ticket_number = None
    name = None
    surname = None
    country = None
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        country = request.form['country']
        ticket_number = random.randint(100000, 999999)
    return render_template(
        'tickets.html',
        ticket_number=ticket_number,
        name=name,
        surname=surname,
        country=country
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)

