document.addEventListener("DOMContentLoaded", function () {

    const menuIcon = document.querySelector('.fa-bars');
    const closeIcon = document.querySelector('.header-mobile .fa-close');
    const mobileMenu = document.querySelector('.header-mobile');

    // Открытие мобильного меню
    menuIcon.addEventListener('click', function () {
        mobileMenu.classList.add('active');
    });

    // Закрытие мобильного меню
    closeIcon.addEventListener('click', function () {
        mobileMenu.classList.remove('active');
    });
});