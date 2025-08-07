document.addEventListener('DOMContentLoaded', function () {
    const notificationsLink = document.querySelector('.notifications-link');
    const popup = document.getElementById('notificationsPopup');
    const notificationsLinkMobile = document.querySelector('.mobile-navbar .notifications-link');

    const closeBtn = popup.querySelector('.close-popup');
    closeBtn.addEventListener('click', function () {
        popup.style.display = 'none';
        notificationsLink.classList.remove('active');
    });

    notificationsLink.addEventListener('click', function (e) {
        e.preventDefault();
        const isVisible = popup.style.display === 'block';
        popup.style.display = isVisible ? 'none' : 'block';
        notificationsLink.classList.toggle('active', !isVisible);

        if (!isVisible) {
            const linkRect = notificationsLink.getBoundingClientRect();
            const popupWidth = popup.offsetWidth;
            const popupLeft = linkRect.left + linkRect.width / 2 - popupWidth / 2;

            popup.style.top = `${linkRect.bottom + window.scrollY}px`;
            popup.style.left = `${popupLeft}px`;
            popup.style.right = 'auto';
            
        }
    });

    notificationsLinkMobile.addEventListener('click', function (e) {
        e.preventDefault();
        const isVisible = popup.style.display === 'block';
        popup.style.display = isVisible ? 'none' : 'block';
        notificationsLink.classList.toggle('active', !isVisible);

        if (!isVisible) {
            popup.style.top = '0';
            popup.style.left = '0';
            popup.style.right = 'auto';
            popup.style.bottom = '0';
        }
    });

    window.addEventListener('click', function (e) {
        if (!popup.contains(e.target) && e.target !== notificationsLink && !notificationsLink.contains(e.target) && !notificationsLinkMobile.contains(e.target)) {
            popup.style.display = 'none';
            notificationsLink.classList.remove('active');
        }
    });

    // Opcional: Asignar íconos a las notificaciones ya renderizadas en el HTML
    document.querySelectorAll('.notification-item').forEach(item => {
        const text = item.querySelector('.notification-text').textContent.toLowerCase();
        const iconContainer = item.querySelector('.notification-icon');
        iconContainer.innerHTML = '';

        const iconImg = document.createElement('img');
        iconImg.alt = 'Tipo de notificación';

        const isFriendRequest = text.includes('solicitud de amistad') || text.includes('friend request');

        if (text.includes('like') || text.includes('gusta')) {
            iconImg.src = document.body.dataset.likeIcon;
        } else if (text.includes('coment') || text.includes('comment')) {
            iconImg.src = document.body.dataset.commentIcon;
        } else if (isFriendRequest) {
            iconImg.src = document.body.dataset.friendRequestIcon;
        }

        iconContainer.appendChild(iconImg);
    });


    // Manejar menú clickeable de cada notificación
    document.querySelectorAll('.notification-menu').forEach(menu => {
        menu.addEventListener('click', function (e) {
            e.stopPropagation();
            console.log('Menú de notificación clickeado');
        });
    });

    // Código para manejar "Ver más / Ver menos"
    const verMasLink = document.getElementById('verMasLink');
    const moreNotifications = document.getElementById('moreNotifications');

    if (verMasLink && moreNotifications) {
        verMasLink.addEventListener('click', function(e) {
            e.preventDefault();
            if (moreNotifications.style.display === 'none') {
                moreNotifications.style.display = 'block';
                verMasLink.textContent = 'Ver menos...';
            } else {
                moreNotifications.style.display = 'none';
                verMasLink.textContent = 'Ver más...';
            }
        });
    }
});
