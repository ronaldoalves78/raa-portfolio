(() => {
  const header = document.querySelector(".site-header");
  const menuButton = document.querySelector(".menu-toggle");
  const navigation = document.querySelector(".site-nav");
  const navigationLinks = [...document.querySelectorAll('.site-nav a[href^="#"]')];
  const year = document.querySelector("#current-year");

  if (year) {
    year.textContent = String(new Date().getFullYear());
  }

  if (!header || !menuButton || !navigation) {
    return;
  }

  header.classList.add("nav-ready");

  const updateHeaderState = () => {
    header.classList.toggle("is-scrolled", window.scrollY > 8);
  };

  updateHeaderState();
  window.addEventListener("scroll", updateHeaderState, { passive: true });

  const closeMenu = () => {
    menuButton.setAttribute("aria-expanded", "false");
    navigation.classList.remove("is-open");
  };

  menuButton.addEventListener("click", () => {
    const willOpen = menuButton.getAttribute("aria-expanded") !== "true";
    menuButton.setAttribute("aria-expanded", String(willOpen));
    navigation.classList.toggle("is-open", willOpen);
  });

  navigationLinks.forEach((link) => {
    link.addEventListener("click", closeMenu);
  });

  document.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
      menuButton.focus();
    }
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth > 680) {
      closeMenu();
    }
  });

  const observedSections = navigationLinks
    .map((link) => document.querySelector(link.getAttribute("href")))
    .filter(Boolean);

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        const visibleSection = entries
          .filter((entry) => entry.isIntersecting)
          .sort((a, b) => b.intersectionRatio - a.intersectionRatio)[0];

        if (!visibleSection) {
          return;
        }

        navigationLinks.forEach((link) => {
          const isCurrent = link.getAttribute("href") === `#${visibleSection.target.id}`;
          if (isCurrent) {
            link.setAttribute("aria-current", "true");
          } else {
            link.removeAttribute("aria-current");
          }
        });
      },
      { rootMargin: "-25% 0px -60%", threshold: [0.1, 0.4, 0.7] },
    );

    observedSections.forEach((section) => observer.observe(section));
  }
})();
