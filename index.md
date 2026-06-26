---
layout: default
title: Home
---

<!-- ================= HEADER SECTION ================= -->
<header class="site-header">
  <div class="header-container">
    
    <!-- Left: Logo -->
    <div class="header-logo">
      <a href="/"><img src="Logo%20Plain.png" alt="Tour With Anand"></a>
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

  <!-- Desktop Slide 1 -->
  <div class="hero-slide active" style="background-image:url('Hero%20Banner%202.png');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>South India Tours & Beyond</h1>
        <p>Kochi Airport–based personalized South India tours with brand new vehicles, premium service, and complete travel support across Kerala and Tamil Nadu.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <!-- Desktop Slide 2 -->
  <div class="hero-slide" style="background-image:url('Hero%20Banner%201.png');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>Kerala & Tamil Nadu Tour Packages</h1>
        <p>Custom holidays and pilgrimage tours across South India.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <!-- Desktop Slide 3 -->
  <div class="hero-slide" style="background-image:url('Hero%20Banner%203.jpg');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>Kochi Airport Taxi Service</h1>
        <p>24×7 airport pickup and drop with professional drivers.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <!-- Mobile Hero Section -->
  <div class="mobile-hero">
    <video class="mobile-hero-video" autoplay loop muted playsinline poster="Hero%20Banner%202.png">
      <source src="https://tourwithanand.com/wp-content/uploads/2026/06/U_made_a_mistake_U_have_to_rem-online-video-cutter.com_.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

    <div class="mobile-video-caption">
        <p>Hi Friends, I'm MAXX! Connect with my friend Anand</p>
        <a href="https://wa.me/919400620615" class="mobile-whatsapp-btn" target="_blank" rel="noopener">
          Chat on WhatsApp
        </a>
    </div>
    
    <h1>Kochi Airport Taxi Service & South India Tours</h1>

    <p>
      Tour With Anand provides reliable Kochi Airport taxi services and personalized South India tour packages with private vehicles. We offer safe airport pickup and drop, premium travel comfort, and complete travel support across Kerala and Tamil Nadu.
    </p>

    <div class="mobile-cta">
      <a href="tel:+919400620615" class="call-btn">📞 Call Anand</a>
      <a href="https://wa.me/919400620615" class="whatsapp-btn">💬 Book Now</a>
    </div>
  </div>

</section>


<!-- ================= STYLES ================= -->
<style>
/* --- HEADER STYLES --- */
.site-header {
  background-color: #21242b;
  font-family: Arial, sans-serif;
  
  /* Screen width fix applied to header */
  width: 100vw;
  max-width: 100vw;
  margin-left: calc(-50vw + 50%);
  border-bottom: 2px solid #1a1c22;
}

.header-container {
  max-width: 1400px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 15px 40px;
}

.header-logo img {
  height: 55px; /* Adjust this value if your logo needs to be larger/smaller */
  display: block;
}

.header-nav ul {
  display: flex;
  gap: 35px;
  list-style: none;
  margin: 0;
  padding: 0;
  align-items: center;
}

.header-nav a {
  color: #ffffff;
  text-decoration: none;
  font-size: 14px;
  line-height: 1.3;
  text-align: left;
  display: block;
  transition: color 0.3s ease;
}

.header-nav a:hover {
  color: #ffcc00;
}

.header-phone-section {
  display: flex;
  align-items: center;
  gap: 15px;
}

.phone-icon-box {
  border: 1px solid rgba(255, 255, 255, 0.15);
  padding: 10px;
  border-radius: 6px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.phone-text {
  display: flex;
  flex-direction: column;
}

.phone-label {
  font-size: 12px;
  color: #a0a0a0;
  margin-bottom: 3px;
}

.phone-number {
  font-size: 16px;
  font-weight: bold;
  color: #ffffff;
  text-decoration: none;
}

.phone-number:hover {
  color: #ffcc00;
}

/* --- HERO STYLES --- */
.hero-slider {
  position: relative;
  height: 85vh; /* slightly reduced to account for new header height */
  overflow: hidden;
  /* Screen width fix */
  width: 100vw;
  max-width: 100vw;
  margin-left: calc(-50vw + 50%);
}

.hero-slide {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  opacity: 0;
  transition: opacity 1.2s ease;
}

.hero-slide.active {
  opacity: 1;
}

.hero-overlay {
  height: 100%;
  background: linear-gradient(to right, rgba(0,0,0,0.85), rgba(0,0,0,0.25));
  display: flex;
  align-items: center;
}

.hero-content {
  max-width: 650px;
  padding: 60px;
  color: #fff;
}

.hero-content h1 {
  font-size: 46px;
  color: #ffcc00;
  margin-bottom: 20px;
  margin-top: 0;
}

.hero-content p {
  font-size: 18px;
  margin: 18px 0 28px;
}

.hero-btn {
  background: linear-gradient(135deg, #ffcc00, #e6b800);
  color: #000;
  padding: 14px 34px;
  border-radius: 35px;
  font-weight: 700;
  text-decoration: none;
  display: inline-block;
}

/* --- MOBILE STYLES --- */
.mobile-hero {
  display: none;
  padding: 40px 20px;
  text-align: center;
  color: #fff;
  background: linear-gradient(180deg, #0b0f14, #000);
  width: 100vw;
  max-width: 100vw;
  margin-left: calc(-50vw + 50%);
}

.mobile-hero-video {
  width: 100%;
  max-width: 400px;
  height: auto;
  margin: 0 auto 10px;
  display: block;
  border-radius: 8px;
}

.mobile-video-caption {
  background-color: #111;
  padding: 15px;
  margin-bottom: 25px;
  border-radius: 8px;
}
.mobile-video-caption p {
  color: #fff;
  font-size: 16px;
  font-weight: 700;
  margin: 0 0 10px 0;
}
.mobile-whatsapp-btn {
  display: inline-block;
  background-color: #25D366;
  color: #000;
  padding: 10px 20px;
  border-radius: 50px;
  font-weight: 700;
  text-decoration: none;
  font-size: 14px;
}

.mobile-hero h1 {
  color: #ffcc00;
  font-size: 28px;
  margin-bottom: 14px;
  margin-top: 0;
}

.mobile-hero p {
  font-size: 15px;
  line-height: 1.6;
  color: #e0e0e0;
  margin-bottom: 30px;
}

.mobile-cta {
  display: flex;
  flex-direction: column;
  gap: 14px;
  align-items: center;
}

.call-btn, .whatsapp-btn {
  width: 100%;
  max-width: 300px;
  padding: 14px;
  border-radius: 40px;
  font-weight: 700;
  text-decoration: none;
}

.call-btn {
  border: 2px solid #ffcc00;
  color: #ffcc00;
}

.whatsapp-btn {
  background: linear-gradient(135deg, #ffcc00, #e6b800);
  color: #000;
}

/* --- RESPONSIVE ADJUSTMENTS --- */
@media (max-width: 1150px) {
  /* Hides the complex desktop navigation on smaller screens to prevent layout breaking */
  .header-nav { display: none; }
}

@media (max-width: 768px) {
  .hero-slide { display: none; }
  .mobile-hero { display: block; }
  .hero-slider { height: auto; }
  .header-container { padding: 15px 20px; justify-content: center; }
  .header-phone-section { display: none; } /* Focus on just the logo for mobile header initially */
}
</style>

<!-- ================= SCRIPTS ================= -->
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
