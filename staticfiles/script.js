$(document).ready(() => {
    $('#hamburger-menu').click(() => {
        $('#hamburger-menu').toggleClass('active')
        $('#nav-menu').toggleClass('active')
    })

    // setting owl carousel

    let navText = ["<i class='bx bx-chevron-left'></i>", "<i class='bx bx-chevron-right'></i>"]

    $('#hero-carousel').owlCarousel({
        items: 1,
        dots: false,
        loop: true,
        nav:true,
        navText: navText,
        autoplay: true,
        autoplayHoverPause: true
    })
    $('#top-movies-slide').owlCarousel({
        items:6,
        dots:false,
        loop:true,
        autoplay:false,
        autoplayHoverPause: true,
        responsive:{
            500:{
                items:3
            },
            1280:{
                items:4
            },
            1600:{
                items:6
            },
            
        }
    })
    $('.movies-slide').owlCarousel({
        items: 2,
        dots: false,
        nav:true,
        navText: navText,
        margin: 15,
        responsive: {
            500: {
                items: 2
            },
            1280: {
                items: 4
            },
            1600: {
                items: 6
            }
        }
    })
})

const user_input = document.getElementById("user-input")
let search_icon = $('#search-outline')
const csrf = document.getElementsByName('csrfmiddlewaretoken')[0].value
const artistsDiv = document.getElementById('searcha')
const user_input1 = document.getElementById("user-input1")
let search_icon1 = $('#search-outline1')
const csrf1 = document.getElementsByName('csrfmiddlewaretoken')[0].value

// let endpoint = '/'
// let delay_by_in_ms = 700
// let scheduled_function = false

// let ajax_call = function (endpoint, request_parameters) {
//     $.getJSON(endpoint, request_parameters)
//         .done(response => {
//             // fade out the artists_div, then:
//             artists_div.fadeTo('slow', 0).promise().then(() => {
//                 // replace the HTML contents
//                 artists_div.html(response['html_from_view'])
//                 // fade-in the div with new contents
//                 artists_div.fadeTo('slow', 1)
//                 // stop animating search icon
//                 search_icon.removeClass('blink')
//             })
//         })
// }
// const mobileNav = document.querySelector(".searchmob")

// const viewportWidth = Math.max(document.documentElement.clientWidth || 0, window.innerWidth || 0)

// function removeFromDomBasedOnWv(width){
// // if width is less or equal 480 ...
//     if(width <= 880){
//         // ...remove element from DOM
//         mobileNav.parentNode.removeChild(mobileNav);
//     }
// return
// }
// removeFromDomBasedOnWv(viewportWidth)
const sendAjax = (resa) => {
    $.ajax({
        type: 'POST',
        url:'/search/',
        // responsive: true,
        data:{
            'csrfmiddlewaretoken':csrf,
            'result':resa,
        },
        success: (res)=> {
            console.log(res.data)
            const data = res.data;
            if(data !== 'Not Found'){
                if (Array.isArray(data) && data.length > 0){
                    artistsDiv.innerHTML = ""
                    data.forEach(resa=> {
                        let tita = resa.title.replace('مشاهدة','')
                        if (resa.title.includes('فيلم'))
                            {
                                artistsDiv.innerHTML += 
                                `
                                <a href=''>
                                    <div class='row mt-2 mb-2'>
                                        <div class='col-12' id='moviesearch'>
                                            <div class="ac-results hidden-sm hidden-xs" style="left: 589.969px; display: block;">
                                                <ul>
                                                    <li class="ac-item-hover">
                                                        <a href="view/${resa.movieid}">
                                                            <img src="${resa.poster}">
                                                            <span>${tita}</span>
                                                            <p>${resa.year}</p>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </a>
                                `
                            }
                        else if(resa.title.includes('مسلسل'))
                            {
                                artistsDiv.innerHTML += 
                                `
                                <a href=''>
                                    <div class='row mt-2 mb-2'>
                                        <div class='col-12' id='moviesearch'>
                                            <div class="ac-results hidden-sm hidden-xs" style="left: 589.969px; display: block;">
                                                <ul>
                                                    <li class="ac-item-hover">
                                                        <a href="serie/${resa.movieid}">
                                                            <img src="${resa.poster}">
                                                            <span>${tita}</span>
                                                            <p>${resa.year}</p>
                                                        </a>
                                                    </li>
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </a>
                                `
                            }
                        })
                }
            }else {
                console.log('ffffffffffffffffff')
                artistsDiv.innerHTML = 
                    `
                    <a href=''>
                        <div class='row mt-2 mb-2'>
                            <div class='col-12' id='moviesearch'>
                                <div class="ac-results hidden-sm hidden-xs" style="left: 589.969px; display: block;">
                                    <ul>
                                        <li class="ac-item-hover">
                                            <a>
                                            <span>لم يتم العثور علي شيء
                                            </span>
                                            </a>
                                        </li>
                                    </ul>
                                </div>
                            </div>
                        </div>
                    </a>
                `
            }
        },
        error: (err)=>{
            console.log(err);
            artistsDiv.innerHTML += 
            `
            <a href=''>
                <div class='row mt-2 mb-2'>
                    <div class='col-12' id='moviesearch'>
                        <div class="ac-results hidden-sm hidden-xs" style="left: 589.969px; display: block;">
                            <ul>
                                <li class="ac-item-hover">
                                    <a>
                                    لم يتم العثور علي شيء
                                    </a>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </a>
            `
        }
    })
}
user_input.addEventListener('keyup', e=>{
    console.log('sad')
    // console.log(e.target.value)
    if (artistsDiv.classList.contains('not-visible')){
        artistsDiv.classList.remove('not-visible')
    };
    sendAjax(e.target.value)
    if ((e.target.value == '')){
        artistsDiv.classList.add('not-visible')
    }

    // var request_parameters = {
    //     q: $(user_input).val() // value of user_input: the HTML element with ID user-input
    // }

    // // start animating the search icon with the CSS class
    // // search_icon.addClass('blink')

    // // if scheduled_function is NOT false, cancel the execution of the function
    // if (scheduled_function) {
    //     clearTimeout(scheduled_function)
    // }

    // // setTimeout returns the ID of the function to be executed
    // scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})
user_input1.addEventListener('keyup', e=>{
    console.log('sad')
    // console.log(e.target.value)
    if (artistsDiv.classList.contains('not-visible')){
        artistsDiv.classList.remove('not-visible')
    };
    sendAjax(e.target.value)
    if ((e.target.value == '')){
        artistsDiv.classList.add('not-visible')
    }
})