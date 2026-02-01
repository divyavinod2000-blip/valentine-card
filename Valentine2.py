from flask import Flask, render_template_string

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>For My Favorite Person ❤️</title>
    <link href="https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Quicksand:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {
            --primary-pink: #ff4d6d;
            --deep-red: #c9184a;
        }

        body {
            /* Animated gradient background */
            background: linear-gradient(-45deg, #ff9a9e, #fad0c4, #fbc2eb, #a18cd1);
            background-size: 400% 400%;
            animation: gradientBG 15s ease infinite;
            font-family: 'Quicksand', sans-serif;
            height: 100vh;
            margin: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }

        @keyframes gradientBG {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }

        .card {
            background: rgba(255, 255, 255, 0.8);
            padding: 40px;
            border-radius: 30px;
            box-shadow: 0 15px 35px rgba(0,0,0,0.2);
            backdrop-filter: blur(12px);
            text-align: center;
            max-width: 450px;
            width: 85%;
            border: 2px solid rgba(255, 255, 255, 0.5);
            z-index: 10;
        }

        h1 {
            font-family: 'Dancing Script', cursive;
            color: #d81159;
            font-size: 2.8em;
            margin-bottom: 20px;
        }

        .btn-container {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
            min-height: 60px;
            position: relative;
        }

        button {
            font-size: 1.1em;
            padding: 12px 30px;
            border: none;
            border-radius: 50px;
            cursor: pointer;
            font-weight: 600;
            transition: all 0.3s ease;
        }

        .yes-btn {
            background: var(--primary-pink);
            color: white;
            box-shadow: 0 4px 15px rgba(255, 77, 109, 0.4);
        }

        .no-btn {
            background: white;
            color: var(--primary-pink);
            border: 2px solid var(--primary-pink);
            z-index: 100;
        }

        #message-area, #no-message-area {
            display: none;
            margin-top: 20px;
            animation: fadeIn 1s ease-in;
        }

        .signature {
            font-family: 'Dancing Script', cursive;
            font-size: 2em;
            color: var(--primary-pink);
            margin-top: 15px;
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .heart-particle {
            position: absolute;
            pointer-events: none;
            z-index: 1;
        }
    </style>
</head>
<body>

    <audio id="romanticSong" loop>
        <source src="https://www.bensound.com/bensound-music/bensound-love.mp3" type="audio/mpeg">
    </audio>

    <div class="card">
        <h1 id="headline">Will you be my Valentine, Achu? 🌹</h1>

        <div class="btn-container" id="btn-wrap">
            <button class="yes-btn" id="yesBtn" onclick="celebrate()">Yes! 💖</button>
            <button class="no-btn" id="noBtn" onmouseover="teleportButton()" onclick="noClicked()">No 🙊</button>
        </div>

        <div id="message-area">
            <p style="font-size: 1.2em;">My heart just skipped a beat! You’ve made me the happiest person ever. ✨</p>
            <p class="signature">Forever Yours, Divya 💞</p>
        </div>

        <div id="no-message-area">
            <p>Wait... you actually clicked it? 🥺<br><br>
            Are you <i>absolutely</i> sure? My heart is slightly broken!</p>
            <button class="yes-btn" style="margin-top: 10px;" onclick="celebrate()">Okay, I change my mind! 💖</button>
        </div>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
    <script>
        const noBtn = document.getElementById('noBtn');
        const romanticSong = document.getElementById('romanticSong');
        let hoverCount = 0;

        // The button moves when hovered to tease him
        function teleportButton() {
            hoverCount++;
            // It jumps around for 5 tries, then stays still so he can click it
            if (hoverCount < 6) {
                const x = Math.random() * (window.innerWidth - noBtn.offsetWidth - 50);
                const y = Math.random() * (window.innerHeight - noBtn.offsetHeight - 50);
                noBtn.style.position = 'fixed';
                noBtn.style.left = x + 'px';
                noBtn.style.top = y + 'px';
            }
        }

        function noClicked() {
            document.getElementById('btn-wrap').style.display = 'none';
            document.getElementById('headline').innerText = "Oh no! 💔";
            document.getElementById('no-message-area').style.display = 'block';
        }

        function celebrate() {
            // Play Music
            romanticSong.play().catch(e => console.log("Music play pending interaction."));

            // UI Updates
            document.getElementById('btn-wrap').style.display = 'none';
            document.getElementById('no-message-area').style.display = 'none';
            document.getElementById('headline').innerText = "Yay! Best Day Ever! 🥰";
            document.getElementById('message-area').style.display = 'block';

            // Confetti Cannon
            var end = Date.now() + (7 * 1000);
            (function frame() {
              confetti({ particleCount: 3, angle: 60, spread: 55, origin: { x: 0 }, colors: ['#ff4d6d', '#ffffff'] });
              confetti({ particleCount: 3, angle: 120, spread: 55, origin: { x: 1 }, colors: ['#ff4d6d', '#ffffff'] });
              if (Date.now() < end) requestAnimationFrame(frame);
            }());
        }

        // Floating Hearts
        function spawnHeart() {
            const heart = document.createElement("div");
            heart.innerHTML = "❤️";
            heart.classList.add("heart-particle");
            heart.style.left = Math.random() * 100 + "vw";
            heart.style.top = "105vh";
            heart.style.fontSize = (Math.random() * 20 + 10) + "px";
            document.body.appendChild(heart);
            const flow = heart.animate([
                { transform: 'translateY(0)', opacity: 0.8 },
                { transform: `translateY(-110vh) translateX(${Math.random() * 40}px)`, opacity: 0 }
            ], { duration: 6000 });
            flow.onfinish = () => heart.remove();
        }
        setInterval(spawnHeart, 400);
    </script>
</body>
</html>
"""


@app.route("/")
def home():
    return render_template_string(HTML_PAGE)


if __name__ == "__main__":
    # Port 5001 avoids the macOS AirPlay conflict
    app.run(host="0.0.0.0", port=5001, debug=True)