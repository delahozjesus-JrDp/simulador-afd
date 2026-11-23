// Dibuja el diagrama del AFD en SVG sin dependencias externas ni CDN.
document.addEventListener("DOMContentLoaded", () => {
    const contenedor = document.getElementById("afd-graph");
    if (!contenedor) return;

    let datos;
    try { datos = JSON.parse(contenedor.dataset.graph); }
    catch { contenedor.textContent = "No fue posible cargar los datos del grafo."; return; }

    const ns = "http://www.w3.org/2000/svg";
    const crear = (tag, attrs = {}, texto = null) => {
        const el = document.createElementNS(ns, tag);
        Object.entries(attrs).forEach(([k, v]) => el.setAttribute(k, v));
        if (texto !== null) el.textContent = texto;
        return el;
    };

    const estados = datos.estados;
    const n = estados.length;
    const radio = 31;
    const separacion = Math.max(125, Math.min(185, 760 / Math.max(1, n - 1)));
    const ancho = Math.max(520, 150 + (n - 1) * separacion + 100);
    const alto = 300;
    const posiciones = {};
    estados.forEach((e, i) => posiciones[e] = { x: 85 + i * separacion, y: 145 });

    const svg = crear("svg", { viewBox: `0 0 ${ancho} ${alto}`, role: "img", "aria-label": "Diagrama del autómata finito determinista" });
    const defs = crear("defs");
    const marker = crear("marker", { id: "arrow", markerWidth: 10, markerHeight: 10, refX: 8, refY: 3, orient: "auto", markerUnits: "strokeWidth" });
    marker.appendChild(crear("path", { d: "M0,0 L0,6 L9,3 z", fill: "#34495e" }));
    defs.appendChild(marker);
    svg.appendChild(defs);

    // Agrupar símbolos por par origen-destino.
    const grupos = {};
    datos.transiciones.forEach(t => {
        const key = `${t.origen}|||${t.destino}`;
        grupos[key] ||= { origen: t.origen, destino: t.destino, simbolos: [] };
        grupos[key].simbolos.push(t.simbolo);
    });

    Object.values(grupos).forEach((g, index) => {
        const a = posiciones[g.origen], b = posiciones[g.destino];
        const etiqueta = g.simbolos.join(", ");
        if (g.origen === g.destino) {
            const path = crear("path", {
                d: `M ${a.x-17} ${a.y-26} C ${a.x-65} ${a.y-105}, ${a.x+65} ${a.y-105}, ${a.x+17} ${a.y-26}`,
                fill: "none", stroke: "#34495e", "stroke-width": 1.8, "marker-end": "url(#arrow)"
            });
            svg.appendChild(path);
            svg.appendChild(crear("text", { x: a.x, y: a.y-91, "text-anchor": "middle", class: "edge-label" }, etiqueta));
        } else {
            const dx = b.x - a.x;
            const dy = b.y - a.y;
            const len = Math.sqrt(dx*dx + dy*dy);
            const ux = dx/len, uy = dy/len;
            const x1 = a.x + ux*(radio+3), y1 = a.y + uy*(radio+3);
            const x2 = b.x - ux*(radio+8), y2 = b.y - uy*(radio+8);
            const curva = index % 2 === 0 ? -34 : 34;
            const mx = (x1+x2)/2, my = (y1+y2)/2 + curva;
            svg.appendChild(crear("path", {
                d: `M ${x1} ${y1} Q ${mx} ${my} ${x2} ${y2}`,
                fill: "none", stroke: "#34495e", "stroke-width": 1.8, "marker-end": "url(#arrow)"
            }));
            svg.appendChild(crear("text", { x: mx, y: my-7, "text-anchor": "middle", class: "edge-label" }, etiqueta));
        }
    });

    // Flecha de inicio.
    const inicial = posiciones[datos.inicial];
    svg.appendChild(crear("path", {
        d: `M ${inicial.x-75} ${inicial.y} L ${inicial.x-radio-5} ${inicial.y}`,
        stroke: "#ef8b32", "stroke-width": 2.5, fill: "none", "marker-end": "url(#arrow)"
    }));

    estados.forEach(estado => {
        const p = posiciones[estado];
        const esFinal = datos.finales.includes(estado);
        svg.appendChild(crear("circle", {
            cx: p.x, cy: p.y, r: radio,
            fill: esFinal ? "#e5f5eb" : "#eaf2f8",
            stroke: esFinal ? "#198754" : "#245b91",
            "stroke-width": 2.5
        }));
        if (esFinal) svg.appendChild(crear("circle", {
            cx: p.x, cy: p.y, r: radio-6, fill: "none", stroke: "#198754", "stroke-width": 1.8
        }));
        svg.appendChild(crear("text", {
            x: p.x, y: p.y+5, "text-anchor": "middle", class: "state-label"
        }, estado));
    });

    contenedor.replaceChildren(svg);
});
