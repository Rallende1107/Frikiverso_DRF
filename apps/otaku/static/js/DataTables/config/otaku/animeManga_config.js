new DataTable('#example', {
    responsive: true,
    info: true,
    paging: true,
    destroy: true,
    ordering: true,
    defRender: true,
    // autoWidth: false,
    pagingType: "full",
    language: {
        "url": "https://cdn.datatables.net/plug-ins/1.10.19/i18n/Spanish.json",
        paginate: {
            first: '<i class="bi bi-chevron-bar-left"></i>',
            last: '<i class="bi bi-chevron-bar-right"></i>',
            next: '<i class="bi bi-chevron-right"></i>',
            previous: '<i class="bi bi-chevron-left"></i>'
        },
        info: "Mostrando _START_ a _END_ de _TOTAL_ registros<br><strong>Página _PAGE_ de _PAGES_</strong>"
    },
    order: [[0, 'asc']],
    pageLength: 20,
    lengthMenu: [
        [10, 25, 50, -1],
        [10, 25, 50, 'All']
    ],
    layout: {
        topStart: {
            buttons: [
                {
                    extend: 'copy',
                    className: 'dataTable-buttons btn-copy',
                    text: '<i class="bi bi-copy"></i> Copiar',
                    footer: false,
                    exportOptions: {
                        columns: ':not(:last-child)'
                    }
                },
                {
                    extend: 'csv',
                    className: 'dataTable-buttons btn-excel',
                    text: '<i class="bi bi-filetype-csv"></i> CSV',
                    footer: false,
                    exportOptions: {
                        columns: ':not(:last-child)'
                    }
                },
                {
                    extend: 'excel',
                    className: 'dataTable-buttons btn-excel',
                    text: '<i class="bi bi-file-excel"></i> Excel',
                    footer: false,
                    exportOptions: {
                        columns: ':not(:last-child)'
                    }
                },
                {
                    extend: 'pdf',
                    className: 'dataTable-buttons btn-pdf',
                    text: '<i class="bi bi-file-pdf"></i> PDF',
                    footer: false,
                    exportOptions: {
                        columns: ':not(:last-child)'
                    }
                },
                {
                    extend: 'print',
                    className: 'dataTable-buttons btn-print',
                    text: '<i class="bi bi-printer"></i> Imprimir',
                    footer: false,
                    exportOptions: {
                        columns: ':not(:last-child)'
                    }
                },
                {
                    extend: 'colvis',
                    className: 'dataTable-buttons btn-colvis',
                    text: '<i class="bi bi-layout-three-columns"></i> Columnas',
                    footer: false,
                    exportOptions: {
                        columns: ':not(:last-child)'
                    }
                },
                {
                    extend: 'pageLength',
                    className: 'dataTable-buttons btn-pageLength',
                    text: '<i class="bi bi-123"></i> Filas',
                    footer: false,
                    exportOptions: {
                        columns: ':not(:last-child)'
                    }
                }
            ]
        }
    },
    columnDefs: [
        { target: 0, visible: true, searchable: false, responsivePriority: 100 }, // ID
        { target: 1, visible: true, searchable: false, responsivePriority: 3 }, // Inicial
        { target: 2, visible: true, searchable: true, responsivePriority: 0 }, // Nombre (Título) Nombre E
        { target: 3, visible: true, searchable: true, responsivePriority: 7 }, // Nombre J
        { target: 4, visible: true, searchable: false, responsivePriority: 2 }, // Eps
        { target: 5, visible: true, searchable: true, responsivePriority: 4 }, // Estado
        { target: 6, visible: true, searchable: false, responsivePriority: 5 }, // Activo
        { target: 7, visible: true, searchable: false, responsivePriority: 0 }, // Acciones
    ],
});