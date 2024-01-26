window.addEventListener('DOMContentLoaded', event => {
    console.log('Entre a provedores demo:');
    // Formatting function for row details - modify as you need
    function format(d) {
        // `d` is the original data object for the row
        return (
            '<dl>' +
            '<dt>Full name:</dt>' +
            '<dd>' +
            d.name +
            '</dd>' +
            '<dt>Extension number:</dt>' +
            '<dd>' +
            d.extn +
            '</dd>' +
            '<dt>Extra info:</dt>' +
            '<dd>And any further details here (images etc)...</dd>' +
            '</dl>'
        );
    }

    const dataTable = document.getElementById('example');
    const dataTableAjax= simpleDatatables.ajax = {
        url: 'provedores-demo.json',
        dataSrc: '',
        beforeSend: function () {
            console.log('Before send AJAX request');
        },
        success: function (data) {
            console.log('Data received:', data);
        },
        error: function (error) {
            console.error('Error loading data:', error);
        },
        complete: function () {
            console.log('AJAX request completed');
        }
    }

    let table = new simpleDatatables.DataTable(dataTable, {

        dataTableAjax,
        columns: [
            {
                className: 'dt-control',
                orderable: false,
                data: null,
                defaultContent: ''
            },
            { data: 'name' },
            { data: 'position' },
            { data: 'office' },
            { data: 'salary' }
        ],
        order: [[1, 'asc']]
    });

    // Add event listener for opening and closing details
    table.on('click', 'td.dt-control', function (e) {
        let tr = e.target.closest('tr');
        let row = table.row(tr);

        if (row.child.isShown()) {
            // This row is already open - close it
            row.child.hide();
        }
        else {
            // Open this row
            row.child(format(row.data())).show();
        }
    });

});
