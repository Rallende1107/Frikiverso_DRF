// actions.js
function handleAction(select, id, name, model) {
    const actionMap = {
        "1": "Ver",
        "2": "Editar",
        "3": "Activar",
        "4": "Desactivar",
        // Generos
        "5": "Hacer Explicito",
        "6": "Hacer Normal",
        // Usuario
        "7": "Hacer Miembro",
        "8": "Quitar del Equipo",
        "9": "Hacer Super Usuario",
        "10": "Hacer Usuario Normal",
        "11": "Reiniciar Contraseña",

        "99": "Eliminar",
    };

    console.log(select);
    console.log(id);
    console.log(name);
    console.log(model);

    const action = select.value;
    if (action) {
        const actionText = actionMap[action];

        if (action === "1" | action === "2") {  // Si la acción es editar, enviar el formulario automáticamente
            document.getElementById('id').value = id;
            document.getElementById('action').value = action;
            document.getElementById('model').value = model;
            document.getElementById('name').value = name;
            document.getElementById('action-form').submit();
        } else {
            Swal.fire({
                title: '¿Estás seguro?',
                text: `¿Estás seguro de que quieres ${actionText} el ${model} ${name}?`,
                icon: 'warning',
                showCancelButton: true,
                confirmButtonColor: '#3085d6',
                cancelButtonColor: '#d33',
                confirmButtonText: 'Sí, confirmar',
                cancelButtonText: 'Cancelar'
            }).then((result) => {
                if (result.isConfirmed) {
                    document.getElementById('id').value = id;
                    document.getElementById('action').value = action;
                    document.getElementById('model').value = model;
                    document.getElementById('name').value = name;
                    document.getElementById('action-form').submit();
                } else {
                    select.value = "";  // Reset select after action
                }
            });
        }
    }
}
