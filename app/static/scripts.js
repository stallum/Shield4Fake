document.addEventListener("keydown", function(event) {
    if(event.key === "Enter") {
        document.getElementById('form').submit()
    }
});