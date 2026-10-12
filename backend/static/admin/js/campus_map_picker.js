document.addEventListener('DOMContentLoaded', function () {
    const latInput = document.getElementById('id_latitude');
    const lngInput = document.getElementById('id_longitude');

    if (!latInput || !lngInput) return;

    // 1. Create main container
    const containerDiv = document.createElement('div');
    containerDiv.style.marginTop = '12px';
    containerDiv.style.marginBottom = '20px';

    // 2. Create "Use My Current Location" Button & Status Label
    const locateBtn = document.createElement('button');
    locateBtn.type = 'button';
    locateBtn.innerHTML = '📍 Use My Current Location';
    locateBtn.className = 'button'; // Standard Django Admin styling
    locateBtn.style.padding = '6px 14px';
    locateBtn.style.cursor = 'pointer';
    locateBtn.style.fontWeight = 'bold';

    const statusSpan = document.createElement('span');
    statusSpan.style.marginLeft = '12px';
    statusSpan.style.fontSize = '12px';
    statusSpan.style.fontWeight = 'bold';

    const buttonWrapper = document.createElement('div');
    buttonWrapper.style.marginBottom = '10px';
    buttonWrapper.appendChild(locateBtn);
    buttonWrapper.appendChild(statusSpan);

    // 3. Create Map Container
    const mapDiv = document.createElement('div');
    mapDiv.id = 'admin-leaflet-map';
    mapDiv.style.height = '360px';
    mapDiv.style.width = '100%';
    mapDiv.style.borderRadius = '8px';
    mapDiv.style.border = '2px solid #cbd5e1';

    containerDiv.appendChild(buttonWrapper);
    containerDiv.appendChild(mapDiv);

    // Insert container below the longitude field row
    const targetRow = lngInput.closest('.form-row') || lngInput.parentElement;
    targetRow.parentNode.insertBefore(containerDiv, targetRow.nextSibling);

    // 4. Parse initial coordinates or default to Dar es Salaam (-6.7924, 39.2083)
    let initialLat = parseFloat(latInput.value) || -6.7924;
    let initialLng = parseFloat(lngInput.value) || 39.2083;

    // 5. Initialize Leaflet Map
    const map = L.map('admin-leaflet-map').setView([initialLat, initialLng], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        attribution: '&copy; OpenStreetMap contributors'
    }).addTo(map);

    let marker = L.marker([initialLat, initialLng], { draggable: true }).addTo(map);

    function updateCoordinates(lat, lng) {
        latInput.value = lat.toFixed(6);
        lngInput.value = lng.toFixed(6);
    }

    // Marker drag event
    marker.on('dragend', function () {
        const pos = marker.getLatLng();
        updateCoordinates(pos.lat, pos.lng);
    });

    // Map click event
    map.on('click', function (e) {
        marker.setLatLng(e.latlng);
        updateCoordinates(e.latlng.lat, e.latlng.lng);
    });

    // Manual coordinate input event
    [latInput, lngInput].forEach(input => {
        input.addEventListener('change', function () {
            const lat = parseFloat(latInput.value) || -6.7924;
            const lng = parseFloat(lngInput.value) || 39.2083;
            const newPos = new L.LatLng(lat, lng);
            marker.setLatLng(newPos);
            map.panTo(newPos);
        });
    });

    // 6. Geolocation Button Click Listener
    locateBtn.addEventListener('click', function () {
        if (!navigator.geolocation) {
            statusSpan.innerText = 'Geolocation is not supported by your browser.';
            statusSpan.style.color = '#dc2626';
            return;
        }

        statusSpan.innerText = 'Detecting current GPS location...';
        statusSpan.style.color = '#2563eb';

        navigator.geolocation.getCurrentPosition(
            function (position) {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;

                // Update form values, marker position, and center map with closer zoom
                updateCoordinates(lat, lng);
                const newPos = new L.LatLng(lat, lng);
                marker.setLatLng(newPos);
                map.setView(newPos, 16);

                statusSpan.innerText = 'Location captured successfully!';
                statusSpan.style.color = '#16a34a';
            },
            function (error) {
                let errorMsg = 'Failed to retrieve location.';
                if (error.code === error.PERMISSION_DENIED) {
                    errorMsg = 'Location permission denied. Enable location in your browser settings.';
                } else if (error.code === error.POSITION_UNAVAILABLE) {
                    errorMsg = 'GPS position unavailable.';
                } else if (error.code === error.TIMEOUT) {
                    errorMsg = 'Location detection timed out.';
                }
                statusSpan.innerText = errorMsg;
                statusSpan.style.color = '#dc2626';
            },
            { enableHighAccuracy: true, timeout: 10000, maximumAge: 0 }
        );
    });
});