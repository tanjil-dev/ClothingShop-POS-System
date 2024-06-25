$('#get-sell').click(function(){
$.ajax({
        url: "Url",
        dataType: "json",
        type: "get",
        success: function (data) {

        },
        error: function (xhr, exception, thrownError) {
            var msg = "";
            if (xhr.status === 0) {
                msg = "Not connect.\n Verify Network.";
            } else if (xhr.status == 404) {
                msg = "Requested page not found. [404]";
            } else if (xhr.status == 500) {
                msg = "Internal Server Error [500].";
            } else if (exception === "parsererror") {
                msg = "Requested JSON parse failed.";
            } else if (exception === "timeout") {
                msg = "Time out error.";
            } else if (exception === "abort") {
                msg = "Ajax request aborted.";
            } else {
                msg = "Error:" + xhr.status + " " + xhr.responseText;
            }
            if (callbackError) {
                callbackError(msg);
            }

        }
    });
    });
        function receivedTotal() {
            $(document).ready(function() {
                var a = $('#barcodeTable tfoot tr .received-amount input').val();
                const b = $('#barcodeTable tfoot tr .after-discount').text();
                const c = $('#barcodeTable tfoot tr .total-amount').text();
                var e = $('#barcodeTable tfoot tr .change-amount').html(a-b);
                $('#barcodeTable tfoot tr .received-amount-text').text(a);
                $('#sellConfirm tbody tr .priceDiscountTotal').text(b);
                $('#sellConfirm tbody tr .priceTotal').text(c);
                $('#sellConfirm tbody tr .priceReceived').text(a);
                $('#sellConfirm tbody tr .priceChange').text(e.text());
                console.log(d);
            });
        }

        var search = "{% url 'get-product' %}";
        var sell_product = "{% url 'sell-product' %}";
        function discountTotal() {
            $(document).ready(function() {
                var a = $('#barcodeTable tfoot tr .discount-amount input').val();
                const b = $('#barcodeTable tfoot tr .total-amount').text();
                $('#barcodeTable tfoot tr .after-discount').html(b-a);
                var c = $('#barcodeTable tfoot tr .discount-amount-text').text(a);
                $('#sellConfirm tbody tr .priceDiscountTotal').text(b-a);
                $('#sellConfirm tbody tr .priceTotal').text(b);
                $('#sellConfirm tbody tr .priceDiscount').text(c.text());
                console.log(d);
            });
        }
        function onScanSuccess(qrCodeMessage) {
            var total = 0;
            document.getElementById('result').innerHTML = '<span class="result">'+qrCodeMessage+'</span>';
            var formData = {bar_code_no: qrCodeMessage}; //Array
            $.ajax({
                url: search+"?term="+qrCodeMessage,
                type: "GET", // data type (can be get, post, put, delete)
                data: formData, // data in json format
                dataType: "json",
                success: function (data, textStatus, jqXHR) {
                    var items=[];

                    if(data.quantity > 0) {
                        $('#barcodeTable tbody tr:last').after('<tr><td class="counterCell"></td> <td style="display: none" class="id-product">' + data.id + '</td> <td>' + data.name + '</td> <td style="display: none" " class="barcode-no">' + data.bar_code_no + '</td> <td style="display: none">' + data.quantity + '</td> </td> <td class="total">' + data.selling_price + '</td> </tr');
                        $('#sellConfirm tbody tr:first').after('<tr><td>' + data.name + '</td> <td class="total">' + data.selling_price + '</td> </tr');
                        $('#barcodeTable tbody tr .barcode-no').each( function(){
                            //add item to array
                            items.push( $(this).text() );
                            console.log(items)
                        });

                        var toFindDuplicates = items => items.filter((item, index) => items.indexOf(item) !== index)


                        $('#barcodeTable tbody tr .total').each( function(){
                            //add item to array
                            total = total + parseInt($(this).text());
                            $('#barcodeTable tfoot tr .total-amount').html(total);
                            $('#barcodeTable tfoot tr .after-discount').html(total);
                        });

                        console.log(data);
                        console.log(textStatus);
                        console.log(jqXHR);
                    }
                    else {
                        alert("Product out of stock")
                    }
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log("jqXHR:" + jqXHR);
                    console.log("TestStatus: " + textStatus);
                    console.log("ErrorThrown: " + errorThrown);
                    alert("তথ্য পাওয়া যায়নি");
                }
            });
        }


        function onScanError(errorMessage) {
            //handle scan error
        }

        var html5QrcodeScanner = new Html5QrcodeScanner(
            "reader", { fps: 10, qrbox: 250 });
        html5QrcodeScanner.render(onScanSuccess, onScanError);

        function createPDF() {
            var sTable = document.getElementById('tab').innerHTML;
            var a1 = $('#barcodeTable tbody tr .barcode-no').html();
            console.log(a1)
            var style = "<style>";
            style = style + "table {width: 300px; font: 17px Calibri;}";
            style = style + "table {width: 300px; height: fit-content;}";
            style = style + "table, th, td {border: solid 1px #DDD; border-collapse: collapse;";

            style = style + "</style>";

            // CREATE A WINDOW OBJECT.
            var win = window.open('', '', 'height=700,width=700');


            win.document.write('<title>Payment Receipt_'+a1+'</title>');   // <title> FOR PDF HEADER.
                     // ADD STYLE INSIDE THE HEAD TAG.



            win.document.write(sTable);         // THE TABLE CONTENTS INSIDE THE BODY TAG.


            win.document.close(); 	// CLOSE THE CURRENT WINDOW.
            sell();
            win.print();    // PRINT THE CONTENTS.
        }
        $('#myModal').on('shown.bs.modal', function () {
            $('#myInput').trigger('focus')
        })
        function sell(){
            var product_id=[];
            var total = $(".total-amount").text();
            var discount = $(".discount-amount-text").text();
            var after_discount = $(".after-discount").text();
            var received_amount = $(".received-amount-text").text();
            var change_amount = $(".change-amount").text();
            var payment_type = $(".payment").val();
            $('#barcodeTable tbody tr .id-product').each( function(){
                //add item to array
                id = parseInt($(this).text());
                product_id.push(id);
            });
            var formData = {total: total, discount: discount, after_discount: after_discount, received_amount: received_amount, change_amount: change_amount, payment_type: payment_type, product_id: JSON.stringify(product_id)}; //Array
            $.ajax({
                url: sell_product,
                type: "POST", // data type (can be get, post, put, delete)
                data: formData, // data in json format
                timeout: 2000,	//Is useful ONLY if async=true. If async=false it is useless
                async: false, // enable or disable async (optional, but suggested as false if you need to populate data afterwards)
                success: function (data, textStatus, jqXHR) {
                    alert("পণ্য বিক্রি হয়ে গেছে!")
                    console.log(data)
                    window.location.href = 'http://localhost:8000';
                },
                error: function (jqXHR, textStatus, errorThrown) {
                    console.log("jqXHR:" + jqXHR);
                    console.log("TestStatus: " + textStatus);
                    console.log("ErrorThrown: " + errorThrown);
                    alert("বিক্রি গ্রহণযোগ্য নয়!");
                    window.location.href = 'http://localhost:8000';
                }
            });


            console.log(formData);
        }