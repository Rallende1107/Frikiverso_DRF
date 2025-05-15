// static/js/utils/handle_messages.js

document.addEventListener('DOMContentLoaded', function() {
    const messagesContainer = document.getElementById('messages-container');

    if (messagesContainer) {
        const messages = JSON.parse(messagesContainer.getAttribute('data-messages'));
        messages.forEach(function(message) {
            const messageType = message.tags.includes('error') ? 'error' : 'success';
            showAlert("Mensaje", message.message, messageType, "OK");
        });
    }
});
