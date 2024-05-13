Array.from(document.getElementsByClassName('hanja')).forEach(b => {
    b.addEventListener('click', e => {
        let url = 'https://en.wiktionary.org/wiki/' + b.innerHTML.split(/[( ]/)[0]
        window.open(url, '_blank');
    })
})