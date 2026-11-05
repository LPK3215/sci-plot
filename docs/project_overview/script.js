/* ============================================================
   Sci-Plot Project Overview — Interactive Controller
   Handles Archify iframe switching, animations, counters, and copy.
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {
  'use strict';

  /* ---------- Nav Sticky Blur & Scroll Effect ---------- */
  const nav = document.querySelector('.nav');
  if (nav) {
    const onScroll = () => {
      if (window.scrollY > 40) {
        nav.classList.add('scrolled');
      } else {
        nav.classList.remove('scrolled');
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* ---------- Smooth Anchor Scrolling ---------- */
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const targetId = this.getAttribute('href');
      if (targetId === '#' || targetId === '') return;
      const targetEl = document.querySelector(targetId);
      if (targetEl) {
        e.preventDefault();
        targetEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
        // Update URL hash without jump
        if (history.pushState) {
          history.pushState(null, null, targetId);
        }
      }
    });
  });

  /* ---------- Archify Interactive Diagram Center ---------- */
  const archifyTabs = document.querySelectorAll('.archify-tab');
  const archifyFrame = document.getElementById('archify-frame');
  const archifyTitle = document.getElementById('archify-current-title');
  const archifyBadge = document.getElementById('archify-current-badge');
  const btnOpenExternal = document.getElementById('btn-open-external');
  const btnFullscreen = document.getElementById('btn-fullscreen');
  const archifyViewport = document.getElementById('archify-viewport');

  const diagramMap = {
    'core': {
      title: 'Core Architecture (10-Min Fast-Track)',
      badge: 'core-architecture.html',
      src: '../archify/core-architecture.html'
    },
    'arch': {
      title: 'System Panorama Architecture',
      badge: 'architecture-panorama.html',
      src: '../archify/architecture-panorama.html'
    },
    'workflow': {
      title: 'Workflow Execution Pipeline',
      badge: 'workflow-panorama.html',
      src: '../archify/workflow-panorama.html'
    },
    'sequence': {
      title: 'Invocation Sequence Chain',
      badge: 'sequence-panorama.html',
      src: '../archify/sequence-panorama.html'
    },
    'dataflow': {
      title: 'Data Flow & Storage Pipeline',
      badge: 'dataflow-panorama.html',
      src: '../archify/dataflow-panorama.html'
    }
  };

  if (archifyTabs.length && archifyFrame) {
    archifyTabs.forEach(tab => {
      tab.addEventListener('click', () => {
        const diagramKey = tab.getAttribute('data-diagram');
        const data = diagramMap[diagramKey];
        if (!data) return;

        // Switch active tab styling
        archifyTabs.forEach(t => t.classList.remove('active'));
        tab.classList.add('active');

        // Update iframe source and meta
        archifyFrame.src = data.src;
        if (archifyTitle) archifyTitle.textContent = data.title;
        if (archifyBadge) archifyBadge.textContent = data.badge;
        if (btnOpenExternal) btnOpenExternal.href = data.src;
      });
    });
  }

  // Fullscreen toggle for Archify diagram viewer
  if (btnFullscreen && archifyViewport) {
    btnFullscreen.addEventListener('click', () => {
      if (!document.fullscreenElement) {
        if (archifyViewport.requestFullscreen) {
          archifyViewport.requestFullscreen();
        } else if (archifyViewport.webkitRequestFullscreen) {
          archifyViewport.webkitRequestFullscreen();
        }
        btnFullscreen.innerHTML = '<span>⤢</span> Exit Fullscreen';
      } else {
        if (document.exitFullscreen) {
          document.exitFullscreen();
        }
        btnFullscreen.innerHTML = '<span>⤢</span> Fullscreen';
      }
    });

    document.addEventListener('fullscreenchange', () => {
      if (!document.fullscreenElement) {
        btnFullscreen.innerHTML = '<span>⤢</span> Fullscreen';
      }
    });
  }

  /* ---------- Animated Stat Numbers (Count-Up) ---------- */
  const countUpObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
      if (!entry.isIntersecting) return;
      const el = entry.target;
      const targetVal = parseInt(el.getAttribute('data-target'), 10);
      if (isNaN(targetVal)) return;

      const duration = 1800;
      const startTime = performance.now();

      const updateCount = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);
        // Quartic ease-out
        const eased = 1 - Math.pow(1 - progress, 4);
        el.textContent = Math.floor(eased * targetVal);

        if (progress < 1) {
          requestAnimationFrame(updateCount);
        } else {
          el.textContent = targetVal;
        }
      };

      requestAnimationFrame(updateCount);
      observer.unobserve(el);
    });
  }, { threshold: 0.4 });

  document.querySelectorAll('.count-up').forEach(el => countUpObserver.observe(el));

  /* ---------- Ambient Background Particles Parallax ---------- */
  const orbs = document.querySelectorAll('.bg-particles .orb');
  if (orbs.length && window.matchMedia('(prefers-reduced-motion: no-preference)').matches) {
    window.addEventListener('mousemove', (e) => {
      const offsetX = (e.clientX / window.innerWidth - 0.5) * 24;
      const offsetY = (e.clientY / window.innerHeight - 0.5) * 24;
      if (orbs[0]) orbs[0].style.transform = `translate(${offsetX}px, ${offsetY}px)`;
      if (orbs[1]) orbs[1].style.transform = `translate(${-offsetX * 0.8}px, ${-offsetY * 0.8}px)`;
      if (orbs[2]) orbs[2].style.transform = `translate(calc(-50% + ${offsetX * 0.4}px), calc(-50% + ${offsetY * 0.4}px))`;
    }, { passive: true });
  }

  /* ---------- 3D Card Hover Tilt (Desktop Only) ---------- */
  if (window.matchMedia('(hover: hover) and (pointer: fine)').matches) {
    const tiltCards = document.querySelectorAll('.feature-card, .stat-card, .style-card');
    tiltCards.forEach(card => {
      card.addEventListener('mousemove', (e) => {
        const rect = card.getBoundingClientRect();
        const x = (e.clientX - rect.left) / rect.width - 0.5;
        const y = (e.clientY - rect.top) / rect.height - 0.5;
        card.style.transform = `perspective(1000px) rotateY(${x * 6}deg) rotateX(${-y * 6}deg) translateY(-4px)`;
      });
      card.addEventListener('mouseleave', () => {
        card.style.transform = 'perspective(1000px) rotateY(0deg) rotateX(0deg) translateY(0)';
      });
    });
  }

  /* ---------- Copy to Clipboard for Code Blocks ---------- */
  document.querySelectorAll('.btn-copy').forEach(button => {
    button.addEventListener('click', () => {
      const targetId = button.getAttribute('data-target');
      let textToCopy = '';
      if (targetId) {
        const targetEl = document.getElementById(targetId);
        if (targetEl) textToCopy = targetEl.textContent.trim();
      } else {
        const pre = button.closest('.code-box')?.querySelector('pre code');
        if (pre) textToCopy = pre.textContent.trim();
      }

      if (!textToCopy) return;

      navigator.clipboard.writeText(textToCopy).then(() => {
        const origText = button.textContent;
        button.textContent = '✓ Copied!';
        button.style.color = '#34d399';
        button.style.borderColor = '#34d399';
        setTimeout(() => {
          button.textContent = origText;
          button.style.color = '';
          button.style.borderColor = '';
        }, 2000);
      }).catch(err => {
        console.error('Copy failed:', err);
      });
    });
  });

});

