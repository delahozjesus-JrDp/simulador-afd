document.addEventListener("DOMContentLoaded", () => {
    const campoEstados = document.getElementById("estados");
    const campoAlfabeto = document.getElementById("alfabeto");
    const selectorInicial = document.getElementById("estado_inicial");
    const contenedorFinales = document.getElementById("contenedor-finales");
    const contenedorTransiciones = document.getElementById("contenedor-transiciones");
    const botonGenerar = document.getElementById("generar-tabla");
    const formulario = document.getElementById("form-afd");

    let estados = [];
    let alfabeto = [];

    const separar = (texto) => texto.split(",").map(x => x.trim()).filter(Boolean);

    function elemento(tag, texto, clase) {
        const el = document.createElement(tag);
        el.textContent = texto;
        if (clase) el.className = clase;
        return el;
    }

    function actualizarDatos() {
        estados = separar(campoEstados.value);
        alfabeto = separar(campoAlfabeto.value);

        selectorInicial.replaceChildren(elemento("option", "Selecciona el estado inicial"));
        selectorInicial.options[0].value = "";

        estados.forEach(estado => {
            const opcion = elemento("option", estado);
            opcion.value = estado;
            selectorInicial.appendChild(opcion);
        });

        contenedorFinales.replaceChildren();
        if (!estados.length) {
            contenedorFinales.appendChild(elemento("p", "Primero ingresa los estados.", "empty-message"));
        } else {
            estados.forEach(estado => {
                const label = document.createElement("label");
                label.className = "final-option";
                const check = document.createElement("input");
                check.type = "checkbox";
                check.name = "estados_finales";
                check.value = estado;
                label.append(check, elemento("span", estado));
                contenedorFinales.appendChild(label);
            });
        }

        contenedorTransiciones.replaceChildren(
            elemento("p", "Genera nuevamente la tabla con los datos actuales.", "empty-message")
        );
    }

    function validarEntradas() {
        if (!estados.length || !alfabeto.length) throw new Error("Debes ingresar al menos un estado y un símbolo.");
        if (new Set(estados).size !== estados.length) throw new Error("No puedes ingresar estados duplicados.");
        if (new Set(alfabeto).size !== alfabeto.length) throw new Error("No puedes ingresar símbolos duplicados.");
        if (alfabeto.some(s => [...s].length !== 1)) throw new Error("Cada símbolo debe tener exactamente un carácter.");
        if (estados.some(e => /[,\\s]/.test(e))) throw new Error("Los nombres de estado no deben contener comas ni espacios.");
    }

    function generarTabla() {
        actualizarDatos();
        try { validarEntradas(); }
        catch (error) { alert(error.message); return; }

        const tabla = document.createElement("table");
        tabla.className = "transition-table";
        const thead = document.createElement("thead");
        const filaHead = document.createElement("tr");
        filaHead.appendChild(elemento("th", "Estado"));
        alfabeto.forEach(s => filaHead.appendChild(elemento("th", s)));
        thead.appendChild(filaHead);
        tabla.appendChild(thead);

        const tbody = document.createElement("tbody");
        estados.forEach((estado, i) => {
            const fila = document.createElement("tr");
            fila.appendChild(elemento("th", estado));
            alfabeto.forEach((simbolo, j) => {
                const celda = document.createElement("td");
                const select = document.createElement("select");
                select.name = `transicion_${i}_${j}`;
                select.required = true;
                const inicial = elemento("option", "Destino");
                inicial.value = "";
                select.appendChild(inicial);
                estados.forEach(destino => {
                    const opcion = elemento("option", destino);
                    opcion.value = destino;
                    select.appendChild(opcion);
                });
                celda.appendChild(select);
                fila.appendChild(celda);
            });
            tbody.appendChild(fila);
        });
        tabla.appendChild(tbody);
        contenedorTransiciones.replaceChildren(tabla);
        contenedorTransiciones.appendChild(
            elemento("p", `Se generaron ${estados.length * alfabeto.length} transiciones obligatorias.`, "table-summary")
        );
    }

    campoEstados.addEventListener("input", actualizarDatos);
    campoAlfabeto.addEventListener("input", actualizarDatos);
    botonGenerar.addEventListener("click", generarTabla);

    formulario.addEventListener("submit", evento => {
        try {
            validarEntradas();
            const selects = contenedorTransiciones.querySelectorAll("select");
            if (selects.length !== estados.length * alfabeto.length) {
                throw new Error("Primero debes generar la tabla de transiciones.");
            }
            if ([...selects].some(s => !s.value)) {
                throw new Error("Debes completar todas las transiciones.");
            }
            if (!selectorInicial.value) throw new Error("Selecciona el estado inicial.");
        } catch (error) {
            evento.preventDefault();
            alert(error.message);
        }
    });

    actualizarDatos();
});
