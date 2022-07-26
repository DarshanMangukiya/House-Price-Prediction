function onClickedEstimatePrice(){
    console.log("Estimated Price button Clicked");
    var sqft = document.getElementById("uisqft");
    var bhk = document.getElementById("uibhk");
    var bath = document.getElementById("uibath");
    var location = document.getElementById("uilocations");
    var estprice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price";

    $.post(url, {
        sqft: parseFloat(sqft.value),
        bhk: bhk.value,
        bath: bath.value,
        location: location.value
    },function(data, status) {
        console.log(data.estimated_price);
        estprice.innerHTML = "<h2>" + data.estimated_price.toString() + " Lakhs</h2>";
        console.log(status);
    });
} 


function onPageLoad(){
    console.log("document loaded");
    var url = "http://127.0.0.1:5000/get_location_names";
    $.get(url,function(data, status){
        console.log("got response for get_location_names");
        if(data){
            var locations = data.locations;
            var uilocations =document.getElementById("uilocations");
            $('#uilocations').empty();
            for(var i in locations){
                var opt = new Option(locations[i]);
                $('#uilocations').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;