<section class="hero-slider">

  <div class="hero-slide active" style="background-image:url('https://tourwithanand.com/wp-content/uploads/2025/06/home-banner-2.png');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>South India Tours & Beyond</h1>
        <p>Kochi Airport–based personalized South India tours with brand new vehicles, premium service, and complete travel support across Kerala and Tamil Nadu.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <div class="hero-slide" style="background-image:url('https://tourwithanand.com/wp-content/uploads/2025/06/home-banner-1.png');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>Kerala & Tamil Nadu Tour Packages</h1>
        <p>Custom holidays and pilgrimage tours across South India.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <div class="hero-slide" style="background-image:url('https://tourwithanand.com/wp-content/uploads/2025/06/travel.jpg');">
    <div class="hero-overlay">
      <div class="hero-content">
        <h1>Kochi Airport Taxi Service</h1>
        <p>24×7 airport pickup and drop with professional drivers.</p>
        <a href="https://wa.me/919400620615" class="hero-btn">Book Now</a>
      </div>
    </div>
  </div>

  <div class="mobile-hero">
    <video class="mobile-hero-video" autoplay loop muted playsinline poster="https://tourwithanand.com/wp-content/uploads/2025/06/home-banner-2.png">
      <source src="https://tourwithanand.com/wp-content/uploads/2026/06/U_made_a_mistake_U_have_to_rem-online-video-cutter.com_.mp4" type="video/mp4">
      Your browser does not support the video tag.
    </video>

    <div class="mobile-video-caption">
        <p>Hi Friends, I'm MAX! Connect with my friend Anand</p>
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

<style>
/* ================= DESKTOP STYLES ================= */
.hero-slider {
  position: relative;
  height: 90vh;
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

/* ================= MOBILE STYLES ================= */
.mobile-hero {
  display: none;
  padding: 40px 20px;
  text-align: center;
  color: #fff;
  background: linear-gradient(180deg, #0b0f14, #000);
}

.mobile-hero-video {
  width: 100%;
  max-width: 400px;
  height: auto;
  margin: 0 auto 10px; /* Reduced bottom margin to make caption closer */
  display: block;
  border-radius: 8px;
}

/* Max Section Styling */
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

/* ================= RESPONSIVE ================= */
@media (max-width: 768px) {
  .hero-slide { display: none; }
  .mobile-hero { display: block; }
  .hero-slider { height: auto; }
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
