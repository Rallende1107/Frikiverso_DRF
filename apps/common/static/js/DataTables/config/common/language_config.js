new DataTable('#example', {
    responsive: true,
    info: true,
    ordering: true,
    paging: true,
    language: {
        //url: "/static/js/DataTables/lang/Spanish.json"
        "url": "https://cdn.datatables.net/plug-ins/1.10.19/i18n/Spanish.json"
    },
    order: [
            [0, 'asc']
            ],
    columnDefs: [
        { target: 0, visible: true, searchable: false, responsivePriority: 99}, // id
        { target: 1, visible:  true, searchable:  true, responsivePriority:  0}, // name initials
        { target: 2, visible:  true, searchable:  true, responsivePriority:  9}, // name_esp initials_esp
        { target: 3, visible:  true, searchable: false, responsivePriority:  5}, // activo
        { target: 4, visible:  true, searchable: false, responsivePriority:  0}, // acciones

    ],
    lengthMenu:[20,5,10,30,40,50],
    layout: {
        topStart: {
            buttons: [
                {
                    extend: 'copy',
                    className: 'btn-copy',
                    text: '<i class="fas fa-copy"></i> Copiar'
                },
                {
                    extend: 'csv',
                    className: 'btn-excel',
                    text: '<i class="fas fa-file-csv"></i> CSV'
                },
                {
                    extend: 'excel',
                    className: 'btn-excel',
                    text: '<i class="fas fa-file-excel"></i> Excel'
                },
                {
                    extend: 'pdf',
                    className: 'btn-pdf',
                    text: '<i class="fas fa-file-pdf"></i> PDF',
                    footer: false
                },
                {
                    extend: 'print',
                    className: 'btn-print',
                    text: '<i class="fas fa-print"></i> Imprimir',
                    footer: false
                },
                {
                    extend: 'colvis',
                    className: 'btn-colvis',
                    text: '<i class="fas fa-columns"></i> Columnas',
                    footer: false
                },
                {
                    extend: 'pageLength',
                    className: 'btn-pageLength',
                    text: '<i class="fas fa-list"></i> Filas',
                    footer: false
                }
            ]
        }
    }
});