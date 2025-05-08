function mostrarGraficos() {
    const paises = ["USA", "China", "India", "Germany", "UK", "France", "Brazil", "Canada", "Australia", "Japan"];
    const contenedor = document.getElementById("contenedor");

    paises.forEach(pais => {
        const bloque = document.createElement("div");
        bloque.classList.add("grafico-pais");

        const titulo = document.createElement("h2");
        titulo.innerText = pais;
        titulo.classList.add("titulo-pais");

        const img = document.createElement("img");
        img.src = `/grafico/${pais}`;
        img.alt = `Gráfico de ${pais}`;
        img.classList.add("grafico-img");

        bloque.appendChild(titulo);
        bloque.appendChild(img);
        contenedor.appendChild(bloque);
    });
}
