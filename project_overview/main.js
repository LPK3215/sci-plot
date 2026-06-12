/* ============================================================
   Sci-Plot Project Overview — Interactive Logic
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

  /* ---- Nav scroll effect ---- */
  const nav = document.querySelector('.nav');
  const handleScroll = () => {
    if (window.scrollY > 60) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  };
  window.addEventListener('scroll', handleScroll, { passive: true });
  handleScroll(); // initial state

  /* ---- Smooth scroll for nav links ---- */
  document.querySelectorAll('.nav-links a[href^="#"]').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const target = document.querySelector(link.getAttribute('href'));
      if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });

  /* ---- Fade-in on scroll (Intersection Observer) ---- */
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15, rootMargin: '0px 0px -40px 0px' });

  document.querySelectorAll('.fade-in').forEach(el => observer.observe(el));

  /* ---- Animated counter for stats ---- */
  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const target = parseInt(el.dataset.target, 10);
      if (isNaN(target)) return;
      const duration = 1600;
      const start = performance.now();
      const step = (now) => {
        const elapsed = now - start;
        const progress = Math.min(elapsed / duration, 1);
        // ease-out cubic
        const eased = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(eased * target);
        if (progress < 1) requestAnimationFrame(step);
      };
      requestAnimationFrame(step);
      counterObserver.unobserve(el);
    });
  }, { threshold: 0.5 });

  document.querySelectorAll('.count-up').forEach(el => counterObserver.observe(el));

  /* ---- Parallax effect on hero orbs ---- */
  const orbs = document.querySelectorAll('.bg-particles .orb');
  if (orbs.length) {
    window.addEventListener('mousemove', (e) => {
      const x = (e.clientX / window.innerWidth - 0.5) * 20;
      const y = (e.clientY / window.innerHeight - 0.5) * 20;
      if (orbs[0]) orbs[0].style.transform = `translate(${x}px, ${y}px) scale(1)`;
      if (orbs[1]) orbs[1].style.transform = `translate(${-x * 0.6}px, ${-y * 0.6}px) scale(1)`;
      if (orbs[2]) orbs[2].style.transform = `translate(calc(-50% + ${x * 0.3}px), calc(-50% + ${y * 0.3}px)) scale(1)`;
    }, { passive: true });
  }

  /* ---- Tilt effect on cards (desktop only) ---- */
  if (window.matchMedia('(hover: hover)').matches) {
    document.querySelectorAll('.card').forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(800px) rotateY(${x * 4}deg) rotateX(${-y * 4}deg) translateY(-4px)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(800px) rotateY(0) rotateX(0) translateY(0)';
      });
    });
  }

  /* ---- Copy code block (for output structure) ---- */
  document.querySelectorAll('.output-tree .line').forEach(line => {
    line.style.cursor = 'default';
    line.title = '文件路径';
  });

});
