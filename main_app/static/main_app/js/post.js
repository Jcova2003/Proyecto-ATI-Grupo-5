document.addEventListener("DOMContentLoaded", function () {
    var post_bar = document.getElementById("post-bar");
    var post = document.getElementById("post");
    var mltmedia_upload = document.getElementById('multimedia-upload');
    var posts_content = document.getElementsByClassName('post-content');
    var btnText = document.getElementsByClassName("readMore");

    Array.from(posts_content).forEach(previewText);
    Array.from(btnText).forEach(readMore);

    post_bar.addEventListener('focus', function() {
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


    window.addEventListener('click', function(e){   
        if (!post.contains(e.target)){
            var post_bar = document.getElementById("post-bar");

            post.style.flexDirection = "row";
            post.style.height = '90px';
            post.style.padding = '0 1rem';

            post_bar.style.height = '25px';

            document.getElementById('post-pfp').style.width = '72px';
            document.getElementById("createPost-options").style.display = "none";
            document.getElementById("post-user-name").style.display = "none";
        }
    });

    mltmedia_upload.addEventListener('change', function() {
        var filename = mltmedia_upload.files[0].name;
        var label = document.getElementById('multimedia-upload-btn');
        
        label.innerHTML = filename;
    });

});

function previewText(post_content) {
    var show = post_content.querySelector('#post-text');
    var text = show.getHTML();

    if (text.length > 250) {
        var more = post_content.querySelector('#more');
        show.innerHTML = text.slice(0, 251);
        text = text+" ";
        more.innerHTML = text.slice(251, -1)+"<br>";
    } else {
        post_content.querySelector('#dots').style.display = "none";
        post_content.querySelector('.readMore').style.display = "none";
    }

}

function readMore(btnText) {
    if(btnText) {
        btnText.addEventListener('click', function(e) {
            const post_content = e.target.parentElement;
            var dots = post_content.querySelector("#dots");
            var moreText = post_content.querySelector("#more");

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
    }
}