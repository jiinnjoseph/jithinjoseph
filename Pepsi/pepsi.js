const track = document.querySelector(".track");
const images = document.querySelectorAll(".track img");

let index = 0;
let slideWidth;
const totalSlides = images.length / 2;

window.onload = () => {
    slideWidth = images[0].offsetWidth + 20;
};

function updateSlide() {
    track.style.transform = `translateX(-${index * slideWidth}px)`;
}

function moveRight() {
    track.style.transition = "transform 0.5s ease";
    index++;
    updateSlide();

    if (index >= totalSlides) {
        setTimeout(() => {
            track.style.transition = "none";
            index = 0;
            updateSlide();
        }, 500);
    }
}

function moveLeft() {
    if (index <= 0) {
        track.style.transition = "none";
        index = totalSlides;
        updateSlide();
    }

    setTimeout(() => {
        track.style.transition = "transform 0.5s ease";
        index--;
        updateSlide();
    }, 10);
}