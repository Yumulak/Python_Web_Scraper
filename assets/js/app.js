//scroll to top function
const scrollUp = document.querySelector("#scroll-up");

scrollUp.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth",
    });
});

// hamburger menu selections
const burger = document.querySelector("#burger-menu");
const ul = document.querySelector("nav ul");
const nav = document.querySelector("nav");

burger.addEventListener("click", () => {
    ul.classList.toggle("show");
});


// close hamburger menu when clicking on a link
// select nav links
const navLink = document.querySelectorAll(".nav-link");

navLink.forEach((link) =>
    navLink.addEventListener("click", () => {
        ul.classList.remove("show");
    })
);

//drag and drop
function allowDrop(ev) {
    ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
}

function drop(ev) {
    var data = ev.dataTransfer.getData("text");
    ev.target.appendChild(document.getElementById(data));
    // var href = document.querySelector('a').getAttribute('href');
    // window.open(href, "_blank");
    ev.preventDefault();
}
