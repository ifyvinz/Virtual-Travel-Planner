document.addEventListener('DOMContentLoaded', function () {
    const likeBtn = document.querySelector('.like-icon-span');
    const unLikeBtn = document.querySelector('.unlike-icon-span');
    document.querySelector('.edit-form').style.display = "none";
    if (likeBtn) {
        likeBtn.addEventListener('click', (event) => {
            const postId = event.target.dataset.id;
            console.log(postId)
            likeButton(postId, likeBtn)
           
        });
    }

    if (unLikeBtn) {
        unLikeBtn.addEventListener('click', (event) => {
            const postId = event.target.dataset.id;
            console.log(postId)
            unLikeButton(postId,  unLikeBtn)
            
        });
    }

    document.querySelector(".edit-icon").addEventListener('click', ()=>{
        editPost();
        document.querySelector('.edit-form').style.display = "block";
    })
});

async function likeButton(postId, likeBtn) {
    
    toggleLikes(postId, likeBtn);
}

async function unLikeButton(postId,  unLikeBtn) {
    
    toggleLikes(postId,  unLikeBtn);
}

const toggleLikes = async (postId, postLikeElement) => {
    try {
        let response = await fetch(`/planner/${postId}/likePost`);
        if (response.ok) {
            const data = await response.json();
            likeUnlike(postLikeElement, data.post.likes.length)
            //countElement.innerHTML = data.post.likes.length;
        } else {
            console.log('Error:', response.status);
        }
    } catch (err) {
        console.error('Error:', err);
    }
};


const likeUnlike = (postLikeElement, likeCount) => {
    let countLike = likeCount;
    if (postLikeElement.classList.contains('like-icon-span')) {
        postLikeElement.classList.remove('like-icon-span');
        postLikeElement.classList.add('unlike-like-icon-span');
        postLikeElement.innerHTML = "";
        postLikeElement.innerHTML = "favorite_border";
        postLikeElement.nextElementSibling.innerHTML = `${countLike}`;
    } else {
        postLikeElement.classList.remove('unlike-like-icon-span');
        postLikeElement.classList.add('like-icon-span');
        postLikeElement.innerHTML = "";
        postLikeElement.innerHTML = "favorite";
        postLikeElement.nextElementSibling.innerHTML = `${countLike}`;
    }
};


const editPost = () =>{
   
    document.querySelector("#blog-div").style.display = "none";
    document.querySelector("#similar-blog-div").style.display = "none";
   
    
}