$("document").ready(function () {
    if ($("#state").length > 0) {
        var selected_district = $("#district option:selected").val();
        var selected_place = $("#place option:selected").val();

        update_district_by_state($("#state").val());
        $("#district").val(selected_district);
        update_places_by_district($("#district").val());
        $("#place").val(selected_place);


        $("#state").on("change", function () {
            var state = $(this).val();
            update_district_by_state(state);
        });
        $("#district").on("change", function () {
            var district = $(this).val();
            update_places_by_district(district);
        });
    }
});

function update_district_by_state(state) {
    $.ajax({
        url: '/district/' + state,
        type: "GET",
        async: false,
        success: function (data) {
            $('#district').children().remove();
            $("#district").append("<option value='-'>Select District (optional)</option>");
            $('#place').children().remove();
            $("#place").append("<option value='-'>Select Place (optional)</option>");
            data.district_list.forEach(function (a, i) {
                $("#district").append("<option value=" + a[0] + ">" + a[1] + "</option>");
            });
        }
    });
}

function update_places_by_district(district) {
    $.ajax({
        url: "/place/" + district,
        type: "GET",
        async: false,
        success: function (data) {
            $('#place').children().remove();
            $("#place").append("<option value='-'>Select Place (optional)</option>");
            data.place_list.forEach(function (a, i) {
                $("#place").append("<option value=" + a[0] + ">" + a[1] + "</option>");
            });
        }
    });
}