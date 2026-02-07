// Highlight the active link in the navbar
document.querySelectorAll('.nav-link').forEach(link => {
    if (link.href === window.location.href) {
        link.style.borderBottom = "2px solid white";
    }
});