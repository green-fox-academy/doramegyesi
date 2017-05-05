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
    }
];

var mainPicture = document.querySelector('#main-image');
var previous = document.querySelector('#previous');
var next = document.querySelector('#next');
var index = 0;
var infotitle = document.querySelector('.infotitle')
var description = document.querySelector('.description')

function getNext() {
    if (index+1 < allPictures.length) {
        index++;
    } else {
        index = 0;
    }
    mainPicture.setAttribute('src', allPictures[index].source)
    infotitle.innerText = allPictures[index].title;
    description.innerText = allPictures[index].description;
};

function getPrevious() {
    if (index-1 >= 0) {
        index--;
    } else {
        index = allPictures.length-1;
    }
    mainPicture.setAttribute('src', allPictures[index].source)
    infotitle.innerText = allPictures[index].title;
    description.innerText = allPictures[index].description;
};

previous.addEventListener('click', getPrevious);
next.addEventListener('click', getNext);
