var allPictures = [
    {
        source: 'images/1.jpg',
        title: 'words of wisdom',
        description: 'Never half-ass two things. Whole-ass one thing.'
    },
    {source: 'images/2.jpg',
    title: 'on women',
    description: 'I am a simple man. I like pretty, dark-haired women and breakfast food.'
},
    {source: 'images/3.jpg',
    title: 'on cats',
    description: 'Any dog under fifty pounds is a cat, and cats are useless.'
},
    {source: 'images/4.jpg',
    title: 'on great outdoors',
    description: 'Fishing relaxes me. It is like yoga, except I still get to kill something.'
},
    {source: 'images/5.jpg',
    title: 'on crying',
    description: 'Keep your tears in your eyes belong.'
},
    {source: 'images/6.jpg',
    title: 'on caring',
    description: 'I am not interested in caring about people.'
}];

var mainPicture = document.querySelector('#main-image');
var previous = document.querySelector('#previous');
var next = document.querySelector('#next');
var index = 0;

function changePictures() {
    if (index+1 < allPictures.length) {
        index++;
        mainPicture.setAttribute('src', allPictures[index].source)
        //mainPicture.setAttribute('src', allPictures[index].title)
    } else if (index+1 === allPictures.length) {
        mainPicture.setAttribute('src', allPictures[0].source)
    }
};

/*function getPrevious() {
    if (index+1 < allPictures.length) {
        index--;
        mainPicture.setAttribute('src', allPictures[index].source)
};*/

previous.addEventListener('click', changePictures);
next.addEventListener('click', changePictures);
