var alpha_img=document.querySelector('.alpha-img');
var images=['national-cancer-institute-1c8sj2IO2I4-unsplash.jpg','hush-naidoo-jade-photography-yo01Z-9HQAw-unsplash.jpg','istockphoto-1139755582-612x612.jpg','istockphoto-1403199959-612x612.jpg','istockphoto-1295790747-612x612.jpg'];
var i=0;

function prev()
{
    if(i<=0) i=images.length;
    i--;
    return setImg();
}

function next()
{
    if(i>=images.length-1) i=-1;
    i++;
    return setImg(); 
}

function setImg()
{
    return alpha_img.setAttribute('src','images/'+images[i]);
}