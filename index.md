---
layout: default
title: Home
---

<!-- ================= HEADER SECTION ================= -->
<header class="site-header">
  <div class="header-container">
    
    <!-- Left: Logo -->
    <div class="header-logo">
      <a href="/"><img src="Tour%20With%20Anand%20Logo%20Home.png" alt="Tour With Anand"></a>
    </div>

    <!-- Center: Navigation -->
    <nav class="header-nav">
      <ul>
        <li><a href="#">About<br>Us</a></li>
        <li><a href="#">Kochi Airport Taxi<br>Service</a></li>
        <li><a href="#">Tempo Traveller Rentals In<br>Kochi</a></li>
        <li><a href="#">South India<br>Tours</a></li>
        <li><a href="#">Blog</a></li>
        <li><a href="#">Customer<br>Reviews</a></li>
      </ul>
    </nav>

    <!-- Right: Call Section -->
    <div class="header-phone-section">
      <div class="phone-icon-box">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#ffcc00" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
        </svg>
      </div>
      <div class="phone-text">
        <span class="phone-label">Phone number</span>
        <a href="tel:+919400620615" class="phone-number">+9194006 20615</a>
      </div>
    </div>
  </div>
</header>


<!-- ================= HERO BANNER SECTION ================= -->
<section class="hero-slider">
  <div class="hero-slide active" style="background-image:url('Hero%20Banner%202.png');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>South India Tours & Beyond</h1>
        <p>Kochi Airport–based personalized South India tours with brand new vehicles, premium service, and complete travel support across Kerala and Tamil Nadu.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <div class="hero-slide" style="background-image:url('Hero%20Banner%201.png');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>Kerala & Tamil Nadu Tour Packages</h1>
        <p>Custom holidays and pilgrimage tours across South India.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <div class="hero-slide" style="background-image:url('Hero%20Banner%203.jpg');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>Kochi Airport Taxi Service</h1>
        <p>24×7 airport pickup and drop with professional drivers.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <div class="mobile-hero">
    <video class="mobile-hero-video" autoplay loop muted playsinline poster="Hero%20Banner%202.png">
      <source src="https://tourwithanand.com/wp-content/uploads/2026/06/U_made_a_mistake_U_have_to_rem-online-video-cutter.com_.mp4" type="video/mp4">
    </video>
    <div class="mobile-video-caption">
        <p>Hi Friends, I'm MAXX! Connect with my friend Anand</p>
        <a href="https://wa.me/919400620615" class="mobile-whatsapp-btn">Chat on WhatsApp</a>
    </div>
    <h1>Kochi Airport Taxi Service & South India Tours</h1>
    <p>Tour With Anand provides reliable Kochi Airport taxi services and personalized South India tour packages with private vehicles.</p>
    <div class="mobile-cta">
      <a href="tel:+919400620615" class="call-btn">📞 Call Anand</a>
      <a href="https://wa.me/919400620615" class="whatsapp-btn">💬 Book Now</a>
    </div>
  </div>
</section>


<!-- ================= STYLES ================= -->
<style>
/* --- REMOVE GITHUB DEFAULTS --- */
html, body { margin: 0 !important; padding: 0 !important; background-color: #21242b; }
.page-header, .project-name, .project-tagline, header:not(.site-header), .main-content { display: none !important; }
.wrapper { max-width: 100% !important; padding: 0 !important; margin: 0 !important; }

/* --- HEADER STYLES --- */
.site-header {
  position: absolute; /* Place on top of the banner */
  top: 0;
  left: 0;
  width: 100%;
  z-index: 100;
  background-color: rgba(33, 36, 43, 0.9); /* Slight transparency for elegance */
  border-bottom: 1px solid rgba(255,255,255,0.1);
  padding: 10px 0;
}

.header-container {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 40px;
}

.header-logo img { height: 50px; display: block; }
.header-nav ul { display: flex; gap: 30px; list-style: none; margin: 0; padding: 0; }
.header-nav a { color: #ffffff; text-decoration: none; font-size: 13px; line-height: 1.2; font-weight: 500; }
.header-nav a:hover { color: #ffcc00; }

.header-phone-section { display: flex; align-items: center; gap: 10px; }
.phone-icon-box { border: 1px solid #ffcc00; padding: 8px; border-radius: 50%; display: flex; }
.phone-text { display: flex; flex-direction: column; }
.phone-label { font-size: 10px; color: #a0a0a0; }
.phone-number { font-size: 14px; font-weight: bold; color: #ffffff; text-decoration: none; }

/* --- HERO STYLES --- */
.hero-slider { position: relative; height: 100vh; overflow: hidden; width: 100%; }
.hero-slide { position: absolute; inset: 0; background-size: cover; background-position: top center; opacity: 0; transition: opacity 1.2s ease; }
.hero-slide.active { opacity: 1; }
.hero-overlay { height: 100%; background: linear-gradient(to right, rgba(0,0,0,0.7), rgba(0,0,0,0.1)); display: flex; align-items: center; }
.hero-content { max-width: 600px; padding: 40px 100px; color: #fff; }
.hero-content h1 { font-size: 44px; color: #ffcc00; margin-bottom: 15px; }
.hero-btn { background: #ffcc00; color: #000; padding: 12px 30px; border-radius: 30px; font-weight: 700; text-decoration: none; display: inline-block; }

/* --- MOBILE STYLES --- */
.mobile-hero { display: none; padding: 80px 20px; text-align: center; color: #fff; background: #000; }
@media (max-width: 1000px) {
  .header-nav { display: none; }
  .hero-slide { display: none; }
  .mobile-hero { display: block; }
}
</style>

<script>
const slides = document.querySelectorAll(".hero-slide");
let current = 0;
setInterval(() => {
  slides[current].classList.remove("active");
  current = (current + 1) % slides.length;
  slides[current].classList.add("active");
}, 5000);
</script>
