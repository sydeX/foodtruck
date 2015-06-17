var SEARCH_BTN_ID = 'search-btn'
var SEARCH_TXT_ID = 'search-text'
var TEST_ID = 'test-output'
var RESULT_TABLE_ID = 'table-view'
var SORT_BY_NAME_ID = 'sort-by-name'
var SORT_BY_DIST_ID = 'sort-by-dist'
var FILTER_TXT_ID = 'filter-text'
var RANGE_BAR_ID = 'range-bar'

var map
var centerMarker = new google.maps.Marker();
var infowindow = new google.maps.InfoWindow();

var truckMarkerDict = {}
var truckObjList = []
var sortType

function initialize() {
   initializeMap()
   registerListeners()
}

function initializeMap() {
    var mapCanvas = document.getElementById('map-canvas');
    var mapOptions = {
        center: new google.maps.LatLng(37.7749295, -122.4194155),
        zoom: 13,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(mapCanvas, mapOptions);

    markerOption = {
        animation: google.maps.Animation.DROP,
        map: map,
    }
    centerMarker.setOptions(markerOption)
    centerMap(CENTER_LOCATION)
}

function clearCache() {
    truckObjList = []
    truckMarkerDict = {}
}

function centerMap(address) {
   /*
        Triggered when a new center location is entered

        1. Calls server to get a map center coordinates and a list of truck objects
        2. Center map based on the input address
        3. Refresh all truck info with the Json results.

    */
    clearCache()

    $.get('/trucksByAddr', {address: address},
        function(data) {
            if (data.status == 'OK') {
                var center = new google.maps.LatLng(data.mapcenter.lat, data.mapcenter.lng)
                map.setCenter(center)
                centerMarker.setPosition(center);
                prepareTruckLocation(data.trucks)
            } else {
                alert("Failed to look up address " + address + ": " + data.status)
            }
        }, "json")

}

function hasFilterText(checkFields) {
    filterTxt = document.getElementById(FILTER_TXT_ID).value

    if (filterTxt == '') { return true }

    for (var i in checkFields) {
        if (checkFields[i].toLowerCase().indexOf(filterTxt.toLowerCase()) > -1) { return true }
    }

    return false
}

function renderResult() {
    // Render Truck data in result table view and marker view

    var tableRes = ''
    var dist = document.getElementById(RANGE_BAR_ID).value
    truckMarkerList = []
    for (var i in truckObjList){
        var truck = truckObjList[i]

        marker = truckMarkerDict[truck.applicant + truck.address + truck.fooditems]

        if (truck.distance < dist & hasFilterText([truck.applicant, truck.fooditems])) {
            // Only trucks within specified range and matching filter text are rendered
            tableRes += '<tr>'
            tableRes += '<td id=' + i + ' onclick="onSelectTruckItem(this)">'
            tableRes += '<p class=name>' + truck.applicant + '</p>'
            tableRes += '<p class=loc>' + truck.address + '</p>'
            tableRes += '<p class=food>' + truck.fooditems + '</p>'
            tableRes += '</td>'
            tableRes += '<td class=loc>' + truck.distance + 'mi.</td>'
            tableRes += '</tr>'

            if (! marker.getMap()){
                marker.setMap(map)
            }
        }
        else{
            marker.setMap(null)
        }
    }
    document.getElementById(RESULT_TABLE_ID).innerHTML = tableRes
}

function prepareTruckLocation(trucks){
    // process the json result data, populate truck list and marker dictionary

    var circleIcon ={
        path: google.maps.SymbolPath.BACKWARD_CLOSED_ARROW,
        fillColor: '#272833',
        fillOpacity: .4,
        scale: 4.5,
        strokeColor: 'white',
        strokeWeight: 1
    };

    for (var i in trucks){
        var truckInfo = trucks[i]
        truckObjList.push(truckInfo)

        // create a marker for each truck
        var latLang = new google.maps.LatLng(truckInfo.latitude, truckInfo.longitude)
        var marker = new google.maps.Marker ({
            position: latLang,
            icon: circleIcon,
            map: null,
        })

        truckMarkerDict[truckInfo.applicant + truckInfo.address + truckInfo.fooditems] = marker

        infowindowContent = truckInfo.applicant + '<br/>' + truckInfo.address + '<br />' + truckInfo.fooditems
        bindInfowindowToMarker(marker, infowindowContent)
    }
    sortList()
}

function bindInfowindowToMarker(marker, content){
    google.maps.event.addListener(marker, 'click', function() {
        infowindow.setContent(content),
        infowindow.open(map, marker); })
}

function onSelectTruckItem(cell){
    // Open the corresponding marker info window when a truck item is selected from the table
    marker = truckMarkerDict[cell.textContent]
    new google.maps.event.trigger(marker, 'click')
}

function registerListeners(){
    var searchBtn = document.getElementById(SEARCH_BTN_ID);
    var searchTxt = document.getElementById(SEARCH_TXT_ID);

    searchTxt.addEventListener("keyup", centerMapOnEnter );
    searchBtn.addEventListener("click", function() { centerMap(document.getElementById(SEARCH_TXT_ID).value);} );
}

function centerMapOnEnter(event) {
    // re-center the map when enter key is pressed
    if (event.keyCode == "13") {
        centerMap(document.getElementById(SEARCH_TXT_ID).value)
    }
}

function sortList() {
    if (document.getElementById(SORT_BY_NAME_ID).checked == true & sortType != SORT_BY_NAME_ID ){
        // Sort list by name
        sortType = SORT_BY_NAME_ID
        truckObjList.sort(function(a, b) {
            if(a.applicant < b.applicant) return -1;
            if(a.applicant > b.applicant) return 1;
            return 0;
        });
    }
    else if (document.getElementById(SORT_BY_DIST_ID).checked == true & sortType != SORT_BY_DIST_ID) {
        // Sort list by distance
        sortType = SORT_BY_DIST_ID
        truckObjList.sort(function(a, b) {
             return parseFloat(a.distance) - parseFloat(b.distance);
        });
    }
    renderResult()
}

function updateRange(dist){
    // Update results based on the new distance range
    document.getElementById('range-label').innerHTML = dist;
    renderResult()
}

google.maps.event.addDomListener(window, 'load', initialize);

