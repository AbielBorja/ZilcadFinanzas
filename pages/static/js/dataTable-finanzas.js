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

// Function to calculate time difference in minutes
function calculateTimeDifference(startTime, endTime) {
    var start = new Date("1970-01-01 " + startTime);
    var end = new Date("1970-01-01 " + endTime);

    var diffInMilliseconds = end - start;
    return diffInMilliseconds / (1000 * 60); // Convert milliseconds to minutes
}
