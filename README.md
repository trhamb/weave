# weave

Weave is a small, text-based application layer protocol built as a learning project.

The goal of Weave is to explore how protocols like HTTP work by creating a much simpler system for requesting and serving documents over a network.

Instead of web pages, Weave serves plain text files that can be viewed in the terminal.

---

## How it works

A client connects to the server over TCP and sends a request in the following format:
```
WEAVE/1 /path
```
Example:
```
WEAVE/1 /about
```
---

## Response format

The server responds with a status line followed by a blank line and a body:
```
<STATUS>

<BODY>
```
<blank line>
<response body>

Example:
```
WOVEN

Welcome to the about page!
```
---

## Status codes

Weave uses simple, thematic status codes:

- WOVEN  
  The request was successful and the page content is returned.

- MISWOVEN  
  The request was malformed (invalid format, missing parts, or bad path).

- TANGLED  
  The request was valid but could not be completed (e.g. unsupported version or missing page).

---

## How pages are served

Requested paths are mapped to text files in the `content/` directory.

For example:
```
/about  →  content/about.txt
```
If the file exists, its contents are returned.  
If not, an error response is sent.

---

## Running the server

Run the server with:
```
python main.py
```
The server will start on:
```
127.0.0.1:7777
```
---

## Testing with netcat

You can connect to and test the server using `nc`:
```
echo "WEAVE/1 /about" | nc 127.0.0.1 7777
```
---

## Project goals

- Understand how application layer protocols work
- Learn socket programming in Python
- Explore request/response design
- Build a minimal “small web” style system

---

## Possible future updates

- Better status codes (e.g. differentiate missing pages vs protocol errors)
- Directory support (listing available pages)
- Support for richer text formats
- A simple Weave client

---

## Notes

This is a learning project and intentionally keeps things simple and minimal, though this does not mean it will make sense to anybody but myself.
