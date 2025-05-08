document.getElementById('consumoForm').addEventListener('submit', async (e) => {
    e.preventDefault();

    const form = e.target;
    const datos = {
        computadora: form.computadora.checked,
        horas_pc: parseFloat(form.horas_pc.value) || 0,
        cargas_celular: parseInt(form.cargas_celular.value) || 0,
        tv: form.tv.checked,
        cantidad_tv: parseInt(form.cantidad_tv.value) || 0
    };

    const resp = await fetch('/calcular', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(datos)
    });

    const resultado = await resp.json();
    let mensaje = '';
    for (let [key, val] of Object.entries(resultado)) {
        if (key !== "total") {
            mensaje += `${key}: ${val.toFixed(2)} kWh\n`;
        }
    }
    mensaje += `Total diario: ${resultado.total.toFixed(2)} kWh`;

    alert(mensaje);
});
