const showAlert=(title, text, icon, confirbtn) =>{
    Swal.fire({
        title: title,
        // text: text,
        html:text,
        icon: icon,
        cancelButtonText:confirbtn
    });
}
