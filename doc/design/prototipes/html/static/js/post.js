document.addEventListener("DOMContentLoaded", function () {
    var btnText = document.getElementById("readMore");
    var post_bar = document.getElementById("post-bar");
        var post = document.getElementById("post");
    
    btnText.addEventListener('click', function() {
        var dots = document.getElementById("dots");
        var moreText = document.getElementById("more");

        if (dots.style.display === "none") {
            dots.style.display = "inline";
            btnText.innerHTML = "Ver más";
            moreText.style.display = "none";
        } else {
            dots.style.display = "none";
            btnText.innerHTML = "Ver menos";
            moreText.style.display = "inline";
        }
    });

    post_bar.addEventListener('focus', function() {
        console.log('yup');
        var post_bar = document.getElementById("post-bar");

        post.style.flexDirection = "column";
        post.style.height = 'fit-content';
        post.style.padding = '1rem';

        post_bar.style.height = '150px';
        post_bar.style.width = '100%';

        document.getElementById('post-pfp').style.width = '52px';
        document.getElementById("createPost-options").style.display = "inline";
        document.getElementById("post-user-name").style.display = "inline";
    });

    post.addEventListener('focusout', function() {
        console.log('nop');
        var post_bar = document.getElementById("post-bar");

        post.style.flexDirection = "row";
        post.style.height = '90px';
        post.style.padding = '0 1rem';

        post_bar.style.height = '25px';

        document.getElementById('post-pfp').style.width = '72px';
        document.getElementById("createPost-options").style.display = "none";
        document.getElementById("post-user-name").style.display = "none";
    });
});