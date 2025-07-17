document.addEventListener('DOMContentLoaded', function () {
    const notificationsLink = document.querySelector('.notifications-link');
    const popup = document.getElementById('notificationsPopup');

    if (!notificationsLink || !popup) return;

    const closeBtn = popup.querySelector('.close-popup');
    if (closeBtn) {
        closeBtn.addEventListener('click', function () {
            popup.style.display = 'none';
            notificationsLink.classList.remove('active');
        });
    }

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

    window.addEventListener('click', function (e) {
        if (!popup.contains(e.target) &&
            e.target !== notificationsLink &&
            !notificationsLink.contains(e.target)
        ) {
            popup.style.display = 'none';
            notificationsLink.classList.remove('active');
        }
    });

    // ❌ Elimina esta sección si tu HTML no contiene estos elementos:
    /*
    document.querySelectorAll('.notification-item').forEach(item => {
        const textEl = item.querySelector('.notification-text');
        const iconContainer = item.querySelector('.notification-icon');

        if (!textEl || !iconContainer) return;

        const text = textEl.textContent.toLowerCase();
        iconContainer.innerHTML = '';

        const iconImg = document.createElement('img');
        iconImg.alt = 'Tipo de notificación';

        if (text.includes('like') || text.includes('gusta')) {
            iconImg.src = document.body.dataset.likeIcon;
        } else if (text.includes('coment') || text.includes('comment')) {
            iconImg.src = document.body.dataset.commentIcon;
        }

        iconContainer.appendChild(iconImg);
    });
    */

    // ✅ Menú opcional dentro de la notificación
    document.querySelectorAll('.notification-menu').forEach(menu => {
        menu.addEventListener('click', function (e) {
            e.stopPropagation();
            console.log('Menú de notificación clickeado');
        });
    });
    document.querySelectorAll('.notification-item').forEach(item => {
    const text = item.querySelector('.notification-text').textContent.toLowerCase();
    const iconContainer = item.querySelector('.notification-icon');
    if (!iconContainer) return;
    iconContainer.innerHTML = '';

    const iconImg = document.createElement('img');
    iconImg.alt = 'Tipo de notificación';

    if (text.includes('like') || text.includes('gusta')) {
        iconImg.src = document.body.dataset.likeIcon;
    } else if (text.includes('coment') || text.includes('comment')) {
        iconImg.src = document.body.dataset.commentIcon;
    } else {
        return; // No icon to add
    }

    iconContainer.appendChild(iconImg);
});
});
