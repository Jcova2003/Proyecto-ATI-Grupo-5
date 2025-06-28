// JavaScript personalizado para Proyecto ATI

document.addEventListener("DOMContentLoaded", function () {
  console.log("Proyecto ATI cargado correctamente");

  // Efecto smooth scroll para enlaces internos
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      }
    });
  });

  // Efecto hover para las cards
  const cards = document.querySelectorAll(".feature-card");
  cards.forEach((card) => {
    card.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-5px)";
    });

    card.addEventListener("mouseleave", function () {
      this.style.transform = "translateY(0)";
    });
  });

  // Efecto de typing para el título (opcional)
  const title = document.querySelector(".hero-section h1");
  if (title) {
    const text = title.textContent;
    title.textContent = "";
    let i = 0;

    function typeWriter() {
      if (i < text.length) {
        title.textContent += text.charAt(i);
        i++;
        setTimeout(typeWriter, 100);
      }
    }

    // Descomenta la siguiente línea si quieres el efecto typing:
    // typeWriter();
  }
});

// Función para mostrar notificaciones (opcional)
function showNotification(message, type = "info") {
  const notification = document.createElement("div");
  notification.className = `alert alert-${type} alert-dismissible fade show position-fixed`;
  notification.style.top = "20px";
  notification.style.right = "20px";
  notification.style.zIndex = "9999";
  notification.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

  document.body.appendChild(notification);

  // Auto-remove después de 5 segundos
  setTimeout(() => {
    if (notification.parentNode) {
      notification.remove();
    }
  }, 5000);
}
