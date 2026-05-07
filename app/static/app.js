function renderMessage(msg) {
  document.getElementById('messages').innerHTML = msg; // CWE-79 DOM XSS
}
