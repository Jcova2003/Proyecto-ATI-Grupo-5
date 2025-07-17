document.addEventListener("DOMContentLoaded", function () {
    var btnText = document.getElementById("readMore");
    var post_bar = document.getElementById("post-bar");
    var post = document.getElementById("post");
    var mltmedia_upload = document.getElementById('multimedia-upload');
    
    if(btnText) {
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
    }

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
