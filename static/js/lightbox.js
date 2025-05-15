// script.js

// Seleccionamos todas las imágenes y el contenedor del lightbox
const images = document.querySelectorAll('.gallery img');
const lightbox = document.getElementById('lightbox');
const lightboxImage = document.querySelector('.lightbox-image');
const closeBtn = document.querySelector('.lightbox .close');

// Cuando hacemos clic en una imagen
images.forEach(image => {
    image.addEventListener('click', () => {
        lightbox.style.display = 'flex'; // Mostrar lightbox
        lightboxImage.src = image.src; // Cambiar la imagen del lightbox
    });
});

// Cerrar el lightbox
closeBtn.addEventListener('click', () => {
    lightbox.style.display = 'none'; // Ocultar el lightbox
});
