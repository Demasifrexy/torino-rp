# ============================================================
#              TORINO RP - EH 🇮🇹
#       SITO WEB COMPLETO IN UN SOLO FILE PYTHON
#                    Creato da Disprezzare
# ============================================================

from http.server import HTTPServer, BaseHTTPRequestHandler
import threading
import webbrowser
import socket
import os
import time

# ================= CONFIGURAZIONE =================

HOST = "0.0.0.0"
PORT = 8080

SERVER_NAME = "TORINO RP - EH 🇮🇹"
CREATOR = "Disprezzare"

DISCORD_INVITE = "https://discord.gg/FFXsZGQjQ"
DISCORD_GUILD_ID = "1558619825792745512"

ROBLOX_LINK = "https://www.roblox.com/share/g/837872239"

RULES_LINK = (
    "https://docs.google.com/document/d/"
    "1GLTRrrG32VU0DK5LZe_15RrHJxReKb5hvJucQUkvRH0/edit?usp=sharing"
)

TIKTOK_LINK = (
    "https://www.tiktok.com/@disprezzareofficial0"
    "?_r=1&_t=ZN-9AokTrwFcNa"
)

# ============================================================
#                    PAGINA WEB
# ============================================================

HTML = r"""<!DOCTYPE html>
<html lang="it">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="theme-color" content="#080b12">
<title>TORINO RP - EH 🇮🇹</title>

<style>
:root {
  --bg: #080b12;
  --panel: #121a29;
  --red: #ff3449;
  --gold: #ffca70;
  --text: #f5f7fc;
  --muted: #aab3c5;
}

* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: smooth;
}

body {
  background: var(--bg);
  color: var(--text);
  font-family: Arial, sans-serif;
  overflow-x: hidden;
}

a {
  color: inherit;
  text-decoration: none;
}

button {
  font-family: inherit;
}

.navbar {
  position: sticky;
  top: 0;
  z-index: 10;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 12px;
  padding: 18px 7%;
  background: rgba(8, 11, 18, .92);
  backdrop-filter: blur(15px);
  border-bottom: 1px solid #ffffff18;
}

.logo {
  font-size: 19px;
  font-weight: 900;
  letter-spacing: 2px;
}

.logo span {
  color: var(--red);
}

.navlinks {
  display: flex;
  gap: 18px;
  font-size: 13px;
  color: var(--muted);
}

.navlinks a:hover {
  color: white;
}

.hero {
  min-height: 92vh;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 70px 20px;
  position: relative;
  overflow: hidden;
  background:
    radial-gradient(ellipse at 15% 20%, #ff344922, transparent 40%),
    radial-gradient(ellipse at 90% 80%, #365bff22, transparent 40%),
    linear-gradient(160deg, #111827, #080b12 75%);
}

.hero::before {
  content: "";
  position: absolute;
  width: 280px;
  height: 280px;
  border-radius: 50%;
  background: #ff3449;
  filter: blur(110px);
  opacity: .2;
  animation: float 6s infinite alternate ease-in-out;
}

.hero-content {
  position: relative;
  max-width: 900px;
  animation: entrance 1s ease-out;
}

.badge {
  display: inline-block;
  border: 1px solid #ffffff25;
  background: #ffffff08;
  padding: 10px 17px;
  border-radius: 30px;
  font-size: 12px;
  letter-spacing: 2px;
}

h1 {
  margin: 28px 0 20px;
  font-size: clamp(43px, 9vw, 100px);
  line-height: 1;
  font-weight: 1000;
  letter-spacing: -4px;
}

.gradient {
  background: linear-gradient(90deg, white, #ff596a, #ffd17a, white);
  background-size: 250%;
  color: transparent;
  background-clip: text;
  -webkit-background-clip: text;
  animation: shimmer 5s linear infinite;
}

.subtitle {
  max-width: 700px;
  margin: auto;
  color: var(--muted);
  font-size: 17px;
  line-height: 1.8;
}

.buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 13px;
  justify-content: center;
  margin-top: 30px;
}

.btn {
  border: 0;
  border-radius: 12px;
  padding: 15px 23px;
  font-size: 14px;
  font-weight: bold;
  cursor: pointer;
  transition: .25s;
  display: inline-block;
}

.btn:hover {
  transform: translateY(-4px);
  filter: brightness(1.15);
}

.btn-red {
  color: white;
  background: linear-gradient(120deg, #ff3449, #c81730);
  box-shadow: 0 8px 30px #ff344933;
}

.btn-dark {
  color: white;
  border: 1px solid #ffffff30;
  background: #ffffff08;
}

.stats {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 13px;
  margin-top: 40px;
}

.stat {
  min-width: 130px;
  padding: 18px;
  background: #ffffff08;
  border: 1px solid #ffffff17;
  border-radius: 15px;
}

.stat strong {
  display: block;
  font-size: 28px;
  margin-bottom: 5px;
}

.stat small {
  color: var(--muted);
}

.online {
  color: #39e69a;
}

.offline {
  color: #b5bfd0;
}

.status-note {
  margin-top: 15px;
  font-size: 12px;
  color: #8490a5;
}

section {
  max-width: 1150px;
  padding: 80px 22px;
  margin: auto;
}

.section-title {
  text-align: center;
  margin-bottom: 35px;
}

.section-title small {
  color: var(--red);
  font-weight: bold;
  letter-spacing: 4px;
}

.section-title h2 {
  font-size: clamp(30px, 5vw, 48px);
  margin: 14px 0;
}

.section-title p {
  color: var(--muted);
  line-height: 1.7;
}

.panel {
  padding: clamp(22px, 5vw, 40px);
  background: linear-gradient(140deg, #172033, #0d121d);
  border: 1px solid #ffffff15;
  border-radius: 22px;
  box-shadow: 0 20px 70px #0003;
}

.panel h2 {
  margin-bottom: 15px;
}

.panel h3 {
  margin: 24px 0 10px;
}

.panel p {
  color: #c1cada;
  line-height: 1.9;
  margin-bottom: 15px;
}

.cards {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 16px;
}

.card {
  padding: 25px;
  background: #ffffff06;
  border: 1px solid #ffffff15;
  border-radius: 18px;
  transition: .3s;
}

.card:hover {
  transform: translateY(-5px);
  border-color: #ff344988;
  background: #ffffff0b;
}

.card .icon {
  font-size: 32px;
}

.card h3 {
  margin: 15px 0 10px;
}

.card p {
  color: var(--muted);
  line-height: 1.7;
}

.notice {
  padding: 20px;
  margin-top: 22px;
  background: #ff344910;
  border: 1px solid #ff344955;
  border-radius: 15px;
  color: #ffdce0;
  line-height: 1.8;
}

.links {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 15px;
}

.link-card {
  padding: 24px;
  background: #ffffff06;
  border: 1px solid #ffffff18;
  border-radius: 17px;
  transition: .3s;
}

.link-card:hover {
  transform: translateY(-4px);
  border-color: #ff344988;
}

.link-card .icon {
  font-size: 30px;
}

.link-card h3 {
  margin: 12px 0;
}

.link-card p {
  color: var(--muted);
  line-height: 1.6;
  font-size: 14px;
}

footer {
  text-align: center;
  padding: 35px 20px;
  border-top: 1px solid #ffffff15;
  color: var(--muted);
  line-height: 2;
  font-size: 13px;
}

footer strong {
  color: white;
}

.sound-button {
  position: fixed;
  right: 15px;
  bottom: 15px;
  z-index: 12;
  background: #172033;
  color: white;
  border: 1px solid #ffffff25;
  padding: 13px 17px;
  border-radius: 30px;
  cursor: pointer;
}

.reveal {
  opacity: 0;
  transform: translateY(25px);
  transition: .8s;
}

.reveal.visible {
  opacity: 1;
  transform: translateY(0);
}

.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 100;
  display: none;
  place-items: center;
  padding: 20px;
  background: #03050bee;
  backdrop-filter: blur(12px);
}

.modal-backdrop.show {
  display: grid;
  animation: entrance .3s;
}

.modal {
  width: 100%;
  max-width: 540px;
  padding: 28px;
  text-align: center;
  border-radius: 22px;
  border: 1px solid #ff344966;
  background: linear-gradient(145deg, #192033, #090d16);
  box-shadow: 0 20px 90px #0009;
}

.modal h2 {
  margin: 12px 0;
}

.modal p {
  color: #c2cada;
  line-height: 1.8;
  margin: 12px 0;
}

.timer {
  font-size: 35px;
  color: var(--gold);
  font-weight: 900;
  margin: 18px;
}

#continueButton {
  width: 100%;
}

#continueButton:disabled {
  opacity: .4;
  cursor: not-allowed;
}

@keyframes entrance {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes float {
  from { transform: translate(-20px, -10px); }
  to { transform: translate(30px, 35px); }
}

@keyframes shimmer {
  to { background-position: 250% center; }
}

@media (max-width: 650px) {
  .navlinks {
    gap: 10px;
    font-size: 11px;
  }

  .navlinks a:nth-child(2) {
    display: none;
  }

  .cards,
  .links {
    grid-template-columns: 1fr;
  }

  h1 {
    letter-spacing: -2px;
  }
}
</style>
</head>

<body>

<nav class="navbar">
  <a class="logo" href="#home">TORINO <span>RP</span> 🇮🇹</a>
  <div class="navlinks">
    <a href="#chi-siamo">Chi siamo</a>
    <a href="#opportunita">Opportunità</a>
    <a href="#link">Link ufficiali</a>
  </div>
</nav>

<header class="hero" id="home">
  <div class="hero-content">
    <div class="badge">🇮🇹 COMMUNITY ROLEPLAY ITALIA</div>

    <h1><span class="gradient">TORINO RP</span><br>— EH 🇮🇹</h1>

    <p class="subtitle">
      Realismo, professionalità e una nuova esperienza di Roleplay.
      La tua storia comincia qui: entra in città e diventa parte
      della community.
    </p>

    <div class="buttons">
      <a class="btn btn-red" href="https://discord.gg/FFXsZGQjQ"
         target="_blank" rel="noopener">💬 ENTRA NEL DISCORD</a>
      <button class="btn btn-dark" id="discoverButton">
        ✨ SCOPRI DI PIÙ
      </button>
    </div>

    <div class="stats">
      <div class="stat">
        <strong class="online" id="onlineCount">—</strong>
        <small>🟢 Utenti online</small>
      </div>
      <div class="stat">
        <strong class="offline" id="offlineCount">—</strong>
        <small>⚪ Utenti offline</small>
      </div>
      <div class="stat">
        <strong id="totalCount">—</strong>
        <small>👥 Membri totali</small>
      </div>
    </div>

    <p class="status-note" id="statusNote">
      Caricamento dati Discord...
    </p>
  </div>
</header>

<section id="chi-siamo" class="reveal">
  <div class="section-title">
    <small>LA NOSTRA IDENTITÀ</small>
    <h2>👑 Chi siamo</h2>
    <p>Una città, tante storie da vivere.</p>
  </div>

  <div class="panel">
    <h2>👑 TORINO R.P. 🇮🇹</h2>
    <h3>Realismo, professionalità e una nuova esperienza di Roleplay.</h3>

    <p>
      Benvenuti su Torino Full RP, un progetto dedicato a chi desidera
      vivere un'esperienza di Roleplay immersiva, strutturata e realistica,
      ambientata nella città di Torino.
    </p>

    <p>
      Il nostro obiettivo è offrire un ambiente organizzato e coinvolgente,
      nel quale ogni giocatore possa sviluppare il proprio personaggio,
      intraprendere un percorso professionale e contribuire attivamente
      alla crescita della città.
    </p>

    <h3>🎯 LA NOSTRA VISIONE</h3>
    <p>
      Torino Full RP punta a promuovere un Roleplay di qualità, fondato
      su regole chiare, serietà, rispetto reciproco e collaborazione
      tra giocatori e staff.
    </p>

    <p>
      Ogni personaggio ha una storia da raccontare. Ogni scelta può aprire
      nuove possibilità. Ogni giocatore contribuisce a rendere la città
      un ambiente dinamico e credibile.
    </p>

    <h3>🤝 ENTRA NELLA COMMUNITY</h3>
    <p>
      Che tu voglia intraprendere una carriera nelle istituzioni, avviare
      un'attività o semplicemente costruire la tua storia, Torino Full RP
      ti offre l'opportunità di diventare parte di una community
      in continua evoluzione.
    </p>
  </div>
</section>

<section id="opportunita" class="reveal">
  <div class="section-title">
    <small>COSTRUISCI LA TUA STORIA</small>
    <h2>⚖️ Le nostre opportunità</h2>
    <p>Scegli il tuo percorso e contribuisci alla vita della città.</p>
  </div>

  <div class="cards">
    <article class="card">
      <div class="icon">🚔</div>
      <h3>Forze dell'Ordine</h3>
      <p>
        Entra nei corpi di sicurezza, garantisci il rispetto della legge
        e contribuisci alla tutela dei cittadini.
      </p>
    </article>

    <article class="card">
      <div class="icon">🚑</div>
      <h3>Servizi di Emergenza</h3>
      <p>
        Unisciti ai servizi sanitari e di soccorso e offri assistenza
        alla popolazione nelle situazioni di necessità.
      </p>
    </article>

    <article class="card">
      <div class="icon">🏢</div>
      <h3>Lavoro ed Economia</h3>
      <p>
        Sviluppa la tua carriera, entra nel mondo imprenditoriale
        e costruisci il tuo futuro attraverso opportunità lavorative.
      </p>
    </article>

    <article class="card">
      <div class="icon">🏙️</div>
      <h3>Vita Quotidiana</h3>
      <p>
        Interagisci con gli altri cittadini, partecipa alle attività
        della città e crea esperienze di gioco coinvolgenti.
      </p>
    </article>
  </div>

  <div class="notice">
    🌅 <strong>Staff H24</strong> — niente stress, solo divertimento
    e Roleplay pulito, con l'obiettivo di puntare al 10/10! 🍂
    <br><br>
    ⚠️ <strong>Per entrare in game è obbligatorio entrare nel Discord.</strong>
  </div>
</section>

<section id="link" class="reveal">
  <div class="section-title">
    <small>UNISCITI A NOI</small>
    <h2>🔗 Link ufficiali</h2>
    <p>Tutti i collegamenti utili per entrare nella community.</p>
  </div>

  <div class="links">
    <a class="link-card" href="https://discord.gg/FFXsZGQjQ"
       target="_blank" rel="noopener">
      <div class="icon">💬</div>
      <h3>Server Discord</h3>
      <p>Entra nel server ufficiale di Torino RP.</p>
    </a>

    <a class="link-card" href="https://www.roblox.com/share/g/837872239"
       target="_blank" rel="noopener">
      <div class="icon">🎮</div>
      <h3>Community Roblox</h3>
      <p>Visita la community Roblox di Torino RP.</p>
    </a>

    <a class="link-card"
       href="https://docs.google.com/document/d/1GLTRrrG32VU0DK5LZe_15RrHJxReKb5hvJucQUkvRH0/edit?usp=sharing"
       target="_blank" rel="noopener">
      <div class="icon">📜</div>
      <h3>Regolamento ufficiale</h3>
      <p>Consulta il regolamento attualmente in vigore.</p>
    </a>

    <a class="link-card"
       href="https://www.tiktok.com/@disprezzareofficial0?_r=1&_t=ZN-9AokTrwFcNa"
       target="_blank" rel="noopener">
      <div class="icon">🎵</div>
      <h3>TikTok secondario</h3>
      <p>Seguici su TikTok.</p>
    </a>
  </div>
</section>

<footer>
  <p>Sito creato da <strong>Disprezzare</strong> ©</p>
  <p>© Tutti i diritti riservati a Torino RP.</p>
  <p>TORINO RP - EH 🇮🇹</p>
  <p style="font-size:11px">
    I servizi esterni sono soggetti alle rispettive informative sulla privacy.
  </p>
</footer>

<button class="sound-button" id="soundButton">🔊 Suoni: OFF</button>

<div class="modal-backdrop" id="warningModal">
  <div class="modal">
    <div style="font-size:35px">⚠️</div>
    <h2>AVVISO IMPORTANTE</h2>

    <p>
      Questo sito è dedicato alla community TORINO RP.
      La copia o l'utilizzo non autorizzato dei suoi contenuti può essere
      segnalato alle piattaforme competenti e, ove applicabile, alle autorità.
    </p>

    <p>
      Questa pagina non contiene moduli per raccogliere dati personali.
      Discord, TikTok, Roblox e Google Docs sono servizi esterni con
      le proprie informative sulla privacy.
    </p>

    <p><strong>Buon inizio e buon Roleplay! 😁</strong></p>

    <div class="timer" id="timer">10</div>
    <button class="btn btn-red" id="continueButton" disabled>
      CONTINUA (10)
    </button>
  </div>
</div>

<script>
let soundEnabled = false;
let audioContext = null;

function playSound(frequency = 600) {
  if (!soundEnabled) return;

  try {
    audioContext ||= new (
      window.AudioContext || window.webkitAudioContext
    )();

    const oscillator = audioContext.createOscillator();
    const gain = audioContext.createGain();

    oscillator.type = "sine";
    oscillator.frequency.value = frequency;
    gain.gain.value = 0.04;

    oscillator.connect(gain);
    gain.connect(audioContext.destination);
    oscillator.start();

    gain.gain.exponentialRampToValueAtTime(
      0.001, audioContext.currentTime + 0.12
    );

    oscillator.stop(audioContext.currentTime + 0.12);
  } catch (error) {
    console.log("Audio non disponibile");
  }
}

document.getElementById("soundButton").addEventListener("click", () => {
  soundEnabled = !soundEnabled;

  document.getElementById("soundButton").textContent =
    soundEnabled ? "🔊 Suoni: ON" : "🔊 Suoni: OFF";

  playSound(750);
});

const warningModal = document.getElementById("warningModal");
const discoverButton = document.getElementById("discoverButton");
const timerElement = document.getElementById("timer");
const continueButton = document.getElementById("continueButton");

let countdown = null;

discoverButton.addEventListener("click", () => {
  warningModal.classList.add("show");

  clearInterval(countdown);

  let seconds = 10;
  timerElement.textContent = seconds;
  continueButton.disabled = true;
  continueButton.textContent = "CONTINUA (10)";

  countdown = setInterval(() => {
    seconds--;
    timerElement.textContent = seconds;

    continueButton.textContent =
      seconds > 0 ? `CONTINUA (${seconds})` : "CONTINUA";

    if (seconds <= 0) {
      clearInterval(countdown);
      continueButton.disabled = false;
      playSound(800);
    }
  }, 1000);
});

continueButton.addEventListener("click", () => {
  if (continueButton.disabled) return;

  warningModal.classList.remove("show");

  document.getElementById("chi-siamo").scrollIntoView({
    behavior: "smooth"
  });

  playSound(700);
});

const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add("visible");
      observer.unobserve(entry.target);
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll(".reveal").forEach(element => {
  observer.observe(element);
});

/*
Il widget Discord pubblico può mostrare le presenze online,
ma non restituisce necessariamente il numero totale o gli offline.
*/

async function loadDiscordStats() {
  const online = document.getElementById("onlineCount");
  const offline = document.getElementById("offlineCount");
  const total = document.getElementById("totalCount");
  const note = document.getElementById("statusNote");

  try {
    const response = await fetch(
      "https://discord.com/api/guilds/1558619825792745512/widget.json",
      { cache: "no-store" }
    );

    if (!response.ok) {
      throw new Error("Widget non disponibile");
    }

    const data = await response.json();

    online.textContent =
      Number(data.presence_count || 0).toLocaleString("it-IT");

    offline.textContent = "—";
    total.textContent = "—";

    note.textContent =
      "Presenze online dal widget pubblico Discord.";
  } catch (error) {
    online.textContent = "—";
    offline.textContent = "—";
    total.textContent = "—";

    note.textContent =
      "Per mostrare le presenze, attiva il widget pubblico di Discord.";
  }
}

loadDiscordStats();
setInterval(loadDiscordStats, 60000);

document.querySelectorAll("a").forEach(element => {
  element.addEventListener("click", () => playSound(500));
});
</script>

</body>
</html>
"""

