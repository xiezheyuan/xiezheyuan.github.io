const generateHTML = (data) => {
    const { title, links } = data;
    let html = `<h2 class="ui header">${title}</h2>`;
    html += `<div class="ui divider"></div>`;
    html += `<div class="ui relaxed divided list">`;
    links.forEach(link => {
        html += `
            <div class="item">
                <i class="large ${link.icon} middle aligned icon"></i>
                <div class="content">
                    <a class="header" href="${link.url}" target="_blank">${link.title}</a>
                    <div class="description">${link.summary}</div>
                </div>
            </div>`;
    });
    html += `</div>`;
    html += `<div class="ui divider"></div>`;
    return html;
}


const build = (settings) => {
    // header
    const header = settings.header;
    document.getElementById('header').innerHTML = header;
    // sections
    const sectionsContainer = document.getElementById('sections');
    sectionsContainer.innerHTML = '';
    settings.sections.forEach((section) => {
        const html = generateHTML(section);
        sectionsContainer.innerHTML += html + '\n';
    });
    // footer
    const footer = settings.footer;
    document.getElementById('footer').innerHTML = footer;
    document.title = settings.title;
};