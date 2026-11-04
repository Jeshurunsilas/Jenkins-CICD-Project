
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>Welcome To Jeshurun Silas | CI/CD Project</title>

<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">

<style>
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Poppins', sans-serif;
    min-height: 100vh;
    color: white;
    background: linear-gradient(
        135deg,
        #090979,
        #4b00b5,
        #a100a8,
        #ff416c
    );
    background-size: 300% 300%;
    animation: gradient 12s ease infinite;
    overflow-x: hidden;
}

@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

.circle {
    position: fixed;
    border-radius: 50%;
    filter: blur(3px);
    opacity: 0.25;
    z-index: 0;
    animation: float 8s ease-in-out infinite;
}

.circle.one {
    width: 300px;
    height: 300px;
    background: #00e5ff;
    top: 10%;
    left: -100px;
}

.circle.two {
    width: 250px;
    height: 250px;
    background: #ffea00;
    bottom: 5%;
    right: -70px;
    animation-delay: 2s;
}

@keyframes float {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-40px); }
}

.container {
    position: relative;
    z-index: 1;
    max-width: 1150px;
    margin: auto;
    padding: 25px;
}

nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px 0;
}

.logo {
    font-size: 23px;
    font-weight: 800;
    letter-spacing: 1px;
}

.status {
    padding: 9px 17px;
    border-radius: 30px;
    background: rgba(255,255,255,0.16);
    border: 1px solid rgba(255,255,255,0.3);
    font-size: 12px;
    backdrop-filter: blur(12px);
}

.hero {
    text-align: center;
    padding: 100px 10px 75px;
}

.tag {
    display: inline-block;
    padding: 9px 20px;
    border-radius: 30px;
    background: rgba(255,255,255,0.17);
    border: 1px solid rgba(255,255,255,0.3);
    font-size: 13px;
    margin-bottom: 25px;
}

h1 {
    font-size: clamp(42px, 7vw, 76px);
    font-weight: 800;
    line-height: 1.15;
    margin-bottom: 25px;
}

h1 span {
    background: linear-gradient(90deg, #ffe259, #ffa751, #ff8bd1);
    -webkit-background-clip: text;
    color: transparent;
}

.description {
    max-width: 680px;
    margin: auto;
    color: rgba(255,255,255,0.85);
    font-size: 16px;
    line-height: 1.9;
}

.button {
    display: inline-block;
    margin-top: 35px;
    padding: 15px 32px;
    border-radius: 40px;
    background: white;
    color: #7000b8;
    text-decoration: none;
    font-weight: 700;
    box-shadow: 0 10px 35px rgba(0,0,0,0.2);
    transition: 0.3s;
}

.button:hover {
    transform: translateY(-5px) scale(1.04);
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
}

.cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 22px;
    margin: 25px 0 70px;
}

.card {
    padding: 30px;
    border-radius: 22px;
    background: rgba(255,255,255,0.14);
    border: 1px solid rgba(255,255,255,0.25);
    backdrop-filter: blur(15px);
    transition: 0.3s;
}

.card:hover {
    transform: translateY(-10px);
    background: rgba(255,255,255,0.23);
}

.icon {
    font-size: 38px;
    margin-bottom: 17px;
}

.card h3 {
    font-size: 19px;
    margin-bottom: 10px;
}

.card p {
    font-size: 13px;
    line-height: 1.8;
    color: rgba(255,255,255,0.8);
}

footer {
    text-align: center;
    padding: 25px;
    border-top: 1px solid rgba(255,255,255,0.2);
    font-size: 12px;
    color: rgba(255,255,255,0.75);
}

@media(max-width: 750px) {
    .cards {
        grid-template-columns: 1fr;
    }

    .hero {
        padding: 75px 5px 45px;
    }

    .description {
        font-size: 14px;
    }
}
</style>
</head>

<body>

<div class="circle one"></div>
<div class="circle two"></div>

<div class="container">

    <nav>
        <div class="logo">✦ DEV<span style="color:#ffe259">FLOW</span></div>
        <div class="status">● SYSTEM ONLINE</div>
    </nav>

    <section class="hero">

        <div class="tag">🚀 MY FIRST CI/CD WEBSITE</div>

        <h1>
            Welcome to<br>
            <span>Something Amazing.</span>
        </h1>

        <p class="description">
            Hello, world! Welcome to Jeshurun Silas- my containerized web application.
            This website is automatically built, tested and deployed
            using Jenkins, Docker, Python and Flask.
            My CI/CD Pipeline is working successfully!
        </p>

        <a href="/health" class="button">
            Check System Health →
        </a>

    </section>

    <section class="cards">

        <div class="card">
            <div class="icon">⚡</div>
            <h3>Jenkins Automation</h3>
            <p>
                Automatically builds and tests the application
                whenever new code changes are detected.
            </p>
        </div>

        <div class="card">
            <div class="icon">🐳</div>
            <h3>Docker Powered</h3>
            <p>
                Runs the application inside a portable,
                isolated Docker container.
            </p>
        </div>

        <div class="card">
            <div class="icon">🌐</div>
            <h3>Flask Application</h3>
            <p>
                A lightweight Python web application
                delivered through a modern web interface.
            </p>
        </div>

    </section>

    <footer>
        © 2026 DEVFLOW | Built with Python, Flask, Jenkins & Docker
        <br><br>
        <span>Designed for my Software Engineering CI/CD Experiment</span>
    </footer>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

@app.route("/health")
def health():
    return jsonify({"status": " Not Very Healthy"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
