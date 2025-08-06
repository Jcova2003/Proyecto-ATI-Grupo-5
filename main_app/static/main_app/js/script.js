// JavaScript personalizado para Proyecto ATI

document.addEventListener("DOMContentLoaded", function () {
  console.log("Proyecto ATI cargado correctamente");
  var searchPerson = document.getElementById("search-person");
  var searchFriends = document.querySelector(".search-friends");
  const mediaQueryList = window.matchMedia("(max-width: 992px)");

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

  document.querySelectorAll('.back-link').forEach((anchor) => {
   anchor.href = document.referrer;
  });

  searchPerson.addEventListener("click", function() {
    if (mediaQueryList.matches) {
      var searchBar = searchFriends.querySelector(".search-bar");

      document.getElementById("navbar-brand").style.display = "none";
      document.querySelector(".nav-chat").style.display = "none";
      searchFriends.style.width = "100%";
      searchBar.style.display = "unset";
      document.querySelector(".center").style.display = "none";
      
      document.querySelector(".my-friends").style.display = "unset";
    }
  });


  window.addEventListener('click', function(e){   
        if (!searchFriends.contains(e.target)){
          searchFriends.style = "";
          document.getElementById("navbar-brand").style = "";
          document.querySelector(".nav-chat").style = "";
          searchFriends.querySelector(".search-bar").style = "";
          document.querySelector(".center").style = "";
          document.querySelector(".my-friends").style = "";
        }
    });

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
