// Dove tutte le parti dinamiche del sito vengono effettuate

// LAYOUT
// Se click sull'immagine o scritta nella barra di navigazione torna alla home
const banners = document.querySelectorAll(".banner")
if (banners) {
    banners.forEach(banner => {
        banner.addEventListener("click", () => {
            categoria = banner.getAttribute("id");
            if (categoria == "moto") window.location.href = "/fantamoto";
            else if (categoria == "formula") window.location.href = "/fantaformula";
            else window.location.href = "/";
        })
    })
}
 
// ERRORE
const errore_btn = document.getElementById("errore-btn");
if (errore_btn) {
    errore_btn.addEventListener("click", () => {
        categoria = errore_btn.getAttribute("value");
        if (categoria == "moto") window.location.href = "/fantamoto";
        else if (categoria == "formula") window.location.href = "/fantaformula";
        else window.location.href = "/";
    })
}


// MOTO_HOME e FORMULA_HOME
// Se click sui pulsanti "classifica" nella home, mostra/togli classifica
const btn_scontri = document.getElementById("btn-scontri");
const btn_punti = document.getElementById("btn-punti");
div_scontri = document.getElementById("div-scontri");
div_punti = document.getElementById("div-punti");
// Classifica scontri
if (btn_scontri) {
    btn_scontri.addEventListener("click", () => {
        if (div_scontri.style.display == "none") {
            div_scontri.style.display = "block";
            div_punti.style.display = "none";
        }
        else {
            div_scontri.style.display = "none";
        }
    })
}
// Classifica punti
if (btn_punti) {
    btn_punti.addEventListener("click", () => {
        if (div_punti.style.display == "none") {
            div_punti.style.display = "block";
            div_scontri.style.display = "none";
        }
        else {
            div_punti.style.display = "none";
        }
    })
}

// MOTO_CALENDARIO e FORMULA_CALENDARIO
// Scrolla barra orizzontale fino a opzione attiva
numero_date = document.querySelectorAll(".cale-opzione").length;
data_sel = document.querySelector("#attivo");
if (numero_date && data_sel) {
    data_selez = data_sel.innerHTML
    scroller = document.getElementById("cale-scroll");
    scroll_maxwidth = scroller.scrollWidth - scroller.clientWidth;
    howmuch = data_selez / numero_date * scroll_maxwidth - 10;
    document.getElementById("cale-scroll").scrollLeft += howmuch;
}
// Seleziona solo sfide di giornata selezionata
if (data_sel) {
    data_selez = data_sel.innerHTML;
    mostra_gare(data_selez);
}
// Mostra sfide della giornata selezionata
function mostra_gare(numero) {
    tutte_sfide = document.querySelectorAll(".cale-giornata");
    for (i=1; i < tutte_sfide.length+1; i++) {
        questagiornata = document.getElementById(i);
        if (i == numero && questagiornata.className == "cale-giornata") {
            questagiornata.style.display = "block";
        }
        else if (i != numero && questagiornata.className == "cale-giornata") {
            questagiornata.style.display = "none";
        }
    }
}
// Cambia giornata selezionata
function cambia_attivo(e) {
    numerodata = e.target.getAttribute("num");
    ex_selez = document.getElementById("attivo");
    nuovo_selez = e.target;
    ex_selez.removeAttribute("id");
    nuovo_selez.setAttribute("id", "attivo");
    mostra_gare(numerodata);
}

// MOTO_CALCOLO e FORMULA_CALCOLO (scegli quale gara calcolare)
btn_gara_calcolo = document.getElementById("calc-btn");
if (btn_gara_calcolo) {
    btn_gara_calcolo.addEventListener("click", () => {
        button_classes = btn_gara_calcolo.className;
        if (button_classes.includes("btn-primary")) {
            categoria = "fantamoto";
        }
        else if (button_classes.includes("btn-danger")) {
            categoria = "fantaformula";
        }
        numero = document.getElementById("calc-select").value;
        window.location.href = `/${categoria}/calcolo-${numero}`;
    })
}

// MOTO_FORMAZIONE e FORMULA_FORMAZIONE
// Al click di un'opzione in "formazione", selezionala
opzioni = document.querySelectorAll(".form-opzione");
if (opzioni) {
    opzioni.forEach(opzione => {
        opzione.addEventListener("click", () => {
            seleziona(opzione)
        })
    })
}
// Selezionare/Deselezionare opzione
function seleziona(op) {
    if (op.id == "selezionato") {
        op.querySelector("#form-check").checked = false;
        op.removeAttribute("id");
    }
    else {
        op.querySelector("#form-check").checked = true;
        op.setAttribute("id", "selezionato");
    }
}

