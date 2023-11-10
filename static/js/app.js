// Pop Up Function
let popup = document.getElementById('popup');

function openPopup(id=students.id){
    popup.classList.add('open-popup');

}

function closePopup (){
    popup.classList.remove('open-popup');
}

// Hide and show confirm password error notification(If password does not match)

const showPassword    = document.querySelector('.show');
const showPassword2   = document.querySelector('.cshow');
const createPassword  = document.querySelector('#createPass')
const confirmPassword = document.querySelector('#confirmPass')

showPassword.addEventListener('click', ()=>{
    if ((createPassword.type === 'password') && (confirmPassword.type ==='password')){
        createPassword.type='text';
        confirmPassword.type='text';
        showPassword.classList.replace('fa-eye-slash' ,'fa-eye');
        showPassword2.classList.replace('fa-eye-slash' ,'fa-eye');
    } else{
        createPassword.type= 'password';
        confirmPassword.type= 'password';
        showPassword.classList.replace('fa-eye' ,'fa-eye-slash')
        showPassword2.classList.replace('fa-eye' ,'fa-eye-slash');
    }

});

//Ensuring password match

function verifyPassword(){
let pass1     = document.getElementById('createPass').value;
let pass2     = document.getElementById('confirmPass').value;

if (pass1 === pass2){
    document.getElementById('message').innerHTML='Success';
    document.getElementById('message').style.color='green';
}


}

//User profile submenu dropdown


