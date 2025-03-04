from flask import Flask, 

app = Flask(__name__)

@app.route('/')
def home():
    return "<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="keywords" content="autopc">
    <meta name="description" content="AutoPC, made for QHacks 2022.">
    <meta name="author" content="David C, Amy C, Mercy D, Jagrit R">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PC4U</title>
    <style>
        /* Basic Reset */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Exo', sans-serif;
            background-color: #f4f4f4;
            color: #333;
            line-height: 1.6;
        }

        /* Navbar Styles */
        .navbar {
            background-color: #000000;
            padding: 10px 20px;
            border-bottom: 3px solid #702012;
            position: fixed;
            width: 100%;
            top: 0;
            z-index: 1000;
        }

        .navbar a {
            color: #702012;
            text-decoration: none;
            font-weight: bold;
            margin: 0 15px;
        }

        .navbar a:hover {
            color: #fff;
        }

        .navbar img {
            width: 50px;
            height: auto;
        }

        /* Main Content Styles */
        .container {
            margin-top: 100px;
            padding: 20px;
            text-align: center;
        }

        .home-text {
            margin-bottom: 40px;
        }

        .home-text h1 {
            font-size: 2.5rem;
            color: #702012;
        }

        .home-text h2 {
            font-size: 1.5rem;
            color: #000000;
            margin-top: 10px;
        }

        .home-text button {
            background-color: #702012;
            color: #fff;
            border: none;
            padding: 10px 20px;
            font-size: 1rem;
            cursor: pointer;
            margin-top: 20px;
        }

        .home-text button:hover {
            background-color: #000000;
        }

        /* Features Section */
        .home-sum {
            background-color: #fff;
            padding: 20px;
            border: 2px solid #702012;
            border-radius: 5px;
            margin-top: 40px;
        }

        .home-sum .row {
            display: flex;
            justify-content: space-between;
            margin-bottom: 20px;
        }

        .home-sum .title-column {
            font-size: 1.2rem;
            font-weight: bold;
            color: #702012;
        }

        .home-sum .flvtext-column {
            font-size: 1rem;
            color: #333;
        }
    </style>
</head>
<body>
    <!-- Navbar -->
    <nav class="navbar">
        <div>
            <a href="index.html">
                <img src="static/images/PC.png" alt="AutoPC">
            </a>
            <a href="./build">Start Your Creation</a>
            <a href="https://pc-builder.net/knowledge-base/">Guides and Resources</a>
        </div>
    </nav>

    <!-- Main Content -->
    <div class="container">
        <div class="home-text">
            <h1>A PC built by <span style="color:#000000">YOU</span>, made for <span style="color:#000000">YOU</span></h1>
            <h2>Turn your PC dreams into a reality.</h2>
            <a href="./build">
                <button>Start Building!</button>
            </a>
        </div>

        <!-- Features Section -->
        <div class="home-sum">
            <div class="row">
                <div class="title-column">Build with confidence</div>
                <div class="title-column">Valid recommendations</div>
                <div class="title-column">Multiple options</div>
            </div>
            <div class="row">
                <div class="flvtext-column">All parts are sourced from PC Part Picker</div>
                <div class="flvtext-column">The recommendations are well-formed</div>
                <div class="flvtext-column">Choose from a pool of recommendations</div>
            </div>
            <div class="row">
                <div class="title-column">Sharing made easy</div>
                <div class="title-column">Great for beginners and experts</div>
                <div class="title-column">Choose your price range</div>
            </div>
            <div class="row">
                <div class="flvtext-column">Builds can easily be downloaded for sharing</div>
                <div class="flvtext-column">No matter if you’re new to PC building or a seasoned professional, we’ve got it all</div>
                <div class="flvtext-column">Easily input a price range and we’ll match you with the perfect parts</div>
            </div>
        </div>
    </div>
</body>
</html>
    "

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