# ============================================================
#                    SERVER PYTHON
# ============================================================

class TorinoHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path not in ("/", "/index.html"):
            self.send_error(404, "Pagina non trovata")
            return

        content = HTML.encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(content)))
        self.send_header("Cache-Control", "no-cache")
        self.end_headers()

        self.wfile.write(content)

    def log_message(self, format, *args):
        print("[TORINO RP]", format % args)


def get_local_ip():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        sock.connect(("8.8.8.8", 80))
        return sock.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        sock.close()


def main():
    print("=" * 50)
    print("       TORINO RP - EH 🇮🇹")
    print("       SITO WEB IN PYDROID 3")
    print("=" * 50)

    try:
        server = HTTPServer((HOST, PORT), TorinoHandler)
    except OSError as error:
        print("ERRORE: impossibile avviare il server.")
        print("Dettagli:", error)
        print("Prova a cambiare PORT = 8080 in PORT = 8081.")
        return

    print()
    print("SITO AVVIATO CORRETTAMENTE!")
    print()
    print("Aprilo nel browser del dispositivo:")
    print(f"http://127.0.0.1:{PORT}")
    print()
    print("Indirizzo locale della rete Wi-Fi:")
    print(f"http://{get_local_ip()}:{PORT}")
    print()
    print("Per fermare il sito premi Stop in Pydroid 3.")
    print("=" * 50)

    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nArresto del sito...")
    finally:
        server.server_close()
        print("Server fermato.")


if __name__ == "__main__":
    main()