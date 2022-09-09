sidebar_active = false;


function open_submenu(element) {
    sub_menu = element.getElementsByClassName("sub-menu");
    x = window.matchMedia("(max-width:1022px)")
    if (x.matches) {
        if (sub_menu[0].style["display"] == "none")
            sub_menu[0].style["display"] = 'block';
        else
            sub_menu[0].style["display"] = "none";

    }


}


function sidebar_open(element) {

    element.classList.toggle("change");
    s = document.getElementsByClassName("navigations-list");
    // s[0].style["transition"] = "0.5s";
    if (sidebar_active) {
        sidebar_active = false;
        s[0].style.transform = 'translate(355px, -20px)'

    }
    else {
        sidebar_active = true;
        s[0].style["transition"] = "0.5s"
        s[0].style.transform = 'translate(50px, -20px)'
    }
}