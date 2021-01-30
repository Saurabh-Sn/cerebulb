var pk = NaN

$(window).on('load', function(){

    if (window.location.pathname == "/products/"){
        get_product_data()

    }
     pk = parseInt(location.pathname.split('/')[2])

    if (isNaN(pk) == false){
    get_product_detail(pk)
   }
});
function get_product_data(){
    $.ajax({
        url : '/api/v1/product/',
        type : 'get',
        dataType:'json',
        success : function(data) {
        console.log()
        if (data.length == 0){
            stri='No data found'
            $(".header-row").after(stri);
        }
        else{

            product_list(data)
            }
        },
        error: function(error) {
        }
    });
}

 function product_list(data){
    $(".table-block").empty();
    stri = ''
    result_len= (data.length)
    for (i=result_len-1;i>=0;i--){
       stri='<tr class="table-block">'+
            '<td class="text-center"><div class="cus-tooltip"><a href="/edit_product/'+data[i].id+'/">'+data[i].product_name+'</a></td><td>'+data[i].product_code+'</td><td>'+data[i].product_category+'</td>'+
            '<td>'+data[i].product_mfg_date+'</td><td> <img width="200" height="200" src="' +data[i].product_images+'"></td>'+
            '</tr>'
            $(".header-row").after(stri);
    }
}


$("#add_form").validate({
    errorPlacement: function errorPlacement(error, element) {
        element.after(error);
    },
    errorClass: 'custom-error',
    rules: {
        product_name: {
            required: true,

            minlength: 1,
            maxlength: 100
        },
        product_code: {
            required: true,

            maxlength: 20
        },
        product_category: {
            required: true,

        },


        product_mfg_date: {
            required: true
        },
        product_picture:{
        extension:'jpeg|jpg|png'
        },

    },
    messages: {
        first_name: {
            required: 'Please enter the first name. ',

        },

        product_code: {
            required: 'Please enter product_ode.',

        },

        product_category: {
            required: 'Please select a category.',
        },
        product_images: {
            required: 'Please select a product images',
        },
        product_mfg_date: {
            required: 'Please enter the  date.'
        },
    },
});


function create_product() {
    if ($("#add_form").valid()) {
        var data = $("#add_form")[0]
        var form_data = new FormData(data)
        $.ajax({
            url: '/api/v1/product/',
            type : 'POST',
            data : form_data,
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
            alert('product added')
            window.location ='/products'
            },
            error: function (data) {
               var i = 0
               for (var key in data.responseJSON) {
                   if (i ==0){

                   alert(data.responseJSON[key][0])
                   }
                   i = i +1
                }
            }
        });
    }
}


function edit_product() {
    if ($("#add_form").valid()) {
        var data = $("#add_form")[0]
        var form_data = new FormData(data)
        $.ajax({
            url: '/api/v1/product/',
            type : 'POST',
            data : form_data,
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
            alert('product added')
            window.location ='/products'
            },
            error: function (data) {
               var i = 0
               for (var key in data.responseJSON) {
                   if (i ==0){

                   alert(data.responseJSON[key][0])
                   }
                   i = i +1
                }
            }
        });
    }
}

function get_product_detail(pk){
    $.ajax({
        url : '/api/v1/product/'+pk+'/',
        type : 'get',
        dataType:'json',
        success : function(data) {
        console.log()
         patch_form(data)
        },
        error: function(error) {
        }
    });
}

function patch_form(data) {
    $("input[name='product_name']").val(data.product_name)
    $("input[name='product_code']").val(data.product_code)

    $("select[name='category_name']").val(data.category_name)

    $("input[name='product_mfg_date']").val(data.product_mfg_date)

}