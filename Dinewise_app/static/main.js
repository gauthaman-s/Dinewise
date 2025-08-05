// Example JS for cart and menu actions
console.log('Frontend JS loaded');

// Add shadow to navbar on scroll
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 10) {
        navbar.style.boxShadow = '0 4px 16px rgba(27,94,32,0.13)';
    } else {
        navbar.style.boxShadow = '0 2px 8px rgba(0,0,0,0.04)';
    }
});

// Animate menu buttons on click
const menuBtns = document.querySelectorAll('.menu-btn');
menuBtns.forEach(btn => {
    btn.addEventListener('mousedown', () => {
        btn.style.transform = 'scale(0.96)';
    });
    btn.addEventListener('mouseup', () => {
        btn.style.transform = 'scale(1)';
    });
    btn.addEventListener('mouseleave', () => {
        btn.style.transform = 'scale(1)';
    });
});
