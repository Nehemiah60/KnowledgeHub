// Pop Up Function
function openPopup(id=students.id){
    let popup = document.getElementById('popup');
    popup.classList.add('open-popup');

}

function closePopup (){
    popup.classList.remove('open-popup');
}

// Hide and show confirm password error notification(If password does not match)


document.addEventListener('DOMContentLoaded', function() {
    const showToggles = document.querySelectorAll('.show');
    const cshowToggles = document.querySelectorAll('.cshow');

    showToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const passwordField = toggle.previousElementSibling; // Assuming the password field is just before the icon
            togglePasswordVisibility(passwordField, toggle);
        });
    });

    cshowToggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const passwordField = toggle.previousElementSibling; // Assuming the password field is just before the icon
            togglePasswordVisibility(passwordField, toggle);
        });
    });
});

function togglePasswordVisibility(passwordField, showElement) {
    if (passwordField.type === 'password') {
        passwordField.type = 'text';
        showElement.classList.replace('fa-eye-slash', 'fa-eye');
    } else {
        passwordField.type = 'password';
        showElement.classList.replace('fa-eye', 'fa-eye-slash');
    }
}

//User profile submenu dropdown
function toggleMenu(){
const subMenu = document.getElementById('subMenu');
subMenu.classList.toggle('open-menu');
}

//accordion in course details
document.addEventListener('DOMContentLoaded', function() {
    const accordionTitle = document.querySelector('.module-details');
    const accordionContent = document.querySelector('.accordion');

    accordionTitle.addEventListener('click', function() {
        // Toggle the 'activeAccord' class on the parent container
        accordionContent.parentElement.classList.toggle('activeAccord');

        // Optionally, you can scroll to the top of the accordion when it's clicked
        //accordionTitle.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
});
