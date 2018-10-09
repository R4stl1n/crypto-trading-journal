require.config({
    shim: {
        'datatables.net': ['jquery'],
        'datatablesbootstrap': ['datatables.net']
    },  
    paths: {
        'datatables.net': 'static/plugins/datatables/js/jquery.dataTables.min',
        'datatablesbootstrap': 'static/plugins/datatables/js/dataTables.bootstrap4.min',
    }
});