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
        
    });
});


// Toggling a SWITCH TO CHANGE MODE
document.addEventListener('DOMContentLoaded', function () {
    const body = document.querySelector('body');
    const modeSwitch = document.querySelector('.toggle-switch');
    const modeText = document.querySelector('.mode-text');
  
    // Check if dark mode preference is stored
    const isDarkMode = localStorage.getItem('darkMode') === 'true';
  
    // Apply dark mode if the preference is true
    if (isDarkMode) {
      body.classList.add('dark');
      modeText.textContent = 'Light Mode';
    }
  
    // Toggle dark mode on switch click
    document.addEventListener('DOMContentLoaded', function () {
        modeSwitch.addEventListener('click', function () {
            body.classList.toggle('dark');
            const isDarkMode = body.classList.contains('dark');
        
            // Update dark mode preference in localStorage
            localStorage.setItem('darkMode', isDarkMode);
        
            if (isDarkMode) {
              modeText.textContent = 'Light Mode';
            } else {
              modeText.textContent = 'Dark Mode';
            }
          });
        });
      
    });
   
  //Toggle the SIDEBAR
  

