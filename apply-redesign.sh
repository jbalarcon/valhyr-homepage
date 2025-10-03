#!/bin/bash

# Read the CSS content
CSS_CONTENT=$(cat "/Users/jean-baptistealarcon/coding/valhyr/header-redesign.css")

# Create marker comment to inject CSS after
MARKER='/* Prevent flash when clicking arrow */'

# Add the custom CSS right after the marker
awk -v marker="$MARKER" -v css="$CSS_CONTENT" '
    {
        print
        if (index($0, marker) > 0) {
            print ""
            print css
        }
    }
' "/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned.html" > "/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned-temp.html"

mv "/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned-temp.html" "/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned.html"

echo "CSS injected successfully"