// MOTO_CALCOLOGARA e FORMULA_CALCOLOGARA
btn_calcavviso = document.getElementById("btn-calcavviso");
if (btn_calcavviso) {
    btn_calcavviso.addEventListener("click", () => {
        avviso = document.getElementById("calcavviso");
        if (avviso.style.display == "none") {
            avviso.style.display = "block";
        }
        else {
            avviso.style.display = "none";
        }
    })
}

// ERRORE 404 e ERRORE 500
link_moto = document.getElementById("errore-moto");
link_formula = document.getElementById("errore-formula");
if (link_formula && link_moto) {
    link_moto.addEventListener("click", () => {
        window.location.href = "/fantamoto";
    })
    link_formula.addEventListener("click", () => {
        window.location.href = "/fantaformula";
    })
}


// MOTOCALCOLO/FORMULACALCOLO/MOTOCAMBIOPILOTA/FORMULACAMBIOPILOTA
// Cerca per i piloti nella barra di ricerca delle qualifiche
function cercaPilota(tag) {
    const inputId = tag.id;
    const inputValue = tag.value;
    let results = document.getElementById("listapiloti").value;
    results = results.replace(/'/g, '"');
    results = JSON.parse(results);
    const parentElement = document.getElementById(`dropdown-menu${inputId}`);
    const elementsToRemove = document.querySelectorAll("li");
    elementsToRemove.forEach(element => {
        element.remove();
    });
    if (inputValue) {
        const matchingWords = results.filter(word => word.includes(inputValue));
        matchingWords.sort((a, b) => {
            const indexA = a.indexOf(inputValue);
            const indexB = b.indexOf(inputValue);
            return indexA - indexB;
        });
        matchingWords.forEach(word => {
            const listItem = document.createElement("li");
            const link = document.createElement("a");
            link.classList.add("dropdown-item");
            link.textContent = word;
            link.addEventListener("click", () => {
                // Nel button inserisci il nome del pilota selezionato
                const btn = document.getElementById(`dropdownMenuButton${inputId}`);
                btn.innerHTML = word;
                // Cambio nome pilota
                if (window.location.pathname.includes("adm-piloti")) {
                    const hiddeninput = document.getElementById("oldname");
                    hiddeninput.value = word;
                }
                // Cambio di scuderie pilota
                else if (window.location.pathname.includes("adm-team")) {
                    if (tag.id == "1") {
                        const hiddeninput = document.getElementById("oldpilota");
                        hiddeninput.value = word;
                    } else if (tag.id == "2") {
                        const hiddeninput = document.getElementById("newpilota");
                        hiddeninput.value = word;
                    }
                }
                // Calcolo gara
                else if (window.location.pathname.includes("calcolo")) {
                    const hiddeninput = document.getElementById(`quali-${inputId}`);
                    hiddeninput.value = word;
                }
            })
            listItem.appendChild(link);
            parentElement.appendChild(listItem);
        });
        if (matchingWords.length == 0) {
            const listItem = document.createElement('li');
            listItem.textContent = "No Item";
            listItem.classList.add('dropdown-item');
            parentElement.appendChild(listItem);
        }
    } else {
        results.forEach(word => {
            const listItem = document.createElement("li");
            const link = document.createElement("a");
            link.classList.add("dropdown-item");
            link.textContent = word;
            link.addEventListener("click", () => {
                const btn = document.getElementById(`dropdownMenuButton${inputId}`);
                btn.innerHTML = word;
            })
            listItem.appendChild(link);
            parentElement.appendChild(listItem);
        });
    }
}


// MODIFICA GARA
function annullaGara() {
    const inputAnnulla = document.getElementById("annullata");
    inputAnnulla.value = "1";
    const submitButton = document.getElementById("submit");
    submitButton.click();
}


// Visualizza Penalità
function viewPen(tag) {
    const inputId = tag.id;
    const divPenalità = document.getElementById(`pen-${inputId}`);
    const divPenInputs = divPenalità.getElementsByTagName('input');
    if (divPenalità.style.display == "block") {
        for (const inputTag of divPenInputs) {
            inputTag.disabled = true;
        }
        divPenalità.style.display = "none";
    }
    else if (divPenalità.style.display == "none") {
        for (const inputTag of divPenInputs) {
            inputTag.disabled = false;
        }
        divPenalità.style.display = "block";
    }
}