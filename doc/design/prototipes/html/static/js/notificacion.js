document.addEventListener('DOMContentLoaded', function() {
    const notificationsLink = document.querySelector('.notifications-link');
    const popup = document.getElementById('notificationsPopup');
    const closeBtn = document.querySelector('.close-popup');
    
    notificationsLink.addEventListener('click', function(e) {
        e.preventDefault();
        
        const isVisible = popup.style.display === 'block';
        popup.style.display = isVisible ? 'none' : 'block';
        
        notificationsLink.classList.toggle('active', !isVisible);
        
        if (!isVisible) {
            const linkRect = notificationsLink.getBoundingClientRect();
            const textSpan = notificationsLink.querySelector('span');
            const textRect = textSpan ? textSpan.getBoundingClientRect() : linkRect;
            const popupWidth = popup.offsetWidth;
            const popupLeft = textRect.left + textRect.width/2 - popupWidth/2;
            
            popup.style.top = `${linkRect.bottom + window.scrollY}px`;
            popup.style.left = `${popupLeft}px`;
            popup.style.right = 'auto';
        }
    });
    
    closeBtn.addEventListener('click', function() {
        popup.style.display = 'none';
        notificationsLink.classList.remove('active');
    });
    
    window.addEventListener('click', function(e) {
        if (!popup.contains(e.target) && e.target !== notificationsLink && !notificationsLink.contains(e.target)) {
            popup.style.display = 'none';
            notificationsLink.classList.remove('active');
        }
    });
    
    document.querySelectorAll('.notification-menu').forEach(menu => {
        menu.addEventListener('click', function(e) {
            e.stopPropagation();
            // Aquí iría la lógica para mostrar opciones
            console.log('Menú de notificación clickeado');
        });
    });
    document.querySelectorAll('.notification-item').forEach(item => {
        const text = item.querySelector('.notification-text').textContent.toLowerCase();
        const iconContainer = item.querySelector('.notification-icon');
        
        iconContainer.innerHTML = '';
        
        const iconImg = document.createElement('img');
        iconImg.alt = 'Tipo de notificación';
        
        if (text.includes('like') || text.includes('gusta')) {
            iconImg.src = 'static/img/icons/like.svg';
        } else if (text.includes('coment') || text.includes('comment')) {
            iconImg.src = 'static/img/icons/comment.svg';
        }
        
        iconContainer.appendChild(iconImg);
    });
});