//this function stops the form from reloading the screen when the user clicks on the input type=submit button

    let form = document.getElementById("formToLowercaseWord");
    function handleForm(event) { event.preventDefault(); } 
    form.addEventListener('submit', handleForm);