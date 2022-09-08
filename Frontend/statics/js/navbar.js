menu_items = document.getElementsByClassName("menu-item");
block = "block";
inline = "inline";

function open_submenu(element) {
    sub_menu = element.getElementsByClassName("sub-menu");

    if (sub_menu[0].style["display"] == "none")
        sub_menu[0].style["display"] = block;
    else
        sub_menu[0].style["display"] = "none";




}