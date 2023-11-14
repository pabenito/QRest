ws = new WebSocket(`ws://localhost:8000/ws/group/${group}/client/${client}`);
ws.onmessage = function(event) {
    var message_obj = JSON.parse(event.data)
    var counterElement = document.querySelector('input[section=${message_obj.section}][element=${message_obj.element}]')
    counterElement.value = message_obj.quantity
};
ws.onclose = function(event) {
    console.log('WebSocket closed:', event);
};

ws.onerror = function(event) {
    console.error('WebSocket error:', event);
};
function sendMessage(event) {
    event.preventDefault()
    var eventElement = event.currentTarget
    var sectionName = eventElement.getAttribute("section")
    var elementName = eventElement.getAttribute("element")

    var input = document.getElementById("messageText")
    var message = {
            sender: client,
            group: group,
            message: input.value
        };
    ws.send(JSON.stringify(message));
    input.value = ''
    event.preventDefault()
}
