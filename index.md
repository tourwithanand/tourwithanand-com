---
layout: default
title: Home
---

<header class="site-header">
  <div class="header-container">
    
    <div class="header-logo">
      <a href="/"><img src="Tour%20With%20Anand%20Logo%20Home.png" alt="Tour With Anand"></a>
    </div>

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


<style>
/* --- 1. AGGRESSIVE GITHUB THEME OVERRIDES --- */
/* Hide ALL default GitHub headers, titles, and text */
header:not(.site-header), .page-header, h1.project-name, h2.project-tagline {
    display: none !important;
}

/* Force the GitHub container to allow full-width elements */
.markdown-body, .container, .container-lg, .wrapper {
    max-width: 100% !important;
    width: 100% !important;
    padding: 0 !important;
    margin: 0 !important;
}

body, html {
    margin: 0 !important;
    padding: 0 !important;
    background-color: #21242b !important;
    overflow-x: hidden;
}

/* --- 2. CUSTOM HEADER STYLES --- */
.site-header {
    width: 100vw !important;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    background-color: #21242b;
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    padding: 10px 0;
    z-index: 100;
}

.header-container {
    max-width: 1400px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 0 40px;
    box-sizing: border-box;
}

/* Logo Background Fix */
.header-logo img { 
    height: 55px; 
    display: block; 
    background: transparent !important; 
    background-color: transparent !important;
    border: none !important;
}

.header-nav ul { display: flex; gap: 30px; list-style: none; margin: 0; padding: 0; }
.header-nav a { color: #ffffff; text-decoration: none; font-size: 13px; line-height: 1.2; font-weight: 500; }
.header-nav a:hover { color: #ffcc00; }

.header-phone-section { display: flex; align-items: center; gap: 10px; }
.phone-icon-box { border: 1px solid rgba(255, 255, 255, 0.15); padding: 8px; border-radius: 6px; display: flex; }
.phone-text { display: flex; flex-direction: column; }
.phone-label { font-size: 10px; color: #a0a0a0; margin-bottom: 2px; }
.phone-number { font-size: 14px; font-weight: bold; color: #ffffff; text-decoration: none; }
.phone-number:hover { color: #ffcc00; }

/* --- 3. HERO SLIDER STYLES --- */
.hero-slider { 
    width: 100vw !important;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    height: 85vh; 
    overflow: hidden; 
}

.hero-slide { 
    position: absolute; 
    inset: 0; 
    background-size: cover; 
    background-position: center; 
    opacity: 0; 
    transition: opacity 1.2s ease; 
}

.hero-slide.active { opacity: 1; }

.hero-overlay { 
    height: 100%; 
    background: linear-gradient(to right, rgba(0,0,0,0.85), rgba(0,0,0,0.25)); 
    display: flex; 
    align-items: center; 
}

.hero-content { max-width: 650px; padding: 40px 80px; color: #fff; }
.hero-content h1 { font-size: 46px; color: #ffcc00; margin-bottom: 15px; margin-top: 0; line-height: 1.1; }
.hero-content p { font-size: 18px; margin: 0 0 25px 0; line-height: 1.5; color: #f0f0f0; }
.hero-btn { background: linear-gradient(135deg, #ffcc00, #e6b800); color: #000; padding: 14px 34px; border-radius: 35px; font-weight: 700; text-decoration: none; display: inline-block; }

/* --- 4. MOBILE STYLES --- */
.mobile-hero { 
    display: none; 
    width: 100vw !important;
    position: relative;
    left: 50%;
    transform: translateX(-50%);
    padding: 60px 20px; 
    text-align: center; 
    color: #fff; 
    background: #000; 
}

.mobile-hero-video { width: 100%; max-width: 400px; height: auto; margin: 0 auto 10px; display: block; border-radius: 8px; }
.mobile-video-caption { background-color: #111; padding: 15px; margin-bottom: 25px; border-radius: 8px; }
.mobile-video-caption p { color: #fff; font-size: 16px; font-weight: 700; margin: 0 0 10px 0; }
.mobile-whatsapp-btn { display: inline-block; background-color: #25D366; color: #000; padding: 10px 20px; border-radius: 50px; font-weight: 700; text-decoration: none; font-size: 14px; }
.mobile-hero h1 { color: #ffcc00; font-size: 28px; margin-bottom: 14px; margin-top: 0; }
.mobile-hero p { font-size: 15px; line-height: 1.6; color: #e0e0e0; margin-bottom: 30px; }
.mobile-cta { display: flex; flex-direction: column; gap: 14px; align-items: center; }
.call-btn, .whatsapp-btn { width: 100%; max-width: 300px; padding: 14px; border-radius: 40px; font-weight: 700; text-decoration: none; }
.call-btn { border: 2px solid #ffcc00; color: #ffcc00; }
.whatsapp-btn { background: linear-gradient(135deg, #ffcc00, #e6b800); color: #000; }

/* RESPONSIVE QUERIES */
@media (max-width: 1100px) {
  .header-nav { display: none; }
  .header-container { justify-content: space-around; }
}
@media (max-width: 768px) {
  .hero-slide { display: none; }
  .mobile-hero { display: block; }
  .hero-slider { height: auto; }
  .header-phone-section { display: none; }
  .header-container { justify-content: center; padding: 15px; }
}
</style>

<script>
const slides = document.querySelectorAll(".hero-slide");
let current = 0;
if (window.innerWidth > 768) {
  setInterval(() => {
    slides[current].classList.remove("active");
    current = (current + 1) % slides.length;
    slides[current].classList.add("active");
  }, 5000);
}
</script>
