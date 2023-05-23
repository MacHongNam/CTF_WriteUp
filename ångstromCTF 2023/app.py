from flask import Flask, make_response, request, escape, render_template_string


custom_message = "" 
message = input()

if len(message) >= 25:
    custom_message = escape(message)
print(custom_message)
