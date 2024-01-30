window.addEventListener('DOMContentLoaded', () => {
    var table = $('#datatablesSimpleFinanzas').DataTable({
        search: {
            return: true
        },
        paging: false,
        scrollCollapse: true,
        ordering: false,
        scrollX: true,
        scrollY: '65vh',
        deferRender: true,

    });
});
