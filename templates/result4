<!DOCTYPE html>
<html>
<head>
  <title>You are</title>
  <link href="https://fonts.googleapis.com/css2?family=Londrina+Outline&family=Press+Start+2P&display=swap" rel="stylesheet">

  <style>
    body {
      margin: 3rem 5rem;
      min-height: 100vh;
      background: #D8EAE2;
      position: relative;
      overflow: auto;
    }



    .lava-lamp {
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;

  background:
    radial-gradient(circle at 20% 30%, rgba(255, 0, 170, 0.35), transparent 45%),
    radial-gradient(circle at 70% 20%, rgba(0, 255, 180, 0.35), transparent 50%),
    radial-gradient(circle at 40% 80%, rgba(255, 180, 0, 0.30), transparent 55%),
    radial-gradient(circle at 85% 70%, rgba(120, 0, 255, 0.30), transparent 50%),
    #D8EAE2;

  background-size: 200% 200%;
  filter: blur(35px) saturate(140%);
  animation: lavaMove 20s ease-in-out infinite;
}


    @keyframes lavaMove {
  0%   { background-position: 0% 50%; }
  25%  { background-position: 0% 70%; }
  50%  { background-position: 0% 90%; }
  75%  { background-position: 20% 100%; }
  100% { background-position: 0% 50%; }
}

    .content {
      position: relative;
      z-index: 1;
      padding: 3rem;
      text-align: center;
    }

    .groovy-title {
      font-family: Impact, sans-serif;
      font-size: 4rem;
      color: #318963;
      text-shadow: 3px 3px 0 #2d1b00, -1px -1px 0 #ffd700;
      letter-spacing: -2px;
    }

    @keyframes pulse {
      0%   { transform: scale(1) skew(-5deg); }
      50%  { transform: scale(1.05) skew(-5deg); }
      100% { transform: scale(1) skew(-5deg); }
    }

    .groovy-title {
      animation: pulse 2s infinite;
    }

    .arcade-text {
      font-family: 'Press Start 2P', cursive;
      color: green;
      font-size: 1rem;
      line-height: 1.5;
      display: inline-block;
      margin-top: 2rem;
      text-decoration: none;
    }
  </style>
</head>

<body>
  <div class="lava-lamp"></div>

  <div class="content">
    <!-- NAME OF THE BAND MEMBER -->
    <h1 class="groovy-title">Joey</h1>

    <img src="{{ url_for('static', filename='joey.jpg') }}"
         alt="Joey"
         width="400">

    <br>
     <a class = "arcade-text" href= "{{ song }}" target="_blank">

            A song you will probably like
            </a>
    <br>


    <a href="/" class="arcade-text">NO I AINT</a>
    <br>
     <br>
    <p class = "arcade-text"> You are:</p>
    <br>
    <p class="arcade-text">{{ ratio ['Stu']}} % a Stu</p>
<p class="arcade-text">{{ ratio['Cookie'] }} % a Cookie</p>
<p class="arcade-text">{{ ratio['Ambie'] }} % an Ambie</p>
<p class="arcade-text">{{ ratio['Joey'] }} % a Joey</p>
<br>
    <br>
    <a href="/" class = "groovy-title">NO I AINT</a>
    <br>
    <br>
    <p class = "arcade-text"> Did you know that:</p>
    <br>
    <p class="arcade-text">{{ (stats['Stu'] / stats['All'] * 100) | round(0) }} % are Stus</p>
<p class="arcade-text">{{ (stats['Cookie'] / stats['All'] * 100) | round(0) }} % are Cookies</p>
<p class="arcade-text">{{ (stats['Ambie'] / stats['All'] * 100) | round(0) }} % are Ambies</p>
<p class="arcade-text">{{ (stats['Joey'] / stats['All'] * 100) | round(0) }} % are Joeys</p>

  </div>
</body>
</html>
