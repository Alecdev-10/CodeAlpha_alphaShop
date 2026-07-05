// =========================
// Mobile Navigation
// =========================

const menuBtn = document.getElementById("menuBtn");
const navMenu = document.getElementById("navMenu");

if (menuBtn && navMenu) {

    menuBtn.addEventListener("click", () => {

        navMenu.classList.toggle("active");

    });

}



// =========================
// Auto Hide Django Messages
// =========================

const alerts = document.querySelectorAll(".alert");

alerts.forEach(alert => {

    setTimeout(() => {

        alert.style.transition = "0.4s";

        alert.style.opacity = "0";

        alert.style.transform = "translateY(-10px)";

        setTimeout(() => {

            alert.remove();

        }, 400);

    }, 3500);

});



// =========================
// Confirm Delete
// =========================

const deleteButtons = document.querySelectorAll(".remove-btn");

deleteButtons.forEach(button => {

    button.addEventListener("click", function (event) {

        const confirmDelete = confirm(
            "Remove this product from your cart ?"
        );

        if (!confirmDelete) {

            event.preventDefault();

        }

    });

});



// =========================
// Button Loading Effect
// =========================

const forms = document.querySelectorAll("form");

forms.forEach(form => {

    form.addEventListener("submit", () => {

        const submitButton = form.querySelector(
            "button[type='submit']"
        );

        if (submitButton) {

            submitButton.disabled = true;

            submitButton.innerHTML =
                '<i class="fa-solid fa-spinner fa-spin"></i> Processing...';

        }

    });

});



// =========================
// Card Hover Animation
// =========================

const cards = document.querySelectorAll(".product-card");

cards.forEach(card => {

    card.addEventListener("mouseenter", () => {

        card.style.transition = ".3s";

    });

});



// =========================
// Smooth Scroll
// =========================

document.querySelectorAll("a[href^='#']").forEach(anchor => {

    anchor.addEventListener("click", function (e) {

        e.preventDefault();

        const target = document.querySelector(
            this.getAttribute("href")
        );

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});



// =========================
// Image Preview
// (Future Admin Feature)
// =========================

const imageInput = document.getElementById("imageInput");

const imagePreview = document.getElementById("imagePreview");

if (imageInput && imagePreview) {

    imageInput.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) return;

        const reader = new FileReader();

        reader.onload = function (e) {

            imagePreview.src = e.target.result;

        }

        reader.readAsDataURL(file);

    });

}



// =========================
// Quantity Animation
// =========================

const quantityButtons = document.querySelectorAll(".quantity-btn");

quantityButtons.forEach(button => {

    button.addEventListener("click", () => {

        button.animate(

            [

                { transform: "scale(1)" },

                { transform: "scale(.85)" },

                { transform: "scale(1)" }

            ],

            {

                duration: 180

            }

        );

    });

});



// =========================
// Scroll To Top Button
// =========================

const scrollButton = document.createElement("button");

scrollButton.innerHTML =
'<i class="fa-solid fa-arrow-up"></i>';

scrollButton.className = "scroll-top";

document.body.appendChild(scrollButton);

scrollButton.style.position = "fixed";
scrollButton.style.bottom = "25px";
scrollButton.style.right = "25px";
scrollButton.style.width = "48px";
scrollButton.style.height = "48px";
scrollButton.style.borderRadius = "50%";
scrollButton.style.display = "none";
scrollButton.style.border = "none";
scrollButton.style.cursor = "pointer";
scrollButton.style.background = "#2563eb";
scrollButton.style.color = "#fff";
scrollButton.style.boxShadow = "0 10px 25px rgba(0,0,0,.15)";
scrollButton.style.zIndex = "999";

window.addEventListener("scroll", () => {

    if (window.scrollY > 300) {

        scrollButton.style.display = "block";

    }

    else {

        scrollButton.style.display = "none";

    }

});

scrollButton.addEventListener("click", () => {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

});



// =========================
// Console
// =========================

console.log("AlphaShop Ready");