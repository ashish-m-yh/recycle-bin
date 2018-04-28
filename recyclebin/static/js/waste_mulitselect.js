$("document").ready(function () {
        var wasteGeneratedMultiSelect = $('#wasteGeneratedMultiSelect');
        var wasteRequiredMultiSelect = $('#wasteRequiredMultiSelect');
        var inputSource = $('#inputSource');
        var inputValue = $('#inputValue');
        var quantity = $("#quantityModal");
        var modelHead = $("#modelHead");
        var closeModal = $(".closeModal");
        var addButtonModal = $(".addButtonModal");

        var wasteOptionMap = {};

        var wasteOptions = $("#wasteGeneratedMultiSelect option");
        wasteOptions.each(function (value, option) {
            wasteOptionMap[option.value] = option.text;
        });

        closeModal.on('click', function (e) {
            var inputSource = $('#inputSource').val();
            if (inputSource === "wasteGenerated") {
                $('#wasteGeneratedMultiSelect').multiSelect('deselect', inputValue.val());
            }
            else if (inputSource === "wasteRequired") {
                $('#wasteRequiredMultiSelect').multiSelect('deselect', inputValue.val());
            }
        });
        addButtonModal.on('click', function (e) {
            var inputSource = $('#inputSource').val();
            var value = inputValue.val() + "::" + $("#quantity").val() + "::" + $("#unit").val();
            if (inputSource === "wasteGenerated") {
                var existingVal = $('#wasteGeneratedList').val();
                $('#wasteGeneratedList').val(existingVal + "||" + value);
            }
            else if (inputSource === "wasteRequired") {
                var existingVal = $('#wasteRequiredList').val();
                $('#wasteRequiredList').val(existingVal + "||" + value);
            }
        });

        function afterSelectHandler(values, source) {
            inputSource.val(source);
            inputValue.val(values);
            modelHead.text(wasteOptionMap[values[0]]);
            quantity.modal("show");
            quantity.find(".waste_quantity").val(1);
        }

        function afterDeselectHandler(values, source) {
            if (source === "wasteGenerated") {
                var existingVal = $('#wasteGeneratedList').val();
                var list = existingVal.split("||");
                var valToSave = list.filter(list => list.split("::")[0] !== values[0]).join("||");
                $('#wasteGeneratedList').val(valToSave);
            }
            else if (source === "wasteRequired") {
                var existingVal = $('#wasteRequiredList').val();
                var list = existingVal.split("||");
                var valToSave = list.filter(list => list.split("::")[0] !== values[0]).join("||");
                $('#wasteRequiredList').val(valToSave);
            }
        }

        wasteGeneratedMultiSelect.multiSelect(
            {
                afterSelect: function (values) {
                    afterSelectHandler(values, "wasteGenerated")
                },
                afterDeselect: function (values) {
                    afterDeselectHandler(values, "wasteGenerated")
                }
            }
        );
        wasteRequiredMultiSelect.multiSelect(
            {
                afterSelect: function (values) {
                    afterSelectHandler(values, "wasteRequired")
                },
                afterDeselect: function (values) {
                    afterDeselectHandler(values, "wasteRequired")
                }
            }
        );


    });